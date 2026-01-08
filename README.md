# Requirements
Functional Requirements
- Upload image
- Detect number plate(s)
- Extract text from plates
- Display bounding boxes + text

# Directory Structure
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
│   ├── predict.py              # inference
│   ├── training.ipynb          # Training notebook
│
├── models/
│   ├── plate_detector.pt       # YOLO model
│
├── data/
│
├── requirements.txt
├── README.md
└── .gitignore

```