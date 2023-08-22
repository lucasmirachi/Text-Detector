import cv2
import easyocr
import matplotlib.pyplot as plt

img1_path = './data/test1.png'
img2_path = './data/test2.png'
img3_path = './data/test3.png'

img1 = cv2.imread(img1_path)
img2 = cv2.imread(img2_path)
img3 = cv2.imread(img3_path)

# Instance text detector
# For image 1 (detect english)
#reader1 = easyocr.Reader(['en'], gpu=False)
# For image 2 (detect portuguese)
reader2 = easyocr.Reader(['pt'])
# For image 3 (translate from japanese to english )
#reader3 = easyocr.Reader(['ja', 'en'], gpu=False)

# Detect text on image
#text1 = reader1.readtext(img1)
text2 = reader2.readtext(img2)
#text3 = reader3.readtext(img3)

#for t1 in text1:
#    print(t1)

for t2 in text2:
    print(t2)

#for t3 in text3:
#    print(t3)