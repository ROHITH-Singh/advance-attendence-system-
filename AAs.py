import cv2 
import numpy as np 
import face_recognition

import os 
path = '/home/rohitsingh/advance-attendence-system-/Saved Pictures'

images = []
classUsn = []
mylist = os.listdir(path)
print(mylist)

for cls in mylist:
  currImg = cv2.imread(f'{path}/{cls}')
  images.append(currImg)
  classUsn.append(os.path.splitext(cls)[0])
print(classUsn)

def encodings(images):
  encodeList = []
  for img in images:
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    encode = face_recognition.face_encodings(img)[0]
    encodeList.append(encode)
  return encodeList

encodeListstudents = encodings(images)
print(len(encodeListstudents),'encodings complete')

cap = cv2.VideoCapture(0)

while True:
  success,img = cap.read()
  imgsize = cv2.resize(img,(0,0),None,0.25,0.25)
  imgsize = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
 
  facesCurr = face_recognition.face_locations(imgsize)[0]
  encode = face_recognition.face_encodings(imgsize,facesCurr)[0]

  for encodeface,faceLoc in zip(encode,facesCurr):
    matches = face_recognition.compare_faces(encodeListstudents,encodeface)
    faceDis = face_recognition.face_distance(encodeListstudents,encodeface)
    print(faceDis)