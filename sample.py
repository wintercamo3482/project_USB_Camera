import cv2

# Open camera port
cap = cv2.VideoCapture("/dev/video0")

# Check if the camera opened
if not cap.isOpened():
        print("[ERROR] Fail to open camera device")
        exit()

# Set the resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if not ret:
        print("[ERROR] Fail to read frame")
        break
    
    cv2.imshow('USB Camera Sample', frame)

    # Press 'Q' to quit
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()