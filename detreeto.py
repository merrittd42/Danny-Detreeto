from playsound import playsound
from gpiozero import MotionSensor
import random
import time
#also requires pyobjc

pir = MotionSensor(4)

while True:
    if pir.motion_detected:
        print('Motion detected')
        excellentSoundbite = random.randrange(1, 3)
        playsound(f'{excellentSoundbite}.wav')
        time.sleep(15)
