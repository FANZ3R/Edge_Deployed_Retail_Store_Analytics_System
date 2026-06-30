import cv2
import time

cap = cv2.VideoCapture("test1.mp4")

if not cap.isOpened():
    print("THe webcam is down or the file name is not correct or the file is not at the right location")
    
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fps = int(cap.get(cv2.CAP_PROP_FPS))



#ab mujhe output ke lie define karna hoga 
#phle toh i will have to make a codec which will be defining my compression method
#since output mei file size boht bada hojaata toh we need to write a compression method
#codec is basically the compression methodd for us
#fourcc basically stands for four character code

fourcc = cv2.VideoWriter_fourcc(*"mp4v")


# ab output video define karenge but uske bhi parameters hai kaafi
#1- video name
#2- codec we are using on the input video
#3- the fps we want our video to be in
#4 - the rectangle or the dimension of the video to be 
# the dimension which will be the same as the input feed dimensions

out = cv2.VideoWriter("output.mp4",fourcc,fps,(width,height))

x1,y1 = int(width*0.3) , int(height*0.3)
x2,y2 = int(width*0.7) , int(height*0.7)

while(True):
    start_time = time.time()
    
    ret, frame = cap.read()
    
    if not ret:
        break
    
    #ab mai ek rectangle banake dekhunga apne video ke frame pe
    cv2.rectangle(frame, (x1,y1), (x2,y2),(0,255,0),2)
    
    
    processing_fps = 1/(time.time()-start_time)
    cv2.putText(frame, f"FPS: {processing_fps:.1f}", (10,30),cv2.FONT_HERSHEY_COMPLEX,1 , (0,0,255),2)
    
    #ab put text se toh fps hamare frame mei daljaayega 
    #but abhi usko dikhaana bhi to hai
    #toh dikhaane ke lie ham abhi bhi imshow hi use karenge
    cv2.imshow("feed", frame)
    
    
    # ab dikha toh diya but still its not saving 
    #so for saving we will be doing is
    
    out.write(frame)
    
    delay = int(1000/fps)
    
    if(cv2.waitKey(delay) & 0XFF==ord('q')):
        break
    

cap.release()
out.release()
cv2.destroyAllWindows()
    
    


