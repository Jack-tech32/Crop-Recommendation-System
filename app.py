import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Crop Recommendation", page_icon="🌱")

st.title("Crop Recommendation System")

# Load saved model and label encoder
model =joblib.load('rf_crop_model.pkl')
le = joblib.load('label_encoder.pkl')

# Input fields
def user_input_features():
    N = st.number_input('Nitrogen (N)', min_value=0, max_value=140, value=90)
    P = st.number_input('Phosphorus (P)', min_value=0, max_value=140, value=40)
    K = st.number_input('Potassium (K)', min_value=0, max_value=205, value=40)
    temperature = st.slider('Temperature (°C)', 0.0, 50.0, 25.0)
    humidity = st.slider('Humidity (%)', 0.0, 100.0, 80.0)
    ph = st.slider('pH value', 0.0, 14.0, 6.5)
    rainfall = st.slider('Rainfall (mm)', 0.0, 400.0, 100.0)

    data = {
        'N': N, 'P': P, 'K': K,
        'temperature': temperature, 'humidity': humidity,
        'ph': ph, 'rainfall': rainfall
    }

    return pd.DataFrame([data])

input_df = user_input_features()

# Predict on button click
if st.button("Predict Crop"):
    prediction = model.predict(input_df)
    crop_name = le.inverse_transform(prediction)[0]
    st.success(f"✅ Recommended Crop: **{crop_name}**")
