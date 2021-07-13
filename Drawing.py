import cv2
import numpy as np

range_array = np.load("./Range.npy")

video = cv2.VideoCapture(0)
x1, y1 = 0, 0
canvas = None
val = 1
thickness = 1

while True:
    ret, frame = video.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)

    if canvas is None:
        canvas = np.zeros_like(frame)
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, range_array[0], range_array[1])

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours and cv2.contourArea(max(contours, key = cv2.contourArea)) > 100:             
        c = max(contours, key = cv2.contourArea)    
        x2,y2,w,h = cv2.boundingRect(c)
 
        if x1 == 0 and y1 == 0: 
            x1, y1 = x2, y2
        else:
          
            canvas = cv2.line(canvas, (x1, y1),(x2,y2), [255*val,0,0], 10*thickness)
        
        x1, y1 = x2, y2
    else:
        x1, y1 = 0, 0

    cv2.imshow("Canvas", canvas)
    cv2.imshow("Mask", mask)

    key = cv2.waitKey(1)

    if key == ord('e'):
        val = not val

    if key == ord('i'):
        thickness = thickness + 2 if thickness < 10 else 10
    
    if key == ord('d'):
        thickness = thickness - 1 if thickness > 2 else 2

    if key == 27:
        break
    

video.release()
cv2.destroyAllWindows()
