# Project 3: Machine Learning Model Deployment with Flask

## Duration

**3 hours and 30 minutes** (including a 20-minute break)

## Tasks

### 1. Model Training

* Load and preprocess data.
* Train a machine learning model using Scikit-Learn.
* Save the trained model using `joblib` or `pickle`.

### 2. Flask Application

* Set up a Flask application.
* Create API endpoints for model predictions.
* Load the saved model and use it for predictions.

### 3. Testing

* Test the Flask API locally.
* Ensure the model is making correct predictions.

### 4. Deployment

* Deploy the Flask application.
* Test the deployed application to ensure it is working correctly.

## Target Audience

* **Data Scientists and Machine Learning Engineers**
  * Professionals looking to learn how to serve machine learning models through APIs.
* **Backend Developers**
  * Those who want to expand their skills by integrating machine learning into backend services using Flask.
* **Full-Stack Developers**
  * Developers interested in incorporating ML-based APIs into their applications.

## Summary of Agenda and Benefits

### Model Training (45 minutes)

* Load and preprocess a dataset using Scikit-Learn, ensuring the data is cleaned and ready for model training.
* Train a machine learning model (e.g., decision tree, random forest, etc.) using Scikit-Learn.
* Save the trained model for future use using `joblib` or `pickle`.
* Use GitHub Copilot to assist in writing preprocessing functions and model training code.
* **Benefits**: Copilot speeds up the process of writing common preprocessing functions and model training loops, reducing errors and saving time.

### Flask Application (50 minutes)

* Set up a Flask web application that will serve the trained model via an API.
* Create API endpoints that accept user input (e.g., JSON data) and return model predictions.
* Load the previously saved model within the Flask app to make predictions on new data.
* Use GitHub Copilot to generate the Flask setup and API endpoint structure quickly.
* **Benefits**: Copilot helps in scaffolding Flask routes and model-loading code, allowing participants to focus on the logic rather than repetitive setup tasks.

### Testing (40 minutes)

* Test the Flask API locally by sending POST requests and ensuring that the model makes accurate predictions.
* Use tools like Postman or cURL to simulate API requests and check the API’s responses.
* Use Copilot to write test cases for checking the accuracy and stability of the API predictions.
* **Benefits**: GitHub Copilot assists in writing test cases, streamlining the testing process, and ensuring coverage for various scenarios.

### Deployment (45 minutes)

* Deploy the Flask application on platforms like Heroku or Render.
* Test the deployed API to ensure it is accessible, making correct predictions, and running smoothly in production.
* Use GitHub Copilot to help with deployment configurations and environment variable setup.
* **Benefits**: Copilot aids in writing deployment scripts and environment configurations, which can save time and reduce deployment errors.

## Participation Requirements

* **Basic Knowledge of Python**
  * Participants should be comfortable with Python programming, including libraries like Pandas and Scikit-Learn.
* **Familiarity with Flask**
  * Basic understanding of creating and running a Flask application.
* **Basic Machine Learning Concepts**
  * Participants should know how machine learning models work and have some experience in training models with Scikit-Learn.

### Tools Setup

* Python, Flask, and Scikit-Learn installed.
* Postman or cURL for testing the API locally.
* GitHub Copilot enabled in their IDE (e.g., VSCode).

* **Optional**: Accounts on platforms like Heroku or Render for deploying the Flask application.
