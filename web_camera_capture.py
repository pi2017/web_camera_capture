#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import time

# ON web camera
camera_port = 0
cap = cv2.VideoCapture(camera_port, cv2.CAP_DSHOW)

# time out for warm camera
for i in range(30):
    cap.read()

# capture
ret, frame = cap.read()

# save to file
# Set the image name to the date it was captured
print ('foto saving...')
imageName = str('./static/' + time.strftime("%Y_%m_%d_%H_%M")) + '.jpg'
cv2.imwrite(imageName, frame)
print ('check folder for new foto')

# OFF web camera
print("web camera off")
cap.release()
cv2.destroyAllWindows()
