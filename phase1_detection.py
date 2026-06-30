import cv2
import time
from ultralytics import YOLO


cap = cv2.VideoCapture("test1.mp4")

if not cap.isOpened():
    print("Could not open the video - Check webcam or video file name or its location")
    
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
    

#phle codec banayenge kis basis pe compression karna hai hamei
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter("output.mp4",fourcc,fps,(width,height))

model = YOLO("yolo11n.pt")

confidence_threshold = 0.5

x1,y1 = int(width*0.1) , int(height*0.1)
x2,y2 = int(width*0.4) , int(height*0.4)


while(True):
    start_time = time.time()
    ret , frame = cap.read()
    
    if not ret:
        break
    
    
    
    results = model(frame,verbose= False)
    
    for box in results[0].boxes:
        class_id = int(box.cls[0])
        confidence = float(box.conf[0])
        
        if (class_id != 0) or confidence < confidence_threshold:
            continue
        
        #ab har box ek person ko batayega
        #aur har box pe 2 pairs of cordinates honge
        #wahi top left and bottom right
        
        
        px1, py1, px2, py2 = map(int,box.xyxy[0])
        
        cv2.rectangle(frame, (px1,py1), (px2,py2),(255,0,0),2)
        cv2.putText(frame, f"Confidence: {confidence:.2f}", (px1,py1-10),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
        
    
    
    #fps is rate so frames per second
    processing_fps = 1/(time.time() - start_time)
    cv2.putText(frame, f"FPS: {processing_fps: .1f}", (10,30),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
    cv2.imshow("feed",frame)
    #ab save kardenge current processed frame ko
    
    #using delay we can control the speed of our output stream
    #ways to use it
    # we say 
    # delay = 1000/fps
    #then
    #if cv2.waitKey(delay) & 0XFF == ord('q'):S
    #   break;
    # this will let us control the speed of our output feed
    # why we do 1000/fps 
    #because waitkey expects milliseconds
    #so we need to give it in milliseconds   
    
    
    out.write(frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    
cap.release()
out.release()
cv2.destroyAllWindows()


    
    
    





