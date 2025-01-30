import cv2 as cv
import numpy as np

# Captura de vídeo (frame por frame), 0 para indicar a webcam a ser utilizada.
cap = cv.VideoCapture(0)

# Se há algum problema com a câmera, cap.isOpened() retornará False.
if not cap.isOpened():
    print("Cannot open camera")
    exit()

# Loop de captura de frame.
while True:
    # Captura o frame atual, ret é uma flag para sinalizar se o frame atual está sendo capturado.
    ret, frame = cap.read()

    if not ret:
        print("Has a problem with the frame. Finished.")
        break

    # Conversão do frame para escala de cinza para realizar a detecção facial.
    frame_gray =  cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Instanciação do classificador cascade para faces.
    facial_detector = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

    detections = facial_detector.detectMultiScale(frame_gray, scaleFactor=1.05, minSize=(100,100))

    # Retângulo de detecção em tempo real, ou seja, para cada face encontrada nas detecções.
    for (x,y,w,h) in detections:
        cv.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)
    
    cv.imshow('Frame', frame)

    # Se a tecla 'q' for pressionada, o loop será interrompido.
    if cv.waitKey(1) & 0xFF == ord('q'):
        break


# Liberar a memória.
cap.release()
cv.destroyAllWindows()

