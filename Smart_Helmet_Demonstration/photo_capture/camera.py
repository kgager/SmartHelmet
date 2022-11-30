# program to capture single image from webcam in python
import os 
# importing OpenCV library
from cv2 import (VideoCapture, namedWindow, imshow, waitKey, destroyWindow, imwrite)
  
# initialize the camera
# If you have multiple camera connected with 
# current device, assign a value in cam_port 
# variable according to that
cam_port = 0
cam = VideoCapture(cam_port)
directory = r'C:\Users\Kevin\Desktop\SmartHelmet\Smart_Helmet_Demonstration\yolov5\data\images'
directory2 = r'C:\Users\Kevin\Desktop\SmartHelmet\Smart_Helmet_Demonstration\yolov5'
# reading the input using the camera
result, image = cam.read()
print("Booting up Yolov5")
# If image will detected without any error, 
# show result
if result:
  
    # showing result, it take frame name and image 
    # output
    os.chdir(directory) 
    imshow("photoCaptureTestImage", image)
  
    # saving image in local storage
    imwrite("photoCaptureTestImage.png", image)
    
    # If keyboard interrupt occurs, destroy image 
    # window
    waitKey(0)
    #destroyWindow("photoCaptureTestImage")
    os.chdir(directory2) 
    
    os.system('python detect.py')
# If captured image is corrupted, moving to else part
else:
    print("No image detected. Please! try again")