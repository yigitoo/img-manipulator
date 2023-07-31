import cv2
import numpy as np


img = cv2.imread('pump.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower = np.array([90, 100, 20])
upper = np.array([120, 255, 255])

mask = cv2.inRange(hsv, lower, upper)
inv_mask = cv2.bitwise_not(mask)

h, s, v = cv2.split(hsv)

h = np.mod(h + 155, 180)
s = np.clip(s - 0, 0, 255)
v = np.clip(v + 255, 0, 255)

hsv = cv2.merge([h, s, v])

bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

result = cv2.bitwise_or(cv2.bitwise_and(img, img, mask=inv_mask), cv2.bitwise_and(bgr, bgr, mask=mask))

cv2.imwrite("out.jpg", result)
