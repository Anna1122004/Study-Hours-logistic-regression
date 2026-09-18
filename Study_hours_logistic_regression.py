
import gradio as gr
import joblib

model = joblib.load("studyhour.pkl")


def predict(hours, attendance):

    prediction = model.predict([[hours, attendance]])

    probability = model.predict_proba([[hours, attendance]])

    pass_probability = probability[0][1] * 100
    fail_probability = probability[0][0] * 100

    if prediction[0] == 1:
        result = "Student will PASS"
    else:
        result = "Student will FAIL"

    return (
        result,
        f"Pass Probability: {pass_probability:.2f}%",
        f"Fail Probability: {fail_probability:.2f}%"
    )


app = gr.Interface(
    fn=predict,
    inputs=[
        gr.Number(label="Study Hours", minimum=0, maximum=15, value=5),
        gr.Number(label="Attendance", minimum=0, maximum=100, value=50)
    ],
    outputs=[
        gr.Textbox(label="Prediction"),
        gr.Textbox(label="Pass Probability"),
        gr.Textbox(label="Fail Probability")
    ],
    title="Student Pass / Fail Prediction",
    description="Enter study hours and attendance to predict the student's result."
)

app.launch(
    server_name="0.0.0.0",
    server_port=7860
)
