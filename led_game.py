import gpiozero as GPIO
import time
import asyncio
import random

buttonR = GPIO.Button(19)
buttonB = GPIO.Button(13)
led = GPIO.RGBLED(18, 23, 24, pwm=False)
success = GPIO.LED(20)
global hit
hit = 0
print("Press the button to begin")
buttonB.wait_for_press()
time.sleep(.5)
times = .5
def check_press_red():
    global hit
    if led.color == (1, 0, 0):
        print("Nice")
        success.on()
        time.sleep(.5)
        success.off()
        hit+=1

def check_press_blue():
	global hit
	if led.color == (0, 0, 1):
		print("Nice")
		success.on()
		time.sleep(.5)
		success.off()
		hit+=1
buttonR.when_pressed = check_press_red
buttonB.when_pressed = check_press_blue



async def light(interval, hit):
    led.color = random.choice([(1, 0, 0), (0, 0, 1)]) 
    await asyncio.sleep(interval)
    led.off()
    
    
async def run(times, hit):    
	while times > .05:
		await asyncio.sleep(1)
		await light(times, hit)
		times -= .01
		

loop = asyncio.get_event_loop()
loop.run_until_complete(run(times, hit))
    
print(hit)
num = 5
while num > 0:
	success.on()
	time.sleep(.2)
	success.off()
	time.sleep(.2)
	num -=1
