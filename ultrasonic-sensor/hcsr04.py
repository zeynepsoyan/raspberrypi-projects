import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

print("Demonstration: Mission Impossible Made Possible")
print("Press any key to exit")
TRIG = 23
ECHO = 24
# LED1 = 17, LED2 = 27, LED3 = 22, LED4 = 5, LED5 = 6
led_pins = [17, 27, 22, 5, 6]

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

for led in led_pins:
    GPIO.setup(led, GPIO.OUT)


def get_distance():

    GPIO.output(TRIG, GPIO.LOW)
    print("Waiting for sensor to settle...")
    time.sleep(2)
    print("Calculating distance...")

    GPIO.output(TRIG, GPIO.HIGH)
    time.sleep(0.00001)  # send signal
    GPIO.output(TRIG, GPIO.LOW)

    while GPIO.input(ECHO) == 0:
        start_time = time.time()

    while GPIO.input(ECHO) == 1:
        end_time = time.time()

    duration = end_time - start_time
    distance = round(duration * (34320/2), 2)  # speed of sound = 343.2 m/s

    return int(distance)


def turn_leds_off():

    for led in led_pins:
        GPIO.output(led, GPIO.LOW)


def light_leds(dist):

    # calculate the number of leds and turn them on respectively
    for led in led_pins[:(dist//20)]:
        GPIO.output(led, GPIO.HIGH)


def blink_leds(leds):

    for _ in range(5):
        for led in leds:
            GPIO.output(led, GPIO.HIGH)
        time.sleep(0.2)
        for led in leds:
            GPIO.output(led, GPIO.LOW)


try:
    while True:
        distance = get_distance()
        if distance < 2 or distance > 400:
            print("Out of range")
        else:
            print("Distance:", distance, "cm")
            turn_leds_off()

            if distance < 20:
                blink_leds(led_pins[0])
            elif distance > 360:
                blink_leds(led_pins)
            else:
                light_leds(distance)
            time.sleep(1)

except KeyboardInterrupt:
    print("Program stopped by user")
    GPIO.cleanup()
