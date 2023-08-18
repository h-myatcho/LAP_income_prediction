import streamlit as st
import joblib

# Load the income prediction model
Income_Model = joblib.load("income_model.pkl")

st.title('Income Prediction')

name = st.text_input('Enter your name', '')

if name:
    st.success("Please provide your age and years of experience for income prediction.")
    
    age = st.number_input('Enter your age', min_value=0, max_value=100, value=25, step=1)
    experience = st.number_input('Enter years of experience', min_value=0, max_value=50, value=5, step=1)
    
    data = [age, experience]
    
    result = Income_Model.predict([data])
    
    button_clicked = st.button("Predict")
    if button_clicked:
        predicted_income = result[0]
        st.success(f"Based on the available data, {name}, your predicted income is: ${predicted_income:.2f}")
