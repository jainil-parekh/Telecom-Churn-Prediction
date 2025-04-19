import streamlit as st
import pandas as pd
import joblib

# Load model and feature columns
model = joblib.load("models/telco_churn_model.pkl")
feature_cols = joblib.load("models/feature_columns.pkl")

st.title("📱 Telco Customer Churn Predictor")
st.markdown("Fill in the customer details to predict churn:")

# Sample inputs (you can add more based on actual features)
gender = st.selectbox("Gender", ["Male", "Female"])
SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
MonthlyCharges = st.slider("Monthly Charges", 0, 150, 70)
TotalCharges = st.slider("Total Charges", 0, 10000, 2000)
tenure = st.slider("Tenure (in months)", 0, 72, 12)

# Add all remaining inputs here (based on your full training feature set)

if st.button("Predict"):
    input_dict = {
        'gender': [1 if gender == "Male" else 0],
        'SeniorCitizen': [SeniorCitizen],
        'MonthlyCharges': [MonthlyCharges],
        'TotalCharges': [TotalCharges],
        'tenure': [tenure],
        # add other encoded features here as needed
    }

    input_df = pd.DataFrame(input_dict)

    # Align with trained model feature set
    input_df = input_df.reindex(columns=feature_cols, fill_value=0)

    prediction = model.predict(input_df)[0]
    result = "Churn" if prediction == 1 else "No Churn"
    st.success(f"Prediction: {result}")
