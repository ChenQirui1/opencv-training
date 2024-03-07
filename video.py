# import cv2 as cv

# cap = cv.VideoCapture("person-bicycle-car-detection.gif")
# if not cap.isOpened():
#     print("Cannot open camera")
#     exit()
# while True:
#     # Capture frame-by-frame
#     ret, frame = cap.read()

#     # if frame is read correctly ret is True
#     if not ret:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break
#     # Our operations on the frame come here
#     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     # Display the resulting frame
#     cv.imshow("frame", gray)
#     if cv.waitKey(1) == ord("q"):
#         break

# # When everything done, release the capture
# cap.release()
# cv.destroyAllWindows()

import numpy as np
import cv2 as cv


# cap = cv.VideoCapture("person-bicycle-car-detection.gif")
# while cap.isOpened():
#     ret, frame = cap.read()

#     if not ret:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break

#     ## to loop the video
#     # if not ret:
#     #     cap.set(cv.CAP_PROP_POS_FRAMES, 0)
#     #     continue

#     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

#     cv.imshow("frame", gray)
#     # if cv.waitKey(60) == ord("q"):
#     #     break
#     # Break the loop if 'q' is pressed
#     if cv.waitKey(25) & 0xFF == ord("q"):
#         break

# cap.release()
# cv.destroyAllWindows()

cap = cv.VideoCapture("person-bicycle-car-detection.gif")
# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*"DIVX")

# to get the frame size, get the flags for IOs
# https://stackoverflow.com/questions/63256300/how-do-i-get-usb-webcam-property-ids-for-opencv/63265171#63265171
# https://docs.opencv.org/4.x/d4/d15/group__videoio__flags__base.html
width = cap.get(cv.CAP_PROP_FRAME_WIDTH)  # float `width`
height = cap.get(cv.CAP_PROP_FRAME_HEIGHT)


# to correctly output video, the frame size, i.e. (width,height) needs to be
# the same as the processed frame size OR the original video size (if the unchanged)

out = cv.VideoWriter("output.avi", fourcc, 20.0, (int(width), int(height)))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    frame = cv.flip(frame, 0)

    # write the flipped frame
    out.write(frame)

    cv.imshow("frame", frame)
    if cv.waitKey(25) == ord("q"):
        break

# Release everything if job is finished
cap.release()
out.release()
cv.destroyAllWindows()
