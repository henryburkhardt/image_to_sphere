#Import Packages 
import cv2
import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt
import csv
import os
import sys
  
#Locate image file 
file_path = input("IMAGE NAME: ")
file_path = './'+file_path

#Check file exists 
assert os.path.exists(file_path), "ERROR FILE NOT FOUND AT:  "+str(file_path)
f = open(file_path,'r+')
print("[OK] FILE LOCATED")

#Read Image
img = cv2.imread(file_path, cv2.IMREAD_COLOR)
print('[OK] IMAGE READ')
  
# Convert to grayscale.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
# Blur using 3 * 3 kernel.
gray_blurred = cv2.blur(gray, (3, 3))

# Apply Hough transform on the blurred image.
detected_circles = cv2.HoughCircles(gray_blurred, 
                   cv2.HOUGH_GRADIENT, 1, 20, param1 = 50,
               param2 = 15, minRadius = 1, maxRadius = 40)

#Initiate data storage variables 
circle_data_pixel = [['ID','RADIUS','X','Y','Z']]
circle_data_unity = [['ID','RADIUS','X','Y','Z']]
n=0
skip = 0 
# Draw circles that are detected.
if detected_circles is not None:
    print('[OK] CIRLCES DETECTED')

  
    # Convert the circle parameters a, b and r to integers.
    detected_circles = np.uint16(np.around(detected_circles))
  
    for pt in detected_circles[0, :]:
        a, b, r = pt[0], pt[1], pt[2]
  
        # Draw the circumference of the circle.
        cv2.circle(img, (a, b), r, (0, 255, 0), 2)
  
        # Draw a small circle (of radius 1) to show the center.
        cv2.circle(img, (a, b), 1, (0, 0, 255), 3)

        #z axis translation based on size 
        phys_radius = 39
        per_radius = r 
        percent_change = 1 - (r/39)
        z = percent_change*img.shape[1]

        # Labe with circle ID
        cv2.putText(img, str(n), (a,b), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 1, cv2.LINE_AA)

        # Append circle dataset 
        circle_list = [n,r,a,b,z]

        if r > 5:
            circle_data_pixel.append(circle_list)
            n=n+1

            #Unity translation
            circle_list_unity = [n,(r/25),round(((a/img.shape[1])*23),4),round(((b/img.shape[0])*33),4),round(((z/1319.666667)*50),4)]
            #print(circle_list_unity)
            circle_data_unity.append(circle_list_unity)
        else:
            skip = skip +1 
            print('skipped',str(skip))

#Image output scailing options
scale_percent = 100 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

#Write image output file
cv2.imwrite('circle_3_result.jpg', img)

print("\n[OK] Circle Count: ", len(circle_data_unity),"\n")

#Write CSVs to local direcory   
with open("./circle_3_csv/circle_data_pixel.csv","w", newline='',) as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(circle_data_pixel)

with open("./circle_3_csv/circle_data_unity.csv","w", newline='',) as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(circle_data_unity)

#Write to Unity directory
write_unity = input("Write CSV to Unity Assests Folder? [Y/N]:  ")

if write_unity == "y" or write_unity == "Y":
    #Remove old unity meta data file
    if os.path.exists("C:/Users/22henrywb/MyFirstGame/Assets/Resources/circle_data_unity.csv.meta"):
        os.remove("C:/Users/22henrywb/MyFirstGame/Assets/Resources/circle_data_unity.csv.meta")
        print("[1]: Old Meta File Remmoved")
    else:
        print("No Meta File Found")

    with open("C:/Users/22henrywb/MyFirstGame/Assets/Resources/circle_data_unity.csv","w", newline='',) as my_csv:
        csvWriter = csv.writer(my_csv,delimiter=',')
        csvWriter.writerows(circle_data_unity)
    print("[2]: Scuesfully Written")
elif write_unity == 'n' or write_unity == 'N':
    print("[2]: Not Written to Unity")
else:
    print("WRITE ERROR")    