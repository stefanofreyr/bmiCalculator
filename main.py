import streamlit as st
import calculator

st.title("BMI Calculator")
st.subheader("A *very simple* tool to calculate your Body Mass Index (BMI)", divider="red")

imperial  = st.toggle("Imperial units")

if imperial:
    weight = st.text_input(label="Weight",placeholder="Your weight in pounds, e.g. 176")
    height = st.text_input(label="Height",placeholder="Your height in feet and inches separated by"
                                                      " a space, e.g. 5 11")
else:
    weight = st.text_input(label="Weight", placeholder="Your weight in kilograms, e.g. 80")
    height = st.text_input(label="Height", placeholder="Your height in meters, e.g. 1.80")

calculate = st.button(label="Calculate",icon=":material/calculate:",use_container_width=True)

if calculate:
    if not imperial:
        try:
            result = calculator.bmi(weight, height)
            st.text(f"Your BMI is {result}")
        except ValueError:
            st.error("Values provided are not valid")
    else:
        try:
            imp_height = height.split(" ")
            result = calculator.imp(float(weight), float(imp_height[0]), float(imp_height[1]))
            st.text(f"Your BMI is {result}")
        except ValueError:
            st.error("Values provided are not valid")
        except IndexError:
            st.error("Something's not quite right...")
