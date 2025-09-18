
import nltk
import json
import pickle
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import SGD
from nltk.stem import WordNetLemmatizer
import random
import os

nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

def train_model():
    print("🎓 Starting EduBot Training...")

    # ✅ Read intents.json (UTF-8 read mode)
    with open("intents.json", "r", encoding="utf-8") as f:
        intents = json.load(f)

    words = []
    classes = []
    documents = []
    ignore_words = ['?', '.', ',', '!', "'", '"', '(', ')', '[', ']', '{', '}']

    for intent in intents['intents']:
        for pattern in intent['patterns']:
            w = nltk.word_tokenize(pattern)
            words.extend(w)
            documents.append((w, intent['tag']))
            if intent['tag'] not in classes:
                classes.append(intent['tag'])

    words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
    words = sorted(list(set(words)))
    classes = sorted(list(set(classes)))

    print(f"📊 Stats:\n• Patterns: {len(documents)}\n• Intents: {len(classes)}\n• Unique Words: {len(words)}")

    training = []
    output_empty = [0] * len(classes)

    for doc in documents:
        bag = []
        pattern_words = [lemmatizer.lemmatize(word.lower()) for word in doc[0]]
        for w in words:
            bag.append(1 if w in pattern_words else 0)
        output_row = list(output_empty)
        output_row[classes.index(doc[1])] = 1
        training.append([bag, output_row])

    random.shuffle(training)
    training = np.array(training, dtype=object)
    train_x = list(training[:, 0])
    train_y = list(training[:, 1])

    print("🧠 Building Neural Network...")

    model = Sequential()
    model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(len(train_y[0]), activation='softmax'))

    sgd = SGD(learning_rate=0.01, momentum=0.9, nesterov=True)
    model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

    print("⚡ Training...")
    history = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)

    if not os.path.exists("model"):
        os.makedirs("model")

    # ✅ Save model (HDF5 format warning is okay)
    model.save("model/chatbot_model.h5")

    # ✅ Save words + classes in a separate binary file
    # Save metadata
    with open("model/metadata.pkl", "wb") as f:
         pickle.dump({"words": words, "classes": classes}, f)


    print("✅ Model saved at model/chatbot_model.h5")
    print("✅ Metadata saved at model/metadata.pkl")
    print(f"📈 Final Accuracy: {history.history['accuracy'][-1]:.4f}")

if __name__ == '__main__':
    train_model()
