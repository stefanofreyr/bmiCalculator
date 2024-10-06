import streamlit as st

st.title("BMI Calculator")
st.subheader("A *very simple* tool to calculate your Body Mass Index (BMI)")

weight = st.text_input(label="Weight",placeholder="Your weight in kilograms")
height = st.text_input(label="Height",placeholder="Your height in meters")


calculate = st.button(label="Calculate",icon=":material/calculate:",use_container_width=True)

if calculate:
    result  = round(float(weight) / float(height)**2, 2)
    st.text(f"Your BMI is {result}")