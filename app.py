import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("bankruptcy_model.pkl")

# App UI
st.set_page_config(page_title="Bankruptcy Predictor", layout="centered")
st.title("🔍 Bankruptcy Risk Prediction App")

st.markdown("Provide input values for the following features:")

# Input fields for all features
industrial_risk = st.selectbox("Industrial Risk", [0, 0.5, 1])
management_risk = st.selectbox("Management Risk", [0, 0.5, 1])
financial_flexibility = st.selectbox("Financial Flexibility", [0, 0.5, 1])
credibility = st.selectbox("Credibility", [0, 0.5, 1])
competitiveness = st.selectbox("Competitiveness", [0, 0.5, 1])
operating_risk = st.selectbox("Operating Risk", [0, 0.5, 1])

if st.button("Predict Bankruptcy Risk"):
    input_data = np.array([[industrial_risk, management_risk, financial_flexibility,
                            credibility, competitiveness, operating_risk]])
    
    prediction = model.predict(input_data)[0]
    
    if prediction == 1:
        st.error("⚠️ Prediction  class is : Bankruptcy")
    else:
        st.success("✅ Prediction  class is : Non- Bankruptcy ")
