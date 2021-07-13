import numpy as np
import cv2
import matplotlib.pyplot as plt

video = cv2.VideoCapture(0)

def nothing(a):
    ''' This is Empty '''
    pass
    

cv2.namedWindow("Track-Bars")

cv2.createTrackbar("Lower-H", "Track-Bars", 0, 179, nothing)
cv2.createTrackbar("Upper-H", "Track-Bars", 179, 179, nothing)
cv2.createTrackbar("Lower-S", "Track-Bars", 154, 255, nothing)
cv2.createTrackbar("Upper-S", "Track-Bars", 255, 255, nothing)
cv2.createTrackbar("Lower-L", "Track-Bars", 0, 255, nothing)
cv2.createTrackbar("Upper-L", "Track-Bars", 255, 255, nothing)

while True:
    ret, frame = video.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    image = frame
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lh = cv2.getTrackbarPos("Lower-H", "Track-Bars")
    hh = cv2.getTrackbarPos("Upper-H", "Track-Bars")
    ls = cv2.getTrackbarPos("Lower-S", "Track-Bars")
    hs = cv2.getTrackbarPos("Upper-S", "Track-Bars")
    ll = cv2.getTrackbarPos("Lower-L", "Track-Bars")
    hl = cv2.getTrackbarPos("Upper-L", "Track-Bars")

    l_range = np.array([lh, ls, ll])
    h_range = np.array([hh, hs, hl])

    print(l_range, h_range)

    mask = cv2.inRange(frame, l_range, h_range)
    result = cv2.bitwise_and(frame, frame, mask = mask)  
    image = cv2.bitwise_and(image, image, mask = mask)
      
    cv2.imshow("Frame", frame)
    cv2.imshow("Result", result)
    cv2.imshow("Mask", mask)
    cv2.imshow("Image", image)

    if cv2.waitKey(1) == 27:
        penrange = [l_range, h_range]
        np.save("Range", penrange)
        break

video.release()
cv2.destroyAllWindows()