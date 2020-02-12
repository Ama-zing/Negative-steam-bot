import requests
from bs4 import BeautifulSoup
import telebot
TOKEN = '986636286:AAGBmIYMoNmH_4VmWdNLHfBE42vi2VStaz4'
bot = telebot.TeleBot('986636286:AAGBmIYMoNmH_4VmWdNLHfBE42vi2VStaz4')

import logging
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

@bot.message_handler(commands=['start', 'help'])
def handle_text(message):
	if message.text == "/start":
		bot.send_message(message.from_user.id, "Здарова, клоун! Я тупой бот, но уже даже что-то умею KEKW")

	elif message.text == "/help" or message.text == "help":
		bot.send_message(message.from_user.id, "1) /start - приветствие \n2) /stat - кс го статистика")

@bot.message_handler(commands=['stat'])
def stat_cs(message):
	msg =bot.send_message(message.from_user.id, "Введите свой стим-id")
	bot.register_next_step_handler(msg , steamid)

def steamid(message):

	chat_id = message.chat.id
	id = message.text
	page = requests.get('https://convars.com/csgostats/ru/' + id)
	page.encoding = 'utf-8'
	soup = BeautifulSoup(page.text, 'html.parser')
	a = soup.select("#round11 > div:nth-child(5)")
	text = str(a)
	textend = []
	slova = ['Убийств: ', 'Смертей: ', 'Матчей: ', 'Раунды: ', 'Время: ', 'КД: ']
	i = text.find("<")
	streng = ''
	while i != (-1):
		i = text.find('''fff;">''')
		text = text[(i + 6):]
		i = text.find("<")
		textend.append(text[0:i])
		i = text.find('''fff;">''')
	for j in range(len(textend)):
		streng = slova[j] + textend[j]
		bot.send_message(message.from_user.id, streng)
	kdratio = slova[5] + str(round(int(textend[0])/int(textend[1]), 2))
	bot.send_message(message.from_user.id, kdratio)

bot.polling(none_stop=True, interval=0)
