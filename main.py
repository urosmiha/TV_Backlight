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

    # Draw line from top left corner down to right bottom corner
    # syntax : frame, start coordinates, end coordinates, line colour (BGR), line thickness
    img = cv2.line(frame, (0,0), (width, height), (255,0,0), 10)
    # add new line - add this line on image
    img = cv2.line(img, (0, height), (width,0), (0,255,0), 10)
    cv2.imshow('frame', img)

    # image = np.zeros(frame.shape, np.uint8)
    # Display image
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