import cv2
import mediapipe as mp
import os
import urllib.request
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# ================= CONFIGURATION =================
MODEL_DIR = "models"
MODEL_NAME = "face_landmarker.task"
MODEL_PATH = os.path.join(MODEL_DIR, MODEL_NAME)
MODEL_URL = "https://storage.googleapis.com/mediapipe-models/face_landmarker/face_landmarker/float16/1/face_landmarker.task"

AIM_ID = 151  # Forehead point

# Colors
GREEN = (0,255,0)
RED = (0, 0, 255)
BLACK = (0, 0, 0)

# ================= SETUP UTILS =================
def download_model():
    """Downloads the model file if it doesn't exist."""
    if not os.path.exists(MODEL_DIR):
        os.makedirs(MODEL_DIR)
    if not os.path.exists(MODEL_PATH):
        print(f"Downloading {MODEL_NAME}...")
        urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)
        print("Download complete.")

# Ensure model exists
download_model()

# ================= MEDIAPIPE SETUP =================
base_options = python.BaseOptions(model_asset_path=MODEL_PATH)
options = vision.FaceLandmarkerOptions(
    base_options=base_options,
    running_mode=vision.RunningMode.IMAGE,
    num_faces=1
)
face_landmarker = vision.FaceLandmarker.create_from_options(options)

# ================= MAIN LOOP =================
cap = cv2.VideoCapture(0)

print("Starting Camera... Press 'q' to exit.")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # Flip frame specifically for selfie-view (mirror effect)
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    # Convert to RGB for MediaPipe
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)

    # Detection
    result = face_landmarker.detect(mp_image)

    if result.face_landmarks:
        lm = result.face_landmarks[0][AIM_ID]
        cx, cy = int(lm.x * w), int(lm.y * h)

        # --- DRAW HUD ELEMENTS ---
        # 1. Full Crosshair
        cv2.line(frame, (0, cy), (w, cy), BLACK, 1)
        cv2.line(frame, (cx, 0), (cx, h), BLACK, 1)

        # 2. Concentric Circles (The "Aim" effect)
        cv2.circle(frame, (cx, cy), 30, BLACK, 1)
        cv2.circle(frame, (cx, cy), 22, BLACK, 1)
        cv2.circle(frame, (cx, cy), 15, BLACK, 1)
        
        # 3. Center Dot (Locked Target)
        cv2.circle(frame, (cx, cy), 4, RED, -1)

        # 4. Text Info
        cv2.putText(frame, "TARGET LOCKED", (cx + 40, cy - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, RED, 2)
        cv2.putText(frame, f"X:{cx} Y:{cy}", (20, 40), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, GREEN, 2)

    cv2.imshow("Forehead Aim HUD", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
