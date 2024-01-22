from pk import take_photo
import RPi.GPIO as GPIO
import time

if __name__ == "__main__":
    # Set up GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    print("Waiting for button press...")

    # Take a photo when the button is pressed
    while True:
        input_state = GPIO.input(17)
        if input_state == False:
            take_photo()
            time.sleep(0.2)
            print("Photo taken!")