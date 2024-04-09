
# Object Tracking with Servo Motors On jetson nano 

This code demonstrates object tracking using computer vision techniques and controls servo motors to track the detected object's movement. It uses OpenCV for image processing and the Adafruit ServoKit library for controlling the servos.

## Prerequisites

- Python 3.x
- OpenCV (cv2) library
- numpy library
- adafruit_servokit library

## Hardware Setup

1. Connect the servos to the appropriate channels on your servo controller board. The code assumes the pan servo is connected to channel 0 and the tilt servo to channel 1. Adjust these values accordingly if your setup differs.

## Installation

1. Install the required libraries:
   ```shell
   pip install opencv-python numpy adafruit-circuitpython-servokit
   ```

## Usage

1. Run the code:
   ```shell
   python object_tracking.py
   ```

2. The code will open a video stream from the default camera (index 0). If you have multiple cameras connected, you may need to adjust the `VideoCapture` index accordingly.

3. The program will track a purple object in the video feed. Adjust the `lower_purple` and `upper_purple` values to match the color range of your desired object.

4. The program will display two windows: one showing the binary mask of the tracked object and another showing the tracked object with bounding circles. The window titled "Object Detection" will also display the direction of the object's movement.

5. The servos will adjust their angles to track the object's movement. The pan servo will move left or right based on the object's horizontal position, and the tilt servo will move up or down based on the object's vertical position.

6. Press the 'q' key to quit the program.

## Customization

- Adjust the values for `lower_purple` and `upper_purple` to track objects of different colors. You can use an image editing software to determine the appropriate color range for your target object.

- Modify the minimum radius threshold (`if radius > 10`) to change the minimum size of the object to be tracked.

- Adjust the pan and tilt servo angle increments (`pan += 1`, `pan -= 1`, `tilt -= 1`, `tilt += 1`) to change the tracking sensitivity.

- Customize the font, position, and color of the text overlay in the `cv2.putText` function calls.

## Troubleshooting

- If the servos are not responding or behaving erratically, ensure that the servo controller board is properly connected to the Jetson Nano and the power supply.

- If the video stream does not open or displays an error, make sure that the camera is connected correctly and accessible by OpenCV.

