from wayfinder.camera import init_camera, get_frame
from wayfinder.detector import detect
from wayfinder.logic import decide
from wayfinder.audio import speak
import cv2

def main():
    cap = init_camera()
    print("Wayfinder running...")

    while True:
        frame = get_frame(cap)
        if frame is None:
            break

        detections = detect(frame)
        message = decide(detections)

        if message:
            speak(message)

        cv2.imshow("Wayfinder", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()