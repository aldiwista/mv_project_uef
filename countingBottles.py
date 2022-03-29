#Author : Aldi Wista FADHILAH and Atland BOKSI
import cv2
import numpy as np

im_file = "bottle_crate_06.png"
img = cv2.imread("images/"+im_file,cv2.IMREAD_COLOR)
img = cv2.medianBlur(img,5)
img2 = cv2.medianBlur(img,13)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

normal_bottles= cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,40
                                    ,param1 = 32
                                    ,param2=30,minRadius =1, maxRadius =26)

flip_bottles =cv2.HoughCircles(gray2,cv2.HOUGH_GRADIENT,1,40
                                    ,param1 = 32
                                    ,param2=30,minRadius =30, maxRadius =38)

num_bottles=0
if normal_bottles is not None:
    normal_bottles = np.uint16(np.around(normal_bottles))
  
    for pt in normal_bottles[0, :]:
        a, b, r = pt[0], pt[1], pt[2]
        cv2.circle(img, (a, b), r, (0, 255, 0), 2)  
        cv2.circle(img, (a, b), 1, (0, 0, 255), 3)
        num_bottles=num_bottles+1
else: 
    num_bottles = 0

num_flipped_bottles = 0
if flip_bottles is not None:
    flip_bottles = np.uint16(np.around(flip_bottles))  
    for pt in flip_bottles[0, :]:
        a, b, r = pt[0], pt[1], pt[2]
        cv2.circle(img, (a, b), r, (255, 0, 255), 2)
        cv2.circle(img, (a, b), 1, (0, 0, 255), 3)
        num_flipped_bottles =num_flipped_bottles +1
else: 
    num_flipped_bottles  = 0

num_bottles = num_bottles+num_flipped_bottles

font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
org = (200,50)
color = (255,255,255)
text = '# bottles = '+str(num_bottles)
img = cv2.putText(img, text, org, font, 
                   font_scale, color, 5, cv2.LINE_AA)

cv2.imshow("Detected Bottles", img)
folder = "results/"
cv2.imwrite(folder+"results_"+im_file,img)
cv2.waitKey(0)
cv2.destroyAllWindows()