import cv2


Stitcher = cv2.createStitcher(False)

Image1 = cv2.imread("images/IMG_3.jpg")
Image2 = cv2.imread("images/IMG_4.jpg")

try:
    output = Stitcher.stitch((Image1, Image2))
except Exception as e:
    print(e)

cv2.imwrite("output/output2.jpg", output[1])
print("Stitched image created successfully in output directory")
