import RPi.GPIO as gpio
import time

def init():
    '''setup GPIO Pins'''
    gpio.setmode(gpio.BCM)
    gpio.setup(26, gpio.OUT)
    gpio.setup(19, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(12, gpio.OUT)

def reverse(tf):
    '''move backwards'''
    init()
    gpio.output(26, True)
    gpio.output(19, False)
    gpio.output(13, True) 
    gpio.output(12, False)
    time.sleep(tf)
    gpio.cleanup()

def forward(tf):
    '''move forwards'''
    init()
    gpio.output(26, False)
    gpio.output(19, True)
    gpio.output(13, False) 
    gpio.output(12, True)
    time.sleep(tf)
    gpio.cleanup()

def left(tf):
    '''pivot left'''
    init()
    gpio.output(26, False)
    gpio.output(19, True)
    gpio.output(13, True) 
    gpio.output(12, False)
    time.sleep(tf)

def right(tf):
    '''pivot right'''
    init()
    gpio.output(26, True)
    gpio.output(19, False)
    gpio.output(13, False) 
    gpio.output(12, True)
    time.sleep(tf)
    gpio.cleanup()

def stop():
    '''dead stop'''
    init()
    gpio.output(26, False)
    gpio.output(19, False)
    gpio.output(13, False) 
    gpio.output(12, False)
    gpio.cleanup()
print ("forward")
forward(1)
print ("backward")
reverse(1)
print ("left")
left(1)
print ("right")
right(1)
print ("stop")
stop
