from flask import Flask, request, jsonify, render_template
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
from src.pipeline.predict_pipe import PredictPipeline, CustomData

app = Flask(__name__)

# Home route to render the HTML form

crops = [  "Rice",
    "Maize",
    "Moong",
    "Urad",
    "Groundnut",
    "Sesamum",
    "Potato",
    "Sugarcane",
    "Wheat",
    "Rapeseed & Mustard",
    "Bajra",
    "Jowar",
    "Arhar/Tur",
    "Ragi",
    "Gram",
    "Small millets",
    "Cotton(lint)",
    "Onion",
    "Sunflower",
    "Dry chillies",
    "Horse-gram",
    "Peas & beans (Pulses)",
    "Tobacco",
    "Soyabean",
    "Turmeric",
    "Masoor",
    "Ginger",
    "Linseed",
    "Castor seed",
    "Barley",
    "Sweet potato",
    "Garlic",
    "Banana",
    "Mesta",
    "Tapioca",
    "Coriander",
    "Niger seed",
    "Jute",
    "Coconut",
    "Safflower",
    "Arecanut",
    "Sannhamp",
    "Cashewnut",
    "Cowpea(Lobia)",
    "Black pepper",
    "Moth",
    "Khesari",
    "Cardamom",
    "Guar seed"]  
seasons = ["Kharif", "Rabi", "Whole Year","Summer","Autumn","Winter"]  # Add more seasons as necessary
states = ["Karnataka",
    "Andhra Pradesh",
    "West Bengal",
    "Chhattisgarh",
    "Bihar",
    "Madhya Pradesh",
    "Uttar Pradesh",
    "Tamil Nadu",
    "Gujarat",
    "Maharashtra",
    "Uttarakhand",
    "Odisha",
    "Assam",
    "Nagaland",
    "Puducherry",
    "Meghalaya",
    "Haryana",
    "Jammu and Kashmir",
    "Himachal Pradesh",
    "Kerala",
    "Manipur",
    "Tripura",
    "Mizoram",
    "Telangana",
    "Punjab",
    "Arunachal Pradesh",
    "Jharkhand",
    "Goa",
    "Sikkim",
    "Delhi"] 
@app.route('/')
def home():
    return render_template('index.html', crops=crops, seasons=seasons, states=states)

# Predict route to handle form submission and return the prediction result
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.form
        custom_data = CustomData(
            crop=data['crop'],
            season=data['season'], 
            state=data['state'],
            area=int(data['area']),
            production=int(data['production']),
            rainfall=int(data['rainfall']),
            fertilizer=int(data['fertilizer']),
            pesticide=int(data['pesticide'])
        )
        
        features = custom_data.get_data_as_frame()
        predict_pipeline = PredictPipeline()
        prediction = predict_pipeline.predict(features)
        
        return render_template('index.html', prediction_text=f'Predicted Yield: {round(prediction[0],2)}', crops=crops, seasons=seasons, states=states)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
