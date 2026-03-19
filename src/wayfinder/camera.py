import cv2

def init_camera(index=0):
    cap = cv2.VideoCapture(index, cv2.CAP_V4L2)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    if not cap.isOpened():
        raise RuntimeError("Could not open camera")

    return cap

def get_frame(cap):
    ret, frame = cap.read()
    if not ret:
        return None
    return frame