import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
#GPIO.setmode(GPIO.BOARD)

print("Demonstration: Mission Impossible Made Possible")
print("Press any key to exit")
TRIG = 23
ECHO = 24
# LED1 = 17, LED2 = 27, LED3 = 22, LED4 = 5, LED5 = 6
led_pins = [17,27,22,5,6]

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
	time.sleep(0.00001) #send signal
	GPIO.output(TRIG, GPIO.LOW)

	while GPIO.input(ECHO)==0:
		start_time = time.time()
			
	while GPIO.input(ECHO)==1:
		end_time = time.time()

	duration = end_time - start_time
	distance = round(duration * (34320/2), 2) #speed of sound = 343.2 m/s
	
	return distance
	
def set_leds(dist):

	#turn off all the leds
	for led in led_pins:
		GPIO.output(led, GPIO.LOW)
	
	#calculate the number of leds and turn them on respectively	
	for led in led_pins[:((dist//60)+1)]: 
		GPIO.output(led, GPIO.HIGH)
	

try:
	while True:
		distance = get_distance()
		print("Distance:",distance,"cm")
		set_leds(distance)
		time.sleep(1)

except KeyboardInterrupt:
	print("Program stopped by user")
	GPIO.cleanup()