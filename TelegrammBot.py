import telebot
TOKEN = '986636286:AAGBmIYMoNmH_4VmWdNLHfBE42vi2VStaz4'
bot = telebot.TeleBot('986636286:AAGBmIYMoNmH_4VmWdNLHfBE42vi2VStaz4')

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

@bot.message_handler(content_types=["text"])
def handle_text(message):
	if message.text == "/start":
		bot.send_message(message.from_user.id, "Здарова, клоун! Я тупой бот, ничего не умею, как и ты)) KEKW")

	elif message.text == "/help" or message.text == "help":
		bot.send_message(message.from_user.id, "1) /start - приветствие")

	else:
		bot.send_message(message.from_user.id, "Чаво? Ничего не понял. Напиши /help или help, чтобы узнать команды.")
bot.polling(none_stop=True, interval=0)