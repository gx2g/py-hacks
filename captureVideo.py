import cv2

# id of the video capturing device to open. To open default Camera, using default backend. 
capture =  cv2.VideoCapture(0)

while True:
    _, frame = capture.read()
    # we give the windows name of "Capture Webcamp"
    cv2.imshow("Capture from Webcam", frame)

    # ASCII code for the Escape key is 27. 
    if cv2.waitKey(1) == 27:
        break

# Release the capture and destroy all windows. 
capture.release()
cv2.destroyAllWindows()

