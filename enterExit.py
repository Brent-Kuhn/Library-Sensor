import RPi.GPIO as GPIO
import time

import pygame.mixer
from pygame.mixer import Sound

sensorCalibration = 35

pygame.init()
pygame.mixer.init()
enterSound = pygame.mixer.Sound("/home/pi/Music/analog-watch-alarm_daniel-simion.wav")
exitSound = pygame.mixer.Sound("/home/pi/Music/fire-truck-air-horn_daniel-simion.wav")

GPIO.setmode(GPIO.BCM)

def enter():
    GPIO.setmode(GPIO.BCM)
    TRIG1 = 23
    ECHO1 = 24

    print("Distance 1 Measurement In Progress")

    GPIO.setup(TRIG1,GPIO.OUT)
    GPIO.setup(ECHO1,GPIO.IN)

    GPIO.output(TRIG1, 0)
    print("Waiting for sensor to settle")
    time.sleep(.1)

    GPIO.output(TRIG1, 1)
    time.sleep(0.00001)
    GPIO.output(TRIG1, 0)

    while GPIO.input(ECHO1) == 0:
            pass
    pulse_start = time.time()

    while GPIO.input(ECHO1) == 1:
            pass
    pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = distance//1

    print('Distance:', distance, 'cm')

    GPIO.cleanup()
    
    return(distance)

def exit():
    GPIO.setmode(GPIO.BCM)
    TRIG2 = 25
    ECHO2 = 8

    print("Distance 2 Measurement In Progress")

    GPIO.setup(TRIG2,GPIO.OUT)
    GPIO.setup(ECHO2,GPIO.IN)

    GPIO.output(TRIG2, 0)
    print("Waiting for sensor to settle")
    time.sleep(.1)

    GPIO.output(TRIG2, 1)
    time.sleep(0.00001)
    GPIO.output(TRIG2, 0)

    while GPIO.input(ECHO2) == 0:
            pass
    pulse_start = time.time()

    while GPIO.input(ECHO2) == 1:
            pass
    pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = distance//1

    print('Distance:', distance, 'cm')

    GPIO.cleanup()
    
    return(distance)

while True:
    enterDistance = enter()
    time.sleep(.5)
    exitDistance = exit()
    time.sleep(.5)
    if enterDistance < sensorCalibration:
        enterSound.play()
        time.sleep(1)
        enterSound.stop()
        time.sleep(10)
    if exitDistance < sensorCalibration:
        exitSound.play()
        time.sleep(1)
        exitSound.stop()
        time.sleep(10)