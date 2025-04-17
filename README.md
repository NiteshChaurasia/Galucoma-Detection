🩺 Glaucoma Detection with Deep Learning
This project utilizes a Convolutional Neural Network (CNN) to detect glaucoma from retinal fundus images. It features a Streamlit web application that allows users to upload fundus images, receive a diagnosis, and download a PDF report containing the results.

📁 Dataset
The model is trained on the REFUGE2 dataset, which is designed to evaluate and compare automated algorithms for glaucoma detection and optic disc/cup segmentation on a standard dataset.

The dataset includes:

High-resolution retinal fundus images.

Corresponding optic disc and cup segmentation masks.

Glaucoma diagnosis labels.

You can download the dataset from Kaggle: REFUGE2 Dataset

🚀 Features
Upload fundus images for glaucoma detection.

Receive immediate diagnosis results.

Download a PDF report containing patient information and diagnosis.

🛠️ Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/NiteshChaurasia/Galucoma-Detection.git
cd Galucoma-Detection
Install the required packages:

bash
Copy
Edit
pip install -r requirements.txt
Run the Streamlit app:

bash
Copy
Edit
streamlit run app.py
📄 PDF Report
After uploading an image and receiving a diagnosis, a PDF report is generated containing:

Patient's full name

Age

Date of birth

Diagnosis result

Date of report generation
