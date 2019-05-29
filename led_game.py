import gpiozero as GPIO
import time
import asyncio
import random

buttonR = GPIO.Button(19)
buttonB = GPIO.Button(13)
led = GPIO.RGBLED(18, 23, 24, pwm=False)
red = GPIO.LED(25)
blue = GPIO.LED(12)
success = GPIO.LED(20)
global hit
hit = 0
print("Press the blue button for normal mode and then the red button for hardcore mode")
buttonB.wait_for_press()
mode = "normal"
buttonR.wait_for_press(timeout=3)
if buttonR.is_pressed:
	mode = "hardcore"
time.sleep(.5)
times = .5

def add_score():
	global hit
	print("Nice")
	success.on()
	time.sleep(.5)
	success.off()
	hit+=1

def check_press_red():
    if mode == "normal":
        if red.is_lit:
            add_score()
    else:
        if led.color == (1, 0, 0):
            add_score()

def check_press_blue():
	if mode == "normal":
		if blue.is_lit:
			add_score()
	else:
		if led.color == (0, 0, 1):
			add_score()


buttonR.when_pressed = check_press_red
buttonB.when_pressed = check_press_blue



async def light(interval, hit):
    if mode == "normal":
        random.choice([red.on, blue.on])()
        await asyncio.sleep(interval)
        red.off()
        blue.off()
    else:
        led.color = random.choice([(1, 0, 0), (0, 0, 1)]) 
        await asyncio.sleep(interval)
        led.off()
    
    
async def run(times, hit):    
	while times > .1:
		await asyncio.sleep(1)
		await light(times, hit)
		times -= .01
		

loop = asyncio.get_event_loop()
loop.run_until_complete(run(times, hit))
    
print(f"Score:  {hit}/{.4/.01}")
num = 5
while num > 0:
	success.on()
	time.sleep(.2)
	success.off()
	time.sleep(.2)
	num -=1
