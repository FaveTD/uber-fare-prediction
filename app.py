import streamlit as st
import pickle
import numpy as np

# Loading trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)
st.set_page_config(page_title="Uber Fare Prediction", layout="centered")
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>Uber Fare Prediction App</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Enter ride details below to predict the fare.</p>", unsafe_allow_html=True)
st.write("---")
col1, col2 = st.columns(2)

with col1:
    pickup_longitude = st.slider("Pickup Longitude", -74.1, -73.7, -73.93)
    pickup_latitude = st.slider("Pickup Latitude", 40.6, 40.9, 40.73)
    passenger_count = st.slider("Number of Passengers", 1, 6, 1)
    pickup_hour = st.slider("Pickup Hour (0-23)", 0, 23, 16)

with col2:
    dropoff_longitude = st.slider("Dropoff Longitude", -74.1, -73.7, -73.98)
    dropoff_latitude = st.slider("Dropoff Latitude", 40.6, 40.9, 40.72)
    pickup_day = st.slider("Day of the Week (1=Monday, 7=Sunday)", 1, 7, 3)

if st.button("Predict Fare"):
    features = np.array([[pickup_longitude, pickup_latitude,
                          dropoff_longitude, dropoff_latitude,
                          passenger_count, pickup_hour, pickup_day]])
    fare = model.predict(features)
    st.success(f"💰 Estimated Uber Fare: ${fare[0]:.2f}")
