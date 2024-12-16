from flask import Flask, request, jsonify
from joblib import load

app = Flask(__name__)

# Load the trained model
model = load("model.pkl")

@app.route('/')
def home():
    return "Flask API for Model Predictions!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = [data['feature1'], data['feature2']]
    prediction = model.predict([features])
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
