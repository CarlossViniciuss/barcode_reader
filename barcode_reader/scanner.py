import cv2
import mediapipe as mp

from pyzbar import pyzbar

def detectar_gestos(frame):
    # Lógica de detecção de gestos aqui
    pass

def init_scanner():

    cap = cv2.VideoCapture(0)
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        detectar_gestos(frame)
        barcodes = pyzbar.decode(frame)

        for barcode in barcodes:
            (x, y, w, h) = barcode.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            barcode_value = barcode.data.decode("utf-8")
            cv2.putText(frame, barcode_value, (x, y -10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)


        cv2.imshow("Barcode Scanner", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()