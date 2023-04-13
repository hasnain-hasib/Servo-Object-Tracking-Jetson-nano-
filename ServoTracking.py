import cv2
import time
import numpy as np
from adafruit_servokit import ServoKit
import time

gear = ServoKit(channels=16)
pan_servo = gear.servo[0]
tilt_servo = gear.servo[1]
pan= 90
tilt = 45
pan_servo.angle = pan
tilt_servo.angle = tilt

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    start_time = time.time()
    ret, frame = capture.read()

    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    
    lower_purple = np.array([120,50,50])
    upper_purple = np.array([170,255,255])

    
    mask = cv2.inRange(hsv, lower_purple, upper_purple)
    smallmask= cv2.resize(mask,(300,300))
    cv2.imshow('smallmask',smallmask)
    fgmask = cv2.bitwise_and(frame, frame, mask=mask)
    smallfgmask = cv2.resize(fgmask, (300, 300))
    cv2.imshow('fgmask', smallfgmask)

    
    res = cv2.bitwise_and(frame,frame, mask= mask)

    gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    center = None
    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        if radius > 10:
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)

            if center[0] < 200:
                pan += 1
                pan_servo.angle = pan
                direction = "Left"
            elif center[0] > 440:
                pan -= 1
                pan_servo.angle = pan
                direction = "Right"
            else:
                direction = "Center"

            if center[1] < 110:
                tilt -= 1
                tilt_servo.angle = tilt
                
                direction = "Up"
            elif center[1] > 220:
                tilt += 1
                tilt_servo.angle = tilt
                
                direction = "Down"
            else:
                direction = "Center"

            cv2.putText(frame, f"Direction: {direction}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.imshow('Object Detection', frame)
  

    fps = int(1.0 / (time.time() - start_time))
    cv2.putText(frame, f"FPS: {fps}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    cv2.imshow('Object Detection', frame)
    

    if cv2.waitKey(2) & 0xFF == ord("q"):
        break

capture.release()
cv2.destroyAllWindows()
