import RPi.GPIO as GPIO
from time import sleep

# Set up GPIO to read in pin 7
# (where we've connected our PIR)
GPIO.setmode(GPIO.BCM)
PIR_PIN = 7
GPIO.setup(PIR_PIN, GPIO.IN)

try:
    print "PIR Module Test (CTRL+C to exit)"
    sleep(2)
    print "Ready"
    
    # Listen indefinitely
    while True:
        if GPIO.input(PIR_PIN):
            print "Alert! Motion detected!"
            # Pause for action
            sleep(6)
        else:
            print "Motion not detected!"
        sleep(1)
        
except KeyboardInterrupt:
    print "Exiting!"
    # Release GPIO on exit
    GPIO.cleanup()