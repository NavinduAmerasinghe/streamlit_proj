import streamlit as st

st.set_page_config(
    page_title="BMI Calculator",
    page_icon="⚖️",
    layout="centered"
)

st.title("⚖️ BMI Calculator")
st.write("Calculate your **Body Mass Index (BMI)** and understand your health category.")

# --- Unit selection ---
unit = st.radio("Select unit system:", ["Metric (kg, cm)", "Imperial (lb, ft/in)"])

# --- Input fields ---
if unit == "Metric (kg, cm)":
    weight = st.number_input("Weight (kg)", min_value=1.0, value=70.0)
    height_cm = st.number_input("Height (cm)", min_value=50.0, value=170.0)
    height_m = height_cm / 100

else:
    weight_lb = st.number_input("Weight (lb)", min_value=1.0, value=154.0)
    feet = st.number_input("Height (feet)", min_value=1, value=5)
    inches = st.number_input("Height (inches)", min_value=0, value=7)
    weight = weight_lb * 0.453592
    height_m = (feet * 12 + inches) * 0.0254

# --- BMI Calculation ---
if st.button("Calculate BMI", type="primary"):
    bmi = weight / (height_m ** 2)

    st.subheader(f"📊 Your BMI: **{bmi:.2f}**")

    # --- BMI Categories ---
    if bmi < 18.5:
        st.warning("Underweight 🟡")
        category = "Underweight"
    elif 18.5 <= bmi < 25:
        st.success("Normal weight 🟢")
        category = "Normal weight"
    elif 25 <= bmi < 30:
        st.warning("Overweight 🟠")
        category = "Overweight"
    else:
        st.error("Obese 🔴")
        category = "Obese"

    # --- Ideal Weight Range ---
    min_weight = 18.5 * (height_m ** 2)
    max_weight = 24.9 * (height_m ** 2)

    st.markdown(
        f"""
        **Category:** {category}  
        **Healthy weight range:** {min_weight:.1f} kg – {max_weight:.1f} kg
        """
    )

    st.info(
        "BMI is a general health indicator and does not account for muscle mass, age, or gender."
    )

st.caption("Built with Streamlit • WHO BMI classification")
