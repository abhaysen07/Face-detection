import cv2
import os
import numpy as np
#This module contains all common functions that are called in tester.py file
#Given an image below function returns rectangle for face detected alongwith
gray scale image
def faceDetection(test_img):
    gray_img=cv2.cvtColor(test_img,cv2.COLOR_BGR2GRAY)#convert color image to grayscale 
    face_haar_cascade=cv2.CascadeClassifier('C:/Users/Dinesh/PycharmProjects/FaceRecognitionmaster/HaarCascade/haarcascade_frontalface_default.xml')#Load haarclassifier
    faces=face_haar_cascade.detectMultiScale(gray_img, scaleFactor=1.32, minNeighbors=5)#detectMultiScale returns rectangles
    return faces,gray_img
#Given a directory below function returns part of gray_img which is face alongwith its label/ID
def labels_for_training_data(directory):
    faces=[]
    faceID=[]
    for path,subdirnames,filenames in os.walk(directory):
        for filename in filenames:
            if filename.startswith("."):
                print("Skipping system file")#Skipping files that startwith(.)
                continue
            id=os.path.basename(path)#fetching subdirectory names
            img_path=os.path.join(path,filename)#fetching image path
            print("img_path:",img_path)
            print("id:",id)
            test_img=cv2.imread(img_path)#loading each image one by one
            if test_img is None:
                print("Image not loaded properly")
                continue
            faces_rect,gray_img=faceDetection(test_img)#Calling faceDetection function to return faces detected in particular image
            if len(faces_rect)!=1:
                continue #Since we are assuming only single person images are being fed to classifier
