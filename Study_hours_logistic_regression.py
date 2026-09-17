import streamlit as st
import joblib
model=joblib.load("student_result_prediction.pkl")
st.title("Student Pass / Fail based on Study Hours")
hours=st.number_input("Enter study hours",min_value=0.0,max_value=15.0,value=5.0)
if st.button("Predict "):
   prediction=model.predict([[hours]])
