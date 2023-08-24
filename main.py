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
reader1 = easyocr.Reader(['en'])
# For image 2 (detect portuguese)
reader2 = easyocr.Reader(['pt'])
# For image 3 (translate from japanese to english )
reader3 = easyocr.Reader(['ja', 'en'], gpu=False)

# Detect text on image
text1 = reader1.readtext(img1)
text2 = reader2.readtext(img2)
text3 = reader3.readtext(img3)

threshold = 0.25
for t1 in text1:
    print(t1)
    bounding_box, text, score = t1

    if score > threshold:
        cv2.rectangle(img1, bounding_box[0], bounding_box[2], (0, 255, 0), 1)
        cv2.putText(img1, text, bounding_box[0], cv2.FONT_HERSHEY_COMPLEX, 0.25, (255,0,0), 1)

#for t2 in text2:
#    print(t2)
#    bounding_box, text, score = t2

#    if score > threshold:
#        cv2.rectangle(img2, bounding_box[0], bounding_box[2], (0, 255, 0), 1)
#        cv2.putText(img2, text, bounding_box[0], cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0), 1)

#for t3 in text3:
#    print(t3)
#    bounding_box, text, score = t3

#    if score > threshold:
#        cv2.rectangle(img3, bounding_box[0], bounding_box[2], (0, 255, 0), 1)
#        cv2.putText(img3, text, bounding_box[0], cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0), 1)

plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
plt.show()