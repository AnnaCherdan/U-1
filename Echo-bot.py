import telebot

bot = telebot.TeleBot("5244368482:AAFAbWJltAxQMZJzAHjRS77KvOl7tGH6iL4")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	#bot.reply_to(message, message.text)
    bot.send_message(message.chat.id, message.text)


bot.infinity_polling()