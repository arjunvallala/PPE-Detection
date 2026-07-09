# 🦺 PPE Detection using YOLOv8

A real-time **Personal Protective Equipment (PPE) Detection** system built using **YOLOv8** and **OpenCV**. The model is fine-tuned on a custom construction site safety dataset to detect workers and identify whether they are wearing the required safety equipment.

## Features

- Real-time webcam detection
- Fine-tuned YOLOv8 model
- Detects 10 custom classes
- Color-coded bounding boxes
  - 🟢 Green – Required PPE detected
  - 🔴 Red – Missing PPE
  - 🔵 Blue – Other objects
- Displays confidence score for every detection

## Classes Detected

- Hardhat
- Mask
- NO-Hardhat
- NO-Mask
- NO-Safety Vest
- Person
- Safety Cone
- Safety Vest
- Machinery
- Vehicle

## Tech Stack

- Python
- OpenCV
- Ultralytics YOLOv8
- PyTorch

## Project Structure

```
PPE-Detection/
│── app.py
│── best1.pt
│── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/PPE-Detection.git
cd PPE-Detection
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Requirements

```
ultralytics
opencv-python
```

Or install manually:

```bash
pip install ultralytics opencv-python
```

## Usage

Run the application:

```bash
python app.py
```

Press **Q** to exit the webcam window.

## Model Training

The detection model was fine-tuned using **YOLOv8** on a custom PPE construction safety dataset.

Training command:

```bash
yolo task=detect mode=train model=yolov8l.pt data=data.yaml epochs=10 imgsz=320
```

## Future Improvements

- Person-wise PPE compliance checking
- Alarm for safety violations
- Video file support
- Object tracking using ByteTrack
- Performance optimization for CPU

## License

This project is licensed under the MIT License.
