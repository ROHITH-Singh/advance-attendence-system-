import cv2 
import numpy as np 
import face_recognition
import pandas as pd
from datetime import date
import calendar
from datetime import datetime
import pytz
import datetime
import os 
path = 'C:/Users/ROHIT SINGH/PycharmProjects/advance-attendence-system-/Saved Pictures'

images = []
classUsn = []
mylist = os.listdir(path)
print(mylist)

tz_IN = pytz.timezone('Asia/Kolkata')
datetime_IN = datetime.datetime.now(tz_IN)
print("Current time in India is :", datetime_IN.strftime("%H:%M:%S"))
curr_date = date.today()
print(curr_date.weekday())
print(calendar.day_name[curr_date.weekday()])

df = pd.read_csv('C:/Users/ROHIT SINGH/PycharmProjects/advance-attendence-system-/timetable/timetable - Sheet1 (1).csv')
df.head()
df2 = pd.DataFrame(columns=['USN', 'TIME', 'SUBJECT'])


def time_in_range(current):
  start = datetime.time(9, 0, 0)
  end = datetime.time(9, 55, 0)
  if start <= current <= end:
    return "period 1"
  start = end
  end = datetime.time(10, 50, 0)
  if start <= current <= end:
    return "period 2"
  start = datetime.time(11, 5, 0)
  end = datetime.time(12, 0, 0)
  if start <= current <= end:
    return "period 3"
  start = end
  end = datetime.time(12, 55, 0)
  if start <= current <= end:
    return "period 4"
  start = datetime.time(13, 30, 0)
  end = datetime.time(14, 20, 0)
  if start <= current <= end:
    return "period 5"
  start = end
  end = datetime.time(15, 10, 0)
  if start <= current <= end:
    return "period 6"
  return 'free period'

# current = datetime.datetime.now().time()

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
      print(Usn)
      current = datetime.time(10, 50, 0)
      current = datetime.datetime.now().time()

      print(time_in_range(current))
      x = time_in_range(current)
      print(x)
      if x == 'free period':
        x = 'no class'
        df2 = df2.append({'USN': Usn, 'TIME': curr_date, 'SUBJECT': x},
                         ignore_index=True)
        df2 = df2.drop_duplicates()
        print(df2)
      else:
       df1 = df.iloc[[0]]
       x = df1[x].iloc[[0]].values
       print(x[0])

       df2 = df2.append({'USN': Usn, 'TIME': curr_date, 'SUBJECT': x[0]},
                        ignore_index=True)
       df2 = df2.drop_duplicates()
       print(df2)




      y1,x2,y2,x1 = faceLoc
      y1, x2, y2, x1 =   y1*4 ,x2*4 ,y2*4,x1*4
      cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
      cv2.rectangle(img, (x1, y2-35), (x2, y2), (0, 255, 0), cv2.FILLED)
      cv2.putText(img,Usn,(x1+15,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)

  cv2.imshow('webcam',img)
  cv2.waitKey(1)
