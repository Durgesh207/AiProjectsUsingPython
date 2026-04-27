from facial_emotion_recognition import EmotionRecognition
import cv2

er = EmotionRecognition(device="cpu")

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    if not ret:
        break

    frame = er.recognise_emotion(frame, return_type='BGR')

    cv2.imshow("Emotion Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()