import cv2
import numpy as np
import face_recognition as fr
import os
from datetime import datetime

# Path to the folder of images of all students
studentListPath = r"C:\Users\User\Python Works\AI Attandance System\data" 

#empty list to keep the images in a list
studentImages = []

# An empty list to keep the name of the students from the images
studentNames = []

listOfStudentImages = os.listdir(studentListPath)

#print(listOfStudentImages)

# Getting the names of all the students
for std in listOfStudentImages:
    currentImg = cv2.imread(os.path.join(studentListPath, std))
    studentImages.append(currentImg)
    studentNames.append(os.path.splitext(std)[0])
    
#print(studentNames)
    

def findEncodings(images):
    encodeList = []
    for img in studentImages:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = fr.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def markAttendance(name):
    with open("attendance.csv", "r+") as f:
        myDataList = f.readlines()
        print(myDataList)


encodeListForKnownImgs = findEncodings(studentImages)

print('Encoding Complete')

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgs = cv2.resize(img, (0,0), None, 0.25, 0.25)
    imgs = cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB)
    
    facesInCurrentFrame = fr.face_encodings(imgs)[0]
    encodesCurFrames = fr.face_encodings(imgs, facesInCurrentFrame)
    
    for encodedFace, faceLoc in zip(encodesCurFrames, facesInCurrentFrame):
        matches = fr.compare_faces(encodeListForKnownImgs, encodedFace)
        faceDist = fr.face_distance(encodeListForKnownImgs, encodedFace)
        matchIndex = np.argmin(faceDist)
        
        if matches[matchIndex]:
            name = studentNames[matchIndex].upper()
            #print(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 2)
            cv2.rectangle(img, (x1, y2-35), (x2, y2), (0, 255, 0), cv2.FILLED())    
            cv2.putText(img, name,(x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX(), 1, (255, 255, 255), 2)
            
            
    cv2.imshow('Webcam', img)
    cv2.waitKey(1)