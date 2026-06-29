import cv2
import time


cap = cv2.VideoCapture("test1.mp4")

if not cap.isOpened():
    print("Could not open the video - Check webcam or video file name or its location")
    
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
    

ret , frame = cap.read()

while(True):
    start_time = time.time()
    ret , frame = cap.read()
    
    if not ret:
        break
    
    
    





