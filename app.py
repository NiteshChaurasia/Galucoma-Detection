# app.py

import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
from fpdf import FPDF
import datetime

# Load model
model = tf.keras.models.load_model("glaucoma_classifier_model.h5")

def predict_glaucoma(img):
    img = img.resize((224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    prediction = model.predict(img_array)
    return prediction

st.title("🩺 Glaucoma Detection & PDF Report")

# Collect Patient Info
name = st.text_input("👤 Full Name")
age = st.number_input("🎂 Age", min_value=1, max_value=120, value=30)
dob = st.date_input("📅 Date of Birth")

uploaded_file = st.file_uploader("📤 Upload Fundus Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None and name and age and dob:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_column_width=True)

    result = predict_glaucoma(img)
    predicted_class = np.argmax(result)
    diagnosis = "Glaucoma Detected" if predicted_class == 0 else "No Glaucoma Detected"
    st.success("✅ Prediction Completed")

    st.write(f"**Diagnosis:** {diagnosis}")

    # Generate PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Glaucoma Detection Report", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Name: {name}", ln=True)
    pdf.cell(200, 10, txt=f"Age: {age}", ln=True)
    pdf.cell(200, 10, txt=f"Date of Birth: {dob}", ln=True)
    pdf.cell(200, 10, txt=f"Diagnosis: {diagnosis}", ln=True)
    pdf.cell(200, 10, txt=f"Date of Report: {datetime.date.today()}", ln=True)
    pdf.output("glaucoma_report.pdf")

    with open("glaucoma_report.pdf", "rb") as file:
        st.download_button("📄 Download PDF", file, file_name=f"{name}_report.pdf", mime="application/pdf")
else:
    st.info("Please fill all details and upload an image.")
