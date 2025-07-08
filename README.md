🤖 EduBot - AI Academic Assistant
A modern, interactive chatbot designed to help students learn AI and Machine Learning concepts. Built with Flask, TensorFlow, and a beautiful modern UI.

🚀 Features
Smart AI Assistant: Answers questions about ML/AI concepts
Interactive Calculations: Performs accuracy, precision, recall calculations
Modern UI: Beautiful, responsive chat interface
Real-time Chat: Instant responses with typing indicators
Conversation Logging: Saves chat history for improvements
Career Guidance: Provides AI/ML career advice
📁 Project Structure
EduBot/
├── app.py                     # 🧠 Main backend logic (Flask + Chatbot engine)
├── train_model.py             # 🎓 Train and save model from intents.json
├── model.pkl                  # 💾 Trained model (generated after training)
├── intents.json               # 📚 Intent data (QnA)
├── requirements.txt           # 📦 Dependencies
├── README.md                  # 📖 This file
├── templates/
│   └── index.html             # 🎨 Beautiful UI (Flask template)
├── static/
│   └── style.css              # 💅 Modern styling
└── logs/
    └── chat_logs.csv          # 🗃️ User chat history (auto-generated)
🛠️ Installation & Setup
1. Prerequisites
Python 3.8 or higher
pip package manager
2. Clone/Download the Project
bash
# Create project directory
mkdir EduBot
cd EduBot

# Copy all the provided files to this directory
3. Install Dependencies
bash
# Install required packages
pip install -r requirements.txt

# Alternative: Install individually if needed
pip install flask numpy nltk tensorflow keras scikit-learn
4. Train the Model
bash
# Train the chatbot model (this will create model.pkl)
python train_model.py
Expected output:

🎓 Starting EduBot Training...
📊 Training Data Statistics:
   • XX patterns
   • XX intents
   • XX unique words
🧠 Building Neural Network...
⚡ Training model...
✅ Model training completed and saved!
5. Run the Application
bash
# Start the Flask server
python app.py
Expected output:

🚀 Starting EduBot - AI Academic Assistant
📚 Ready to help with AIML concepts, calculations, and career guidance!
 * Running on http://0.0.0.0:5000
6. Access the Chatbot
Open your browser and go to: http://localhost:5000

🎯 Usage Examples
Ask About ML Concepts
"What is machine learning?"
"Explain supervised learning"
"How do neural networks work?"
Calculate Metrics
"Calculate accuracy for 85 correct out of 100 total"
"Find precision and recall for TP=50, FP=10, FN=5"
"Explain confusion matrix"
Career Guidance
"Career in AI"
"Python ML libraries"
"How to become a data scientist"
🔧 Customization
Adding New Intents
Edit intents.json to add new conversation patterns
Re-train the model: python train_model.py
Restart the app: python app.py
Modifying the UI
Edit templates/index.html for structure changes
Edit static/style.css for styling changes
Adding New Features
Modify app.py to add new endpoints or functionality
Update the frontend JavaScript in index.html
🐛 Troubleshooting
Common Issues
Model not found error
❌ Model not found. Please run train_model.py first!
Solution: Run python train_model.py first
NLTK download issues
python
import nltk
nltk.download('punkt')
nltk.download('wordnet')
Port already in use
Change port in app.py: app.run(debug=True, port=5001)
Or kill the process using port 5000
TensorFlow warnings
These are usually harmless compatibility warnings
The model will still work correctly
📊 Model Performance
The chatbot uses a neural network with:

Input layer: Bag of words representation
Hidden layers: 128 and 64 neurons with dropout
Output layer: Intent classification
Training: 200 epochs with SGD optimizer
🗃️ Logs
Chat conversations are automatically saved to logs/chat_logs.csv with:

Timestamp
User message
Bot response
🚀 Deployment
Local Development
Already covered in the setup steps above.

Production Deployment
For production, consider:

Using Gunicorn instead of Flask dev server
Setting up proper logging
Using environment variables for configuration
Adding rate limiting and security measures
📈 Future Enhancements
Add more ML topics and advanced concepts
Implement user authentication
Add voice input/output
Create admin panel for managing intents
Add multi-language support
Integrate with external APIs for real-time data
🤝 Contributing
Feel free to:

Add new intents and responses
Improve the UI/UX
Add new calculation features
Fix bugs and improve performance
📄 License
This project is open source and available under the MIT License.

🆘 Support
If you encounter any issues:

Check the troubleshooting section
Ensure all dependencies are installed
Verify Python version compatibility
Check the console for error messages
Happy Learning with EduBot! 🎓🤖

