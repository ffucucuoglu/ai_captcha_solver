import imutils
import cv2


def resize_to_fit(image, width, height):

    WHITE=[255,255,255]
    (h, w) = image.shape[:2]

    if w > h:
        image = imutils.resize(image, width=width)

    else:
        image = imutils.resize(image, height=height)
    padW = int((width - image.shape[1]) / 2.0)
    padH = int((height - image.shape[0]) / 2.0)

    image = cv2.copyMakeBorder(image, padH, padH, padW, padW,cv2.BORDER_WRAP,value=WHITE)
    image = cv2.resize(image, (width, height))

    return image
