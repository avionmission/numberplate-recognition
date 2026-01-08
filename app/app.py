import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
import cv2
import tempfile
import os

# Config
st.set_page_title(
    page_title="License Plate Character Detection",
    layout="centered"
)

st.title("License Plate Character Detection")
st.write("Upload an image to detect characters")

# Load Model
def load_model():
    return YOLO("models/model.pt")

model = load_model()

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
        image.save(tmp.name)
        temp_image_path = tmp.name
    
    # Inference
    with st.spinner("Running inference..."):
        results = model(
            temp_image_path,
            device="cpu",
            imgsz=640,
            conf=0.25
        )

    # Visualise Results
    annotated_img = results[0].plot()
    annotated_img = cv2.cvtColor(annotated_img, cv2.COLOR_BGR2RGB)

    st.subheader("Detection Result")
    st.image(annotated_img, use_container_width=True)

    # Detection Table
    boxes = results[0].boxes

    if boxes is not None and len(boxes) > 0:
        st.subheader("Detected Characters")
    
        data= []
        names= results[0].names

        for box in boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            label = names[cls_id]
        
            data.append({
                "Character": label,
                "Confidence": round(conf, 3)
            })
        
        st.table(data)
    else:
        st.warning("No characters detected")
    
    os.remove(temp_image_path)
        
