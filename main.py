import joblib
import streamlit as st

st.title("🏠 Home Price Prediction")

# Load trained model
model = joblib.load("model.pkl")

# User inputs
area = st.number_input("Area (sq ft)", value=1000)
bedrooms = st.number_input("Number of Bedrooms", value=2, step=1)
age = st.number_input("Age of House (years)", value=10)

if st.button("Predict"):
    # Create input DataFrame (VERY IMPORTANT)
    input_data = pd.DataFrame(
        [[area, bedrooms, age]],
        columns=["area", "bedrooms", "age"]
    )

    prediction = model.predict(input_data)

    st.success(f"Estimated House Price: ₹ {prediction[0]:,.2f}")
