from fastapi import FastAPI, Query
from pydantic import BaseModel
import joblib
import numpy as np

# Load the saved model
model = joblib.load("diabetes_model.pkl")

# Define input schema (for POST JSON requests)
class DiabetesInput(BaseModel):
    Pregnancies: int
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int

app = FastAPI(title="Pima Diabetes Prediction API")

@app.get("/")
def home():
    return {"message": "Welcome to the Diabetes Prediction API 🚀"}

# ✅ POST method (for JSON input via Swagger/clients)
@app.post("/predict")
def predict_post(data: DiabetesInput):
    features = np.array([[ 
        data.Pregnancies,
        data.Glucose,
        data.BloodPressure,
        data.SkinThickness,
        data.Insulin,
        data.BMI,
        data.DiabetesPedigreeFunction,
        data.Age
    ]])
    
    prediction = int(model.predict(features)[0])                # convert to Python int
    probability = float(model.predict_proba(features)[0][1])    # convert to Python float
    
    return {
        "prediction": prediction,
        "probability": round(probability, 4)
    }

@app.get("/predict")
def predict_get(
    Pregnancies: int = Query(...),
    Glucose: float = Query(...),
    BloodPressure: float = Query(...),
    SkinThickness: float = Query(...),
    Insulin: float = Query(...),
    BMI: float = Query(...),
    DiabetesPedigreeFunction: float = Query(...),
    Age: int = Query(...)
):
    features = np.array([[ 
        Pregnancies,
        Glucose,
        BloodPressure,
        SkinThickness,
        Insulin,
        BMI,
        DiabetesPedigreeFunction,
        Age
    ]])
    
    prediction = int(model.predict(features)[0])              
    probability = float(model.predict_proba(features)[0][1])  
    
    return {
        "prediction": prediction,
        "probability": round(probability, 4)
    }
