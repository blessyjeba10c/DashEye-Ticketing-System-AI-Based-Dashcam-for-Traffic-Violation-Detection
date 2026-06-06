import cv2
import numpy as np
import time
import random
from geopy.distance import geodesic

# =========================
# GPS + SPEED
# =========================
prev_coord = None
prev_time = None

def get_gps():
    lat = 13.0827 + random.uniform(-0.0005, 0.0005)
    lon = 80.2707 + random.uniform(-0.0005, 0.0005)
    return (lat, lon)

def calculate_speed(coord):
    global prev_coord, prev_time

    if prev_coord is None:
        prev_coord = coord
        prev_time = time.time()
        return 0

    curr_time = time.time()
    dist = geodesic(prev_coord, coord).meters
    speed = dist / (curr_time - prev_time)

    prev_coord = coord
    prev_time = curr_time

    return speed * 3.6


# =========================
# RED LIGHT DETECTION
# =========================
def detect_red(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red1 = np.array([0,120,70])
    upper_red1 = np.array([10,255,255])
    lower_red2 = np.array([170,120,70])
    upper_red2 = np.array([180,255,255])

    mask = cv2.inRange(hsv, lower_red1, upper_red1) + \
           cv2.inRange(hsv, lower_red2, upper_red2)

    red_pixels = cv2.countNonZero(mask)

    return red_pixels > 500


# =========================
# VEHICLE DETECTION (FIXED)
# =========================
def detect_motion(prev_frame, curr_frame):

    if prev_frame is None or curr_frame is None:
        return []

    # Ensure same size
    curr_frame = cv2.resize(curr_frame, (900, 500))
    prev_frame = cv2.resize(prev_frame, (900, 500))

    gray1 = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(curr_frame, cv2.COLOR_BGR2GRAY)

    diff = cv2.absdiff(gray1, gray2)

    _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    vehicles = []
    for cnt in contours:
        if cv2.contourArea(cnt) > 1500:
            x,y,w,h = cv2.boundingRect(cnt)
            vehicles.append((x,y,w,h))

    return vehicles


# =========================
# SAVE + SEND
# =========================
def save_and_send(frame, coord):
    filename = f"violation_{int(time.time())}.jpg"
    cv2.imwrite(filename, frame)

    print("🚨 VIOLATION DETECTED")
    print(f"Saved: {filename}")
    print(f"Location: {coord}")
    print("📡 Sending to Police Server...")
    print("✅ Ticket Issed\n")


# =========================
# MAIN SYSTEM
# =========================
cap = cv2.VideoCapture("car.mp4")

if not cap.isOpened():
    print("Error opening video")
    exit()

ret, prev_frame = cap.read()

if not ret:
    print("Error reading first frame")
    exit()

prev_frame = cv2.resize(prev_frame, (900, 500))  # FIX HERE

STOP_LINE_Y = 300

while True:
    ret, frame = cap.read()

    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    frame = cv2.resize(frame, (900, 500))

    coord = get_gps()
    speed = calculate_speed(coord)

    red = detect_red(frame)

    vehicles = detect_motion(prev_frame, frame)

    # Draw stop line
    cv2.line(frame, (0, STOP_LINE_Y), (900, STOP_LINE_Y), (0,255,255), 2)
    cv2.putText(frame, "STOP LINE", (10, STOP_LINE_Y-10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,255), 2)

    violation = False

    for (x,y,w,h) in vehicles:
        center_y = y + h//2

        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

        if red and center_y > STOP_LINE_Y:
            violation = True
            cv2.putText(frame, "VIOLATION", (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)

    if violation:
        save_and_send(frame, coord)

    # Info display
    cv2.putText(frame, f"Speed: {round(speed,2)} km/h", (20,40),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

    cv2.putText(frame, f"Signal: {'RED' if red else 'NONE'}", (20,80),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)

    cv2.imshow("AI Violation System", frame)

    prev_frame = frame.copy()

    if cv2.waitKey(30) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()