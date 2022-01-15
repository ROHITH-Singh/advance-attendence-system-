# **ATTENDANCE SYSTEM USING FACE RECOGNIZATION**

A report submitted to

RAMAIAH INSTITUTE OF TECHNOLOGY

Bengaluru

**ISE741- Deep Learning (Miniproject)**

as partial fulfillment of the requirement for

Bachelor of Engineering

by

**ROHIT KUMAR SINGH ( USN- 1MS18IS080 )**
**SRINIVAS ( USN- 1MS18IS414 )**
**ADITA YADAV ( USN- 1MS17IS006 )**

under the guidance of

**SUMANA M**

**RAMAIAH**
**Institute of Technology**

DEPARTMENT OF INFORMATION SCIENCE AND ENGINEERING

RAMAIAH INSTITUTE OF TECHNOLOGY

January 2022
Department of Information Science and Engineering
Ramaiah Institute of Technology
Bengaluru – 54
**RAMAIAH**
**Institute of Technology**

*Student Name,  USN*,  has given the presentation and submitted the report on

*Title*

Signature of Examiner               					 Signature of Internal Guide
Name :									Name:

**ABSTRACT**
The attendance is taken in every organization. Traditional approach for attendance is, professor calls student name & record attendance. For each lecture this is wastage of time. To avoid these losses, we are about to use automatic process which is based on image processing. In this project approach, we are using face detection & face recognition system. The first phase is preprocessing where the face detection is processed through the step image processing. It includes the face detection and face recognition process. Second phase is feature extraction. Step by step execution of these techniques (Image Processing) helps to achieve the final output. The working of this project is to detect and recognize the face and mark the attendance for the corresponding face in the database. Input of this project is face detection and recognition and output is to mark the attendance. Our project is being presented as a solution for the Automatic Attendance Marking System. It is designed to be reliable and low power. The Automatic face detection and recognition proposed to attendance marking in database acts as the solution for the automatic attendance marking system.

Keywords: Attendance system, Automated attendance, Image Processing, Face detection, Feature matching, Face recognition.

(WARN_UNRECOGNIZED_ELEMENT: PAGE_BREAK)

# CONTENTS
1. **Introduction	**
 1. **Motivation**

 2. **Objectives**

 3. **Introduction to the project done**

2. **Literature survey.	**
3. **Proposed Model**
4. **Detailed Design **
5. **Coding and Implementation**
6. **Testing**
7. **Conclusion**
8. **References**
<br>
# **1.1 MOTIVATION:** 
<br>
Taking and tracking students attendance manually, losing attendance sheets, dishonesty, wasted time and high error scales are problems facing the lecturers use the existing attendance system. Facial recognition attendance systems are programmed to handle it all on a very large scale. The main motivation of this project is to remove the slow and inefficient traditional manner of attendance and provide easy and fast technique to provide attendance according to the time table. It detects the faces and mark attendance accordingly. This system will prevent unnecessary wastage of time of classes that is usually wasted in form of class roll calls.

(WARN_UNRECOGNIZED_ELEMENT: PAGE_BREAK)
**1.2 ****OBJECTIVES:**
The main objective of this work are:
* To make the attendance marking and management system efficient, time saving, simple and easy.
* This application can monitor the whole system.
* It is the fastest and safest method of security in which student cannot present himself or his friend while they are not.
* Produce monthly reports for lecturers which saves their time and energy.
* Flexibility, Lecture capability of editing attendance records.
* Reduce manual process errors by providing automated and a reliable attendance system using face recognition technology.

**1.3 INTRODUCTION: **
Facial or face recognition is defined as “the science which involves the understanding of how the faces are recognized by biological systems and how this can be emulated by computer systems.
Over the past decade, taking down students’ attendance process had been developed and changed.The main aim of this system is to automate, facilitate, speed up and save time and efforts.
Even though keeping attendance data is an essential part of educational institutes, there has been little advancement in the attendance system. Still, many institutes use traditional handwritten attendance or use some spreadsheet on the computer. This makes it hard for teachers to track the students’ attendance data and their progress. Chances of attendance fraud in this system are relatively higher than it is in automated attendance system. Unless the attendance data is correct, schools cannot formulate proper policies and practices to improve the quality of education
Many people are familiar with facial recognition technology thanks to Face ID, which is now widely used in the mobile market. Typically, facial recognition doesn't use a huge database of photos to determine a person's identity; it merely identifies and recognizes one person as the sole owner of the device, limiting access to others. Facial recognition systems are used in several domains today.
This project introduces an involuntary attendance marking system, devoid of any kind of interference with the normal teaching procedure. The system can be also implemented during exam sessions or in other teaching activities where attendance is highly essential. This system eliminates classical student identification such as calling name of the student, or checking respective identification cards of the student, which can not only interfere with the ongoing teaching process, but also can be stressful for students during examination sessions

(WARN_UNRECOGNIZED_ELEMENT: PAGE_BREAK)

**2. LITERATURE SURVEY : **
A number of researches are done for the past few years on face recognition for the attendance system. In this section, few of the works are summarized:
* Smitha, Pavithra S Hegde, Afshin : applied Haar-Cascade classifier; Local Binary Pattern Histogram for the attendance marking system. Faces  are  detected  and  recognized  from  live  streaming  video  of  the  classroom. Attendance will be mailed to the respective faculty at the end of the session. [1]

* Okokpujie,  Kennedy  O.: authors  have designed and  implemented an attendance system which uses iris biometrics. Initially, the attendees were asked to register their details along with their unique  iris template.  At the  time of attendance,  the system automatically  took  class  attendance  by  capturing  the  eye image of each attendee, recognizing their iris, and searching for a match in the  created database. The prototype was web based. [2]

* Akbar,  Md  Sajid : proposed  a  model  of  an  automated attendance  system.  The  model  focuses  on  how  face recognition incorporated with Radio Frequency Identification (RFID) detect the authorized students and counts as they get in  and  get  out  form  the  classroom.  The  system  keeps  the authentic record of every registered student. The system also keeps  the  data  of  every  student  registered  for  a  particular course  in  the  attendance  log  and  provides  necessary information according to the need. [3]

* Akshara Jadhav, Akshay Jadhav Tushar Ladhe, Krishna Yeoleka : he recognized face is separated and exposed to pre- preparing. This pre-preparing step includes with histogram leveling of the extricated face picture and is resized to 100×100. In this framework, in the wake of perceiving the essences of the understudies, the names are refreshed into an exceed expectations sheet.The exceed expectations sheet is created by trading instrument present in the database framework. [4]

* Nandhini R: the author mentions the fundamental working rule of the venture is that, the video caught information is changed over into picture to identify and perceive it. CNN calculation is executed to recognize the faces. A CNN (Convolution Neural Network), utilizes a framework like a multilayer perceptron, intended to process the prerequisites faster. After the end of distinguishing and preparing the face, it is contrasted with the faces present in the understudies database to refresh the participation of the students. [5]

(WARN_UNRECOGNIZED_ELEMENT: PAGE_BREAK)

**3. PROPOSED MODEL:**
In order to mark attendance, we follow a series of steps which includes enrolment, face detection, face recognition, and then marking the attendance in a database.
![](WARN_REPLACE_IMG_URL)
**Step1 :Face Detection:**
For the application of face recognition, detection of face is very important and the first step. After detecting a face the face recognition algorithm can only be functional. Face detection itself involves some complexities for example surroundings, postures, enlightenment etc.  The camera detects and locates an image of a face, either alone or in a crowd. The image may depict the person looking straight at the camera or in profile.It is performed by  OpenCV.
**Step2: Face Analysis: **
The face image is captured and analyzed. The software examines the geometry of the face and some key factors, which include variables such as the distance between the eyes, the depth of the eye sockets, the distance between the forehead and the chin, the shape of the cheekbones and the contour of the lips, eyes and chin. They aim to identify the main features of the face and are essential to distinguish it. Later, during the recognition process histogram  of the  face to be recognized is calculated and then compared with the already computed histograms and returns the  best matched label associated with the student.

**Step3: Convert the image into data: **
The face capture process transforms the information about the face into a set of digital information. This set of information is stored in the form of a numeric code called a faceprint. A person's faceprint is as unique as their fingerprints.
**Step4: Finding a match: **
The subject's faceprint is compared to a database of known faces. If the facial fingerprint of the student matches an image in a facial recognition database , identification is performed and attendance is marked.
(WARN_UNRECOGNIZED_ELEMENT: PAGE_BREAK)
**4. DETAILED DESIGN:**
**1.OpenCV:**
OpenCV (Open Source Computer Vision Library) is an open source computer vision and machine learning software library. OpenCV was built to provide a common infrastructure for computer vision applications and to accelerate the use of machine perception in the commercial products. Being a BSD-licensed product, OpenCV makes it easy for businesses to utilize and modify the code. To use opencv we use the command OpenCV was designed for computational efficiency and having a high focus on real-time image detection. OpenCV is coded with optimized C and can take work with multicore processors. If we desire more automatic optimization using Intel architectures [Intel], you can buy Intel’s Integrated Performance Primitives (IPP) libraries [IPP]. These consist of low-level routines in various algorithmic areas which are optimized. OpenCV automatically uses the IPP library, at runtime if that library is installed. One of OpenCVs goals is to provide a simple-to-use computer vision infrastructure which helps people to build highly sophisticated vision applications fast. The OpenCV library, containing over 500 functions, spans many areas in vision. Because computer vision and machine learning oft en goes hand-in-hand, OpenCV also has a complete, general-purpose, Machine Learning Library (MLL).This sub library is focused on statistical pattern recognition and clustering. The MLL is very useful for the vision functions that are the basis of OpenCV’s usefulness, but is general enough to be used for any machine learning problem

**The Origin of OpenCV **

OpenCV came out of an Intel Research initiative meant to advance CPU-intensive applications. Toward this end, Intel launched various projects that included real-time ray tracing and also 3D display walls. One of the programmers working for Intel at the time was visiting universities. He noticed that a few top university groups, like the MIT Media Lab, used to have well-developed as well as internally open computer vision infrastructures— code that was passed from one student to another and which
gave each subsequent student a valuable foundation while developing his own vision application. Instead of having to reinvent the basic functions from beginning, a new student may start by adding to that which came before.

**Advantages of OpenCV:**
* OpenCV is an open-source library and is free of cost.
* As compared to other libraries, it is fast since it is written in C/C++.
* It works better on System with lesser **RAM**
* It supports most of the Operating Systems such as Windows, Linux
and MacOS.

**OpenCV's application areas include:  **
2D and 3D feature toolkits
∙  Egomotion estimation
∙  Facial recognition system
∙  Gesture recognition
∙  Human–computer interaction (HCI)
∙  Mobile robotic
∙  Motion understanding
∙  Object identification
∙  Segmentation and recognition
∙  Stereopsis stereo vision: depth perception from 2 cameras
∙  Structure from motion (SFM)

**2.NUMPY:**
NumPy is the fundamental package for scientific computing in Python. It is a Python library that provides a multidimensional array object, various derived objects (such as masked arrays and matrices), and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation and much more.
NumPy arrays have a fixed size at creation, unlike Python lists (which can grow dynamically). Changing the size of an ndarray will create a new array and delete the original. The elements in a NumPy array are all required to be of the same data type, and thus will be the same size in memory. The exception: one can have arrays of (Python, including NumPy) objects, thereby allowing for arrays of different sized elements.  NumPy arrays facilitate advanced mathematical and other types of operations on large numbers of data. Typically, such operations are executed more efficiently and with less code than is possible using Python’s built-in sequences. A growing plethora of scientific and mathematical Python-based packages are using NumPy arrays; though these typically support Python-sequence input, they convert such input to NumPy arrays prior to processing, and they often output NumPy arrays. In other words, in order to efficiently use much (perhaps even most) of today’s scientific/mathematical Python-based software, just knowing how to use Python’s built-in sequence types is insufficient - one also needs to know how to use NumPy arrays.
NumPy fully supports an object-oriented approach, starting, once again, with ndarray. For example, ndarray is a class, possessing numerous methods and attributes. Many of its methods are mirrored by functions in the outermost NumPy namespace, allowing the programmer to code in whichever paradigm they prefer. This flexibility has allowed the NumPy array dialect and NumPy ndarray class to become the de-facto language of multi-dimensional data interchange used in Python
**3.Face recognition:**
Face detection is the process of detecting a human face or multiple human faces in a digital image or video. Face detection is a sub-process of facial recognition, but the term typically refers to image-based face recognition where only the locations of faces in an image are used to identify or verify a person, while facial recognition also creates a model of their unique face, which is then matched to a target face. Face detection is different than face recognition in that face recognition is the automated process of identifying or verifying a person from a digital image or a video source.
While humans can recognize faces without much effort, facial recognition is a challenging [pattern recognition](https://en.wikipedia.org/wiki/Pattern_recognition) problem in [computing](https://en.wikipedia.org/wiki/Computing). Facial recognition systems attempt to identify a human face, which is three-dimensional and changes in appearance with lighting and facial expression, based on its two-dimensional image. To accomplish this computational task, facial recognition systems perform four steps. First [face detection](https://en.wikipedia.org/wiki/Face_detection) is used to segment the face from the image background. In the second step the segmented face image is aligned to account for face [pose](https://en.wikipedia.org/wiki/Pose), image size and photographic properties, such as [illumination](https://en.wikipedia.org/wiki/Illumination_(image)) and [grayscale](https://en.wikipedia.org/wiki/Grayscale). The purpose of the alignment process is to enable the accurate localization of facial features in the third step, the facial feature extraction. Features such as eyes, nose and mouth are pinpointed and measured in the image to represent the face. The so established [feature vector](https://en.wikipedia.org/wiki/Feature_vector) of the face is then, in the fourth step, matched against a database of faces.

## What are the challenges of facial recognition?
Some challenges of facial recognition are discussed here. The algorithms involved in facial recognition systems are quite complex, which makes them highly inconsistent. The facial recognition systems are easily fooled by environmental and lighting changes, different poses, and even similar-looking people. Facial recognition systems require very high computational power, which is why facial recognition systems are mostly used with high-end smartphones and laptops. A facial recognition system might detect several false matches in a single frame. The software has to determine what the user intended to do, which is not an easy task for the software.

**4.Pandas:**
Pandas is an open-source library that is made mainly for working with relational or labeled data both easily and intuitively. It provides various data structures and operations for manipulating numerical data and time series. This library is built on top of the NumPy library. Pandas is fast and it has high performance & productivity for users.
Prior to Pandas, Python was majorly used for data munging and preparation. It had very little contribution towards data analysis. Pandas solved this problem. Using Pandas, we can accomplish five typical steps in the processing and analysis of data, regardless of the origin of data — load, prepare, manipulate, model, and analyze.
Python with Pandas is used in a wide range of fields including academic and commercial domains including finance, economics, Statistics, analytics, etc.
**Key Features of Pandas:**
* Fast and efficient DataFrame object with default and customized indexing.
* Tools for loading data into in-memory data objects from different file formats.
* Data alignment and integrated handling of missing data.
* Reshaping and pivoting of date sets.
* Label-based slicing, indexing and subsetting of large data sets.
* Columns from a data structure can be deleted or inserted.
* Group by data for aggregation and transformations.
* High performance merging and joining of data.
* Time Series functionality.

7. **CODING AND IMPLEMENTATION:**
* **    Importing libraries and packages :  **

![](WARN_REPLACE_IMG_URL)

* **Function for determining period/class depending upon the time**
![](WARN_REPLACE_IMG_URL)
* **Finding the face encodings of the registered students from the database: **
![](WARN_REPLACE_IMG_URL)
* **Comparing the encodings with live video capture and storing in a dataframe **
![](WARN_REPLACE_IMG_URL)
8. **Testing : **
* **Getting encodings of 5 images of students :**
![](WARN_REPLACE_IMG_URL)
* **Live recognising  student :**
![](WARN_REPLACE_IMG_URL)
![](WARN_REPLACE_IMG_URL)

* **Adding recongside student to dataframe  according to the time and period:**
![](WARN_REPLACE_IMG_URL)

**7. CONCLUSION:**
Face detection and face recognition are very important technologies these days, furthermore we noticed that they have a variety of uses such as cellphones, army uses, and some high risk information offices. We decided to make a device that detects and recognizes the face as a student attendance system and can be a substitute for the regular paper attendance system and fingerprint attendance system. Face recognition attendance systems are modern utilities that are a requirement of even the post-pandemic era. These systems make student attendance tracking accurate while saving costs. Such a system also adds a layer of security in the school/colleges. Facial recognition systems are the best modern-day solution for tracking students hours.It’s time to upgrade to a facial recognition attendance system. The above method provides the best outcome. This is achieved using OpenCV for frame extraction and Numpy,Pandas,Python Libraries for face recognition. This method will have higher accuracy in recognition of multiple faces from a single frame with lower response time.

**REFERENCES****:**
[1] Smitha, Pavithra S Hegde, Afshin ,“Face Recognition based Attendance Management System” Vol. 9 Issue 05, May-2020

[2] Okokpujie,  Kennedy  O.,  et  al.  "Design  and  implementation of  a student  attendance  system  using  iris  biometric  recognition." 2017 International  Conference  on  Computational  Science  and Computational Intelligence (CSCI). IEEE, 2017

[3].Akbar,  Md  Sajid,  et  al.  "Face  Recognition  and  RFID  Verified Attendance System." 2018 International Conference on Computing, Electronics & Communications Engineering (iCCECE). IEEE, 2018

[4] Akshara Jadhav, Akshay Jadhav Tushar Ladhe, Krishna Yeolekar “Automated Attendance System Using Face Recognition” Volume: 04 Issue: 01 | Jan -2017

[5] Nandhini R, Duraimurugan N, S.P.Chokkalingam “Face Recognition Based Attendance System” ISSN: 2249 – 8958, Volume-8, Issue-3S, February 2019
* 
(WARN_UNRECOGNIZED_ELEMENT: PAGE_BREAK)

(WARN_UNRECOGNIZED_ELEMENT: PAGE_BREAK)
