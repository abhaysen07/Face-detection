import PIL
import numpy as np
# pip install cv2
import cv2
#make 3 variables and load with CascadeClassifier files
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
# to capture video from Webcam
cap = cv2.VideoCapture(0)
#open in While loop for the repeated program running
while(cap.isOpened()):
    #to get ret and frame from the Webcam.
    ret, frame = cap.read()
    #load in the grey scale to get the color difference from the file
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #detect multiscale from the webcanm top get the proper detection of faces using the parameters.
    faces = face_cascade.detectMultiScale(frame, 1.3, 5)
    for (x, y, w, h) in faces:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        faces_detected = format(len(faces)) + " faces detected!"
        print(faces_detected)
        cv2.imshow('VIDEO',frame)
        cv2.imwrite('face.jpg',roi_gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
