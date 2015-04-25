import cv2
import zbarlight

# initialize camera, set frame width and height
cap = cv2.VideoCapture(0)
width = 640
height = 480
cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, height)

# quick+dirty function to get an image from the camera
def getImage():
    retval, image = cap.read()
    return image

# get the image from the camera, write it to a file
image = getImage()
cv2.imwrite('test_py.jpg', image)

# load the image file, convert to grayscale
frame = cv2.imread('test_py.jpg', cv2.cv.CV_LOAD_IMAGE_GRAYSCALE)

# convert the image file to string so zbarlight can read it
image_string = frame.tostring()

# scan the image
code = zbarlight.qr_code_scanner(image_string, width, height)

# if there's a single qr code in the frame, its value is set
# if not, an exception is thrown
try:
    value = code.decode()
except:
    value = "No code or multiple codes detected"

print value
