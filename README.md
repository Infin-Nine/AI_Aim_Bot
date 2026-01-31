# 🎯 AI Aim Bot

A real-time computer vision project that tracks the user's forehead and overlays a futuristic "Aim Lock" HUD (Heads-Up Display) using MediaPipe and OpenCV.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Face%20Mesh-orange)

## 📸 Preview

> *The system detects the forehead landmark (ID 151) and renders dynamic crosshairs and target circles in real-time.*

## 🚀 Features
- **Real-time Tracking:** High-speed face landmark detection using MediaPipe.
- **Dynamic HUD:** Crosshairs and target circles follow the user's movement.
- **Auto-Model Download:** Automatically fetches the required `.task` model on the first run.

## 🛠️ Installation

1. **Clone the Repository**
   ```bash
   git clone 
   cd 
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Usage

Simply run the main script:
```bash
python main.py
```
- The camera will open.
- The script will automatically download the required MediaPipe model if missing.
- Press **'q'** to exit the application.

## 🧠 How It Works
1. Captures video feed from the webcam.
2. Uses **MediaPipe Face Landmarker** to identify 478 face landmarks.
3. Extracts Landmark **#151** (center of the forehead).
4. Converts normalized coordinates to pixel coordinates.
5. Draws OpenCV primitives (lines, circles) anchored to that coordinate.

## 🤝 Contributing
Feel free to fork this repository and submit pull requests.

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).

