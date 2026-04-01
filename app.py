import streamlit as st

st.title("Disease Prediction System")

age = st.number_input("Enter Age", 1, 100)
bp = st.number_input("Enter Blood Pressure", 80, 200)

if st.button("Predict"):
    if age > 40 and bp > 140:
        st.error("High Risk of Disease")
    else:
        st.success("Low Risk of Disease")
