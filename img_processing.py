""" This is the part of the code which does the initial log collection phase through image processing. 
The input will be the screenshot of the UI captured after each click and the output will be the text read from the screenshot"""

import cv2
import numpy as np
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
# Path of working folder on Disk
src_path = "C:/Users/Shubhangi/Desktop/FINAL_YEAR_PROJECT/UsabilityEvaluation/"

"""Gets all the text present in an image. 
The input image is the screenshot of the UI captured after a click event. """

def get_all_text(img_path):
    # Read image with opencv
    img = cv2.imread(img_path)

    # Convert to gray
    if img.all() != None:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    # Write image after removed noise
    cv2.imwrite(src_path + "removed_noise.png", img)

    #  Apply threshold to get image with only black and white
    #img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    # Write the image after apply opencv to do some ...
    cv2.imwrite(src_path + "thres.png", img)

    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(Image.open(src_path + "thres.png"))

    return result


""" The purpose of this function is to recognize the text in the sections that are highlighted and hence in a blue background.
This helps us obtain the current user location in the application."""

def get_blue_part(img_path):
    # Read image with opencv
    img = cv2.imread(img_path)
    # Convert BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_blue = np.array([100,25,30])
    upper_blue = np.array([130,255,255])
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(img,img, mask= mask)
    # Convert to gray
    if img.all() != None:
       img = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    res = cv2.dilate(img, kernel, iterations=1)
    res = cv2.erode(img, kernel, iterations=1)
    # Write the image after apply opencv to do some ...
    ret,thresh1 = cv2.threshold(res,127,255,cv2.THRESH_BINARY_INV)
    cv2.imwrite(src_path + "thres.png", thresh1)
    

    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(Image.open(src_path + "thres.png"))

    return result

print('--- Start recognize all text from image ---')
print(get_all_text(src_path + "sampleblue.png"))
print("------ Done -------")
print('\n\n--- Start recognize blue text from image ---')
print(get_blue_part(src_path + "sampleblue.png"))

print("------ Done -------")
