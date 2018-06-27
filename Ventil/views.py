import RPi.GPIO as GPIO
import time

d=0
fanPin = 8
leds = [3,5,11,29]
ledStat = {'0': [0,0,0,0],'25': [1,0,0,0], '50': [0,1,0,0], '75': [0,0,1,0], '100': [0,0,0,1]}
GPIO.setmode(GPIO.BOARD)
GPIO.setup(fanPin, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
from django.shortcuts import render

pwm = GPIO.PWM(fanPin, 50)

def showbutton(request):
    if(request.method=="GET"):
        return render(request, "ventil_template.html",{"msg":"Start fan"})
    elif(request.method=="POST"):
        global d
        global ledStat
        global leds
        pwm.start(0)
        if d>100:
            d=0
        pwm.ChangeDutyCycle(d)
        GPIO.output(leds, ledStat.get(str(d)))
        d=d+25
        return render(request, "ventil_template.html",{"msg": "Fan speed: " + str(d-25) + "%"})

