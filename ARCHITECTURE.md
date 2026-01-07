# Requirements
Functional Requirements
- Upload image
- Detect number plate(s)
- Extract text from plates
- Display bounding boxes + text

Non-Functional Requirements
- Inference < 2s per image
- Works offline
- Supports Indian plates

Out of Scope
- Video processing
- Multi-camera feeds
- Cloud deployment

# Project structure plan
```
number-plate-recognition/
│
├── app/
│   ├── streamlit_app.py        # Streamlit UI
│   ├── components/
│   │   ├── uploader.py         # Image/video upload UI
│   │   ├── results.py          # Display bounding boxes & text
│
├── core/
│   ├── detector.py             # Plate detection logic (YOLO / OpenCV)
│   ├── recognizer.py           # OCR (Tesseract / EasyOCR)
│   ├── pipeline.py             # End-to-end flow
│
├── models/
│   ├── plate_detector.pt       # YOLO model
│
├── utils/
│   ├── image.py                # Image preprocessing
│   ├── draw.py                 # Bounding boxes
│   └── config.py               # Constants
│
├── data/
│   ├── samples/
│   └── outputs/
│
├── notebooks/
│   └── experiments.ipynb
│
├── requirements.txt
├── README.md
|── ARCHITECTURE.md             <-------- you are here
└── .gitignore

```