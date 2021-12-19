import cv2 
import numpy as np 
import face_recognition

import os 
path = 'C:/Users/ROHIT SINGH/PycharmProjects/advance-attendence-system-/Saved Pictures'

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
  imgS = cv2.resize(img,(0,0),None,0.25,0.25)
  imgS = cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)
  facesCurrframe = face_recognition.face_locations(imgS)
  encodeCurrframe = face_recognition.face_encodings(imgS, facesCurrframe)



  for encodeface,faceLoc in zip(encodeCurrframe,facesCurrframe):
    matches = face_recognition.compare_faces(encodeListstudents,encodeface)
    faceDis = face_recognition.face_distance(encodeListstudents,encodeface)
    print(faceDis)
    matchIndex = np.argmin(faceDis)

    if matches[matchIndex]:
      Usn = classUsn[matchIndex]
      print(classUsn)
      y1,x2,y2,x1 = faceLoc
      y1, x2, y2, x1 =   y1*4 ,x2*4 ,y2*4,x1*4
      cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
      cv2.rectangle(img, (x1, y2-35), (x2, y2), (0, 255, 0), cv2.FILLED)
      cv2.putText(img,Usn,(x1+15,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)

  cv2.imshow('webcam',img)
  cv2.waitKey(1)
