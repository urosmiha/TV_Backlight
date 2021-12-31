import numpy as np
import cv2

# def drawLine(frame):
#     # Draw line from top left corner down to right bottom corner
#     # syntax : frame, start coordinates, end coordinates, line colour (BGR), line thickness
#     img = cv2.line(frame, (0,0), (width, height), (255,0,0), 10)
#     # add new line - add this line on image
#     img = cv2.line(img, (0, height), (width,0), (0,255,0), 10)
#     cv2.imshow('frame', img)


def highlightColour(frame):

    # covert image to hue saturation brightness image
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # light blue pixels
    lower_blue = np.array([90, 50, 50])
    # darker blue pixels
    upper_blue = np.array([130, 255, 255])

    # create a mask so we can run bitwise-and on it to filer out the colour
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # only keep pixels that match the mask pixel displayed
    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('hsv', result)


def convertBGRtoHSV(BGR_value):
    # BGR_colour = np.array([[BGR_value]])
    BGR_colour = np.array([[[255, 0, 0]]])
    x = cv2.cvtColor(BGR_colour, cv2.COLOR_BGR2HSV)
    print("HSV Value:")
    print(x)


def main():
    print("read camera...")
    # Read camera
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        # You can access different properties of cap by using a different number
        # e.g. 3 - width, 4 - height
        # Comes as float by default, so convert it to int
        width = int(cap.get(3))
        height = int(cap.get(4))

        highlightColour(frame)

        # Display image
        # cv2.imshow('frame', result)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # convertBGRtoHSV([255,0,0])
    main()