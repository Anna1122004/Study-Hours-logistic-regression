import streamlit as st
import joblib
model = joblib.load("studyhour.pkl")
st.title("Student Pass / Fail Prediction")
hours = st.number_input(
    "Enter study hours",
    min_value=0.0,
    max_value=15.0,
    value=5.0
)
attendance=st.number_input(
    "Enter attendance",
    min_value=0.0,
    max_value=100.0,
    value=50.0
)

if st.button("Predict"):
    prediction = model.predict([[hours,attendance]])
    probability = model.predict_proba([[hours,attendance]])
    pass_probability = probability[0][1] * 100
    fail_probability = probability[0][0] * 100
    if prediction[0] == 1:
        st.success("Student will PASS")
    else:
        st.error("Student will FAIL")
    st.write(f"**Pass Probability:** {pass_probability:.2f}%")
    st.write(f"**Fail Probability:** {fail_probability:.2f}%")
    st.progress(int(pass_probability))
