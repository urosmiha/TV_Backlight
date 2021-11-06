import numpy as np
import cv2

# def drawLine(frame):
#     # Draw line from top left corner down to right bottom corner
#     # syntax : frame, start coordinates, end coordinates, line colour (BGR), line thickness
#     img = cv2.line(frame, (0,0), (width, height), (255,0,0), 10)
#     # add new line - add this line on image
#     img = cv2.line(img, (0, height), (width,0), (0,255,0), 10)
#     cv2.imshow('frame', img)


def main():
    # Read camera
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        # You can access different properties of cap by using a different number
        # e.g. 3 - width, 4 - height
        # Comes as float by default, so convert it to int
        width = int(cap.get(3))
        height = int(cap.get(4))

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # light blue
        lower_blue = np.array([90, 50, 50])
        # darker blue
        upper_blue = np.array([130, 255, 255])

        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        # only keep pixels that match the mask pixel displayed
        result = cv2.bitwise_and(frame, frame, mask=mask)

        cv2.imshow('hsv', result)

        # image = np.zeros(frame.shape, np.uint8)
        # Display image
        # cv2.imshow('frame', image)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()