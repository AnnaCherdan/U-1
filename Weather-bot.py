# -*- coding: utf-8 -*-
import pyowm
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config

import telebot

config_dict = get_default_config()
config_dict['language'] = 'ru'

owm = OWM('3ef0b621ba1d0ad74912abfb7b925184', config_dict)
mgr = owm.weather_manager()

bot = telebot.TeleBot("5244368482:AAFAbWJltAxQMZJzAHjRS77KvOl7tGH6iL4")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	#bot.reply_to(message, message.text)
    #bot.send_message(message.chat.id, message.text)
    observation = mgr.weather_at_place( message.text )
    w = observation.weather
    temp = w.temperature('celsius')["temp"]

    answer = "В городе " + message.text + " сейчас " + w.detailed_status + "\n"
    answer += "Температура приблизительно: " + str(temp) + "\n\n"
    if temp < 0:
        answer += "Дубак! Оденься нормально, как сибиряк"
    elif temp < 10:
        answer += "Прохладно, одевайся тепло"
    elif temp < 20:
        answer += "Температура норм, не налегай на одежду."
    else:
        answer += "Загадочная погода..."

    bot.send_message(message.chat.id, answer)
bot.infinity_polling()
