# AI-Attendance-System

### Steps  
- Clone the repository. 
- The 'studentListPath' holds the path to the data folder change it accordingly.
- Open your cmd, activate env
- cd to main.py file directory
- *python main.py* on cmd

### Dependencies
- CMake
- dlib
- face_recognition
- CV2
- numpy
- os

###### Note
- To add new people to list, just drop a picture of them in the data folder. Make sure to rename the picture according to the attendies name.
- If you have an external webcam you may need to change the *cap = cv2.VideoCapture(0)* 0 in this place, it maybe replaced with 1/2/and so on.
