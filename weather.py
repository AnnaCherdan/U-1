# -*- coding: utf-8 -*-
import pyowm
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
owm = OWM('3ef0b621ba1d0ad74912abfb7b925184')# , language = "ru"
mgr = owm.weather_manager()

place = input("Where are you from?: ")

observation = mgr.weather_at_place('place')
w = observation.weather

temp = w.temperature('celsius')["temp"]

print("In the city " + place + " now is " + w.detailed_status)
print("The temperature in the city now approximately: " + str(temp))

if temp < 10:
    print("Прохладно, одевайся тепло")
elif temp < 20:
    print("Температура норм, не налегай на одежду.")
else:
    print("Загадочная погода...")


#print(w)

