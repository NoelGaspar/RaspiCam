#!/usr/bin/python3
import json, signal, sys, os
import board
import neopixel
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import Servo

from picamera import PiCamera
from time import sleep
from datetime import datetime


SERVO_PIN = 12
RGB_PIN   = board.D18
NUM_LEDS  = 4
RGB_ORDER = neopixel.RGB
pigpio_factory = PiGPIOFactory()

class budaToken():
  def __init__(self, servo_pin = SERVO_PIN):
    self.RGB         = neopixel.NeoPixel(RGB_PIN,NUM_LEDS,brightness=0.2, auto_write=False,pixel_order=RGB_ORDER)
    # Start rpi camera
    self.camera = PiCamera()
    # Start servomotor
    self.servo = Servo(servo_pin, pin_factory = pigpio_factory)

  ''' Set status led state '''
  def statusLed(self, state):
    pass

  def flashLed(self, state):
    if state:
      self.RGB.fill((255,255,255))
      self.RGB.show()
    else:
      self.RGB.fill((0,0,0))
      self.RGB.show()
  
  ''' Triggers servomotor '''
  def servoPush(self):
    print("moving motors")
    self.servo.mid()
    sleep(1)
    self.servo.min()
    sleep(0.5)
    self.servo.mid()
    sleep(1)

  ''' Takes picture using rpi camera '''
  def takePhoto(self):
    path = 'data/pic.jpg'
    self.camera.capture(path)
    return path

  def takePhotoFull(self):
    self.servoPush()
    self.flashLed(1)
    self.takePhoto()
    self.flashLed(0)

if __name__ == "__main__":

  buda = budaToken()
  buda.takePhotoFull()
