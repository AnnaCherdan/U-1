# -*- coding: utf-8 -*-
import pyowm
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['lang'] = 'ru'

owm = OWM('3ef0b621ba1d0ad74912abfb7b925184', config_dict)
mgr = owm.weather_manager()

place = input("Какой город вас интересует?: ")

observation = mgr.weather_at_place('place')
w = observation.weather

temp = w.temperature('celsius')["temp"]

print("В интересном вам городе " + place + " сейчас " + w.detailed_status)
print("Приблизительная температура: " + str(temp))

if temp < 10:
    print("Прохладно, одевайся тепло")
elif temp < 20:
    print("Температура норм, не налегай на одежду.")
else:
    print("Загадочная погода...")


#print(w)

