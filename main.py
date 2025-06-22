import streamlit as st
from ultralytics import YOLO
import gdown
import numpy as np
from PIL import Image

# Baixar o modelo se não existir
import os
if not os.path.exists('model/best.pt'):
    gdown.download(id='1PmHc25ne_8U5Buoi5bvyq9G1K2jsAadz', output='model/best.pt', quiet=False)
model = YOLO('model/best.pt')

def detect_objects(image):
    results = model(image)
    annotated_image = results[0].plot()
    return annotated_image

st.title('PCB Board Defect Detection')
st.write('Upload an image to detect the defects on a PCB board')

uploaded_file = st.file_uploader('Upload a photo', type=['jpg', 'jpeg', 'png'])
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    image_np = np.array(image)
    result_img = detect_objects(image_np)
    st.image(result_img, caption='PCB board defect detected', use_column_width=True)