from pk import take_photo
import RPi.GPIO as GPIO

if __name__ == "__main__":
    # Set up GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    # Take a photo when the button is pressed
    while True:
        input_state = GPIO.input(18)
        if input_state == False:
            take_photo(path)
            time.sleep(0.2)