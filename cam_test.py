from picamera import PiCamera
from time import sleep

# Initialize the camera
camera = PiCamera()

# Camera configuration (optional, can be customized)
camera.resolution = (1920, 1080)  # Set to your desired resolution
camera.framerate = 30

try:
    # Start the camera preview
    camera.start_preview()
    
    # Display the preview indefinitely (or for a desired duration)
    sleep(10)  # Change 10 to the number of seconds you want the preview displayed

finally:
    # Stop the camera preview
    camera.stop_preview()
    camera.close()
