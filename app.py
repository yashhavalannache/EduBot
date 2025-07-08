# ====================================
# ✅ 3. app.py — Flask Chatbot Server
# ====================================

from flask import Flask, render_template, request, jsonify
from flask import Flask, request, jsonify, render_template

import pickle
import numpy as np
import nltk
import json
import random
import os
from keras.models import load_model
from nltk.stem import WordNetLemmatizer
from datetime import datetime

lemmatizer = WordNetLemmatizer()
app = Flask(__name__)

model = load_model('model/chatbot_model.h5')
with open('model/metadata.pkl', 'rb') as f:
    data = pickle.load(f)
    words = data['words']
    classes = data['classes']

with open("intents.json", "r", encoding="utf-8") as f:

    intents = json.load(f)

nltk.download('punkt')
nltk.download('wordnet')

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def bow(sentence, words):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence):
    p = bow(sentence, words)
    res = model.predict(np.array([p]))[0]
    results = [[i, r] for i, r in enumerate(res) if r > 0.25]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def get_response(ints, intents_json):
    if not ints:
        return "🤖 Sorry, I didn't understand. Can you rephrase?"
    tag = ints[0]['intent']
    for i in intents_json['intents']:
        if i['tag'] == tag:
            return random.choice(i['responses'])
    return "🤖 Sorry, I didn't understand."



@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_msg = data.get('message', '')
    ints = predict_class(user_msg)
    res = get_response(ints, intents)
    return jsonify({'response': res})
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    print("🚀 Starting EduBot Server...")
    port = int(os.environ.get('PORT', 5009))
    app.run(host='0.0.0.0', port=port, debug=False)
 
    