import os
import cv2
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)
newname=input("enter folder name")
bb="trainingImages/"
folder_name=bb+newname
createFolder(folder_name)
folderpath = os.path.abspath(folder_name)
a = folderpath
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_id = input("Enter the object name")
direct = face_id
path = os.path.join(a,direct)
cap=cv2.VideoCapture(0)
count = 0
while True:
    ret,test_img=cap.read()
    if not ret :
        continue
        cv2.imwrite(path+"%d.jpg" % count, test_img) # save frame as JPG file
        count += 1
        resized_img = cv2.resize(test_img, (1000, 700))
        cv2.imshow('face detection Tutorial ',resized_img)
        k = cv2.waitKey(100) & 0xff
        if k == 27:
            break
        elif count >= 30:
            break
        cap.release()
        cv2.destroyAllWindows
