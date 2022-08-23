from adafruit_motorkit import MotorKit
from time import sleep
import board
import csv

c = open('magTestprograms.csv','w')

print('Start')

kit = MotorKit()


freq = 50   # hertz
period = 1/freq
step = period/4

while True:
    for i in range(10):
        kit.motor1.throttle = (0.1*i)
        sleep(step)

    for i in range(10):
        kit.motor1.throttle = 1 - (0.1*i)
        sleep(step)

    for i in range(10):
        kit.motor1.throttle = 0 - (0.1*i)
        sleep(step)

    for i in range(10):
        kit.motor1.throttle = -1 + (0.1*i)
        sleep(step)
