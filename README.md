# Credit Card Fraud Detection Web Application

## Overview

This project is a machine learning-powered web application that detects fraudulent credit card transactions in real time. The application uses a trained Logistic Regression model and provides predictions through a FastAPI backend with a simple web-based user interface.

## Features

* Real-time fraud prediction
* FastAPI REST API
* Interactive web interface
* Fraud probability score output
* Logistic Regression classification model
* Custom fraud threshold (0.3)
* JSON-based API responses

## Technologies Used

* Python
* FastAPI
* Scikit-learn
* NumPy
* Pandas
* HTML
* CSS
* JavaScript
* Uvicorn

## Project Structure

```text
Fraud_Detection/
│
├── app.py
├── requirements.txt
├── README.md
│
├── model/
│   └── fraud_model.pkl
│
├── static/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
└── .gitignore
```

## Input Features

The model uses the following transaction features:

* V14
* V10
* V12
* V17
* V4
* V3
* Amount

These features were selected based on their importance in detecting fraudulent transactions.

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Fraud_Detection.git
cd Fraud_Detection
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

The application will be available at:

```text
http://127.0.0.1:8000
```

### API Documentation

FastAPI automatically generates interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

### Web Interface

Open:

```text
http://127.0.0.1:8000/ui
```

## API Endpoint

### Predict Fraud

**POST** `/predict`

Example Request:

```json
{
  "V14": -5.0,
  "V10": -3.0,
  "V12": -4.0,
  "V17": -5.0,
  "V4": 2.0,
  "V3": -1.0,
  "Amount": 1000
}
```

Example Response:

```json
{
  "prediction": 1,
  "fraud_probability": 0.8421,
  "result": "FRAUD"
}
```

## Model Information

* Algorithm: Logistic Regression
* Class imbalance handled using `class_weight='balanced'`
* Fraud classification threshold: 0.3
* Model saved using Pickle

## Future Improvements

* Deploy on Render or Railway
* Add transaction history logging
* Improve UI/UX
* Experiment with XGBoost and Random Forest models
* Add authentication and user management
## Live Demo

Frontend:
https://fraud-detection-xjub.onrender.com/ui

API Documentation:
https://fraud-detection-xjub.onrender.com/docs

## Author

Priya Panwar

Machine Learning and Data Science Enthusiast
