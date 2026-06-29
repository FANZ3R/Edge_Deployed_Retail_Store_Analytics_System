import cv2
import time


cap = cv2.VideoCapture("test1.mp4")

if not cap.isOpened():
    print("Could not open the video - Check webcam or video file name or its location")
    
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
    

#phle codec banayenge kis basis pe compression karna hai hamei
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter("output.mp4",fourcc,fps,(width,height))



while(True):
    start_time = time.time()
    ret , frame = cap.read()
    
    if not ret:
        break
    
    #ab rectangle draw karna hai ek frame pe
    cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0),2)
    
    
    
    





