from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
model = pickle.load(open('model/fraud_model.pkl', 'rb'))

class Transaction(BaseModel):
    V14: float
    V10: float
    V12: float
    V17: float
    V4: float
    V3: float
    Amount: float
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/ui")
def ui():
    return FileResponse("static/index.html")
@app.get("/")
def home():
    return {"message": "Fraud Detection API"}

@app.post("/predict")
def predict(data: Transaction):
    features = np.zeros(30)
    features[13] = data.V14
    features[9]  = data.V10
    features[11] = data.V12
    features[16] = data.V17
    features[3]  = data.V4
    features[2]  = data.V3
    features[29] = data.Amount

    proba = model.predict_proba(features.reshape(1, -1))[0][1]
    prediction = int(proba >= 0.3)

    return {
        "prediction": prediction,
        "fraud_probability": round(float(proba), 4),
        "result": "FRAUD" if prediction == 1 else "Legitimate"
    }