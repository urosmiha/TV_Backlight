import numpy as np
import cv2

cap = cv2.VideoCapture(0)

x = 0
while True:
    ret, frame = cap.read()
    # You can access different properties of cap by using a different number
    # e.g. 3 - width, 4 - height
    # Comes as float by default, so convert it to int
    width = int(cap.get(3))
    height = int(cap.get(4))

    # Show camera footage in a frame
    # cv2.imshow('frame',frame)

    image = np.zeros(frame.shape, np.uint8)

    # cv2.imshow('frame', image)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


# Load image for OpenCV to read
# -1 : load as colout
# 0  : load as greyscale
# 1  : load as transparent
# img = cv2.imread('image.jpg', -1)