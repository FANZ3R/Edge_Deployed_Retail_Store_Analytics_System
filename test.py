import cv2
import time
from ultralytics import YOLO

cap = cv2.VideoCapture("test1.mp4")

if not cap.isOpened():
    print("Check if the webcam is working or the file name is wrong or the file location is given as wrong")
    
    
#ab input frame ka width aur heihgt define karleta
#kyuki isike basis pe hi mai define karunga apna  codec compression method

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

#ab isi dimensions pe mai apna codec lagaunga
#codec ek compression method hota basically
#mp4v ek codec hota hai mtlb mp4v hamara compression method hai idhar   
#mp4v is the default codec used which is generally trusted to produce mp4 videos smoothly

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter("output.mp4", fourcc, fps, (width,height))

model = YOLO("yolo11n.pt")

confidence_threshold = 0.5


while(True):
    start_time = time.time()
    ret , frame = cap.read()
    
    
    if ret == False:
        break
    
    results = model(frame,verbose = False)
    
    for box in results[0].boxes:
        #results[0] means 0th frame ke results
        class_id = int(box.cls[0])
        confidence = float(box.conf[0])
        
        if class_id !=0 or confidence < confidence_threshold:
            continue            
        
        px1,py1,px2,py2 = map(int,box.xyxy[0])
        
        cv2.rectangle(frame, (px1,py1),(px2,py2),(255,0,0),2)
        cv2.putText(frame,f"Confidence:{confidence:.2f}",(px1,py1-10),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
        
    processing_fps = 1/(time.time()-start_time)
    cv2.putText(frame,f"frame:{processing_fps:.1f}",(10,30),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
    cv2.imshow("feed",frame)
    
    
    out.write(frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
        

