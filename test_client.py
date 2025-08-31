import requests

# Base URL of your FastAPI server
BASE_URL = "http://127.0.0.1:8000"

# Test data (matches your model features)
test_input = {
  "Pregnancies": 2,
  "Glucose": 120,
  "BloodPressure": 70,
  "SkinThickness": 25,
  "Insulin": 80,
  "BMI": 28.5,
  "DiabetesPedigreeFunction": 0.45,
  "Age": 35
}

# ----------------------------
# 1️⃣ Test POST /predict
# ----------------------------
response_post = requests.post(f"{BASE_URL}/predict", json=test_input)

if response_post.status_code == 200:
    print("POST /predict response:")
    print(response_post.json())
else:
    print("POST /predict failed:", response_post.status_code, response_post.text)

# ----------------------------
# 2️⃣ Test GET /predict (query params)
# ----------------------------
response_get = requests.get(f"{BASE_URL}/predict", params=test_input)

if response_get.status_code == 200:
    print("\nGET /predict response:")
    print(response_get.json())
else:
    print("GET /predict failed:", response_get.status_code, response_get.text)
