# Finger-Pen
## Virtual Air pen 
Working:
1. First Run the detection.py file, using this file we can detect the color that we wat to use as the marker for our air pen.
2. These values are saved in the Range.npy file
3. Simply open the drawing.py file. This file will automatically read the Range.npy file and you can statr drawing.

## Detection
Here we simply use range bars to adjust the Hue, Saturation and Value to detect our marker.
Here you will see a mask. You can close the Program once you are statisfied with the mask.

## Drawing
Here we are using contour detection of the specific color ranges that were detected in the Detection part and were saved in the Range.npy file.
Some Keys:
E - To toggle between erasing and drawing
I - to incremet the size of the brush
D - to decrement the size of the brush
