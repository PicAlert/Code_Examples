from picamera import PiCamera
from time import sleep

camera = PiCamera()

# Rotate as needed
camera.rotation = 0

# Give at least 2 seconds to adjust
sleep(2)

# Take a still picture and save to file:
camera.capture('test_pic.png')

# Record video and save to file:
camera.start_recording('test_vid.h264')
sleep(10)
camera.stop_recording()

# Close camera
camera.close()