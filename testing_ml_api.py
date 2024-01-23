import json
import requests

input_data = {
  "pregnancies": 2,
  "Glucose": 100,
  "BloodPressure": 120,
  "SkinThickness": 10,
  "Insulin": 100,
  "BMI": 25,
  "DiabetesPedigreeFunction": 0.352,
  "Age": 35
}

url = "http://diab-pred-check-api.centralindia.azurecontainer.io/diabetes_prediction"

json_object = json.dumps(input_data)

response = requests.post(url, data=json_object)

print(response.text)
