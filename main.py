import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression

st.title("🏠 Home Price Prediction")

# --- Train model inside the app (no joblib file needed) ---
data = {
    "area": [1000, 1500, 2000, 2500, 3000],
    "bedrooms": [2, 3, 3, 4, 4],
    "age": [10, 15, 20, 5, 8],
    "price": [100000, 150000, 200000, 250000, 270000],
}
df = pd.DataFrame(data)

X = df[["area", "bedrooms", "age"]]
y = df["price"]

model = LinearRegression()
model.fit(X, y)

# --- Inputs ---
area = st.number_input("Area (sq ft)", value=1000.0)
bedrooms = st.number_input("Number of Bedrooms", value=2, step=1)
age = st.number_input("Age of House (years)", value=10.0)

if st.button("Predict"):
    input_data = pd.DataFrame([[area, bedrooms, age]], columns=["area", "bedrooms", "age"])
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated House Price: ₹ {prediction:,.2f}")
