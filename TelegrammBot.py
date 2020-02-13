import requests
from bs4 import BeautifulSoup
import telebot
TOKEN = '986636286:AAGBmIYMoNmH_4VmWdNLHfBE42vi2VStaz4'
bot = telebot.TeleBot('986636286:AAGBmIYMoNmH_4VmWdNLHfBE42vi2VStaz4')

@bot.message_handler(commands=['start', 'help'])
def handle_text(message):
	if message.text == "/start":
		bot.send_message(message.from_user.id, "Здарова, клоун! Я тупой бот, но уже даже что-то умею KEKW")

	elif message.text == "/help" or message.text == "help":
		bot.send_message(message.from_user.id, "1) /start - приветствие \n2) /stat - кс го статистика \n3) /nickname - украсить ваш ник в steam")

@bot.message_handler(commands=['stat'])
def stat_cs(message):
	msg = bot.send_message(message.from_user.id, "Введите свой стим-id")
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

@bot.message_handler(commands=['nickname'])
def steam_nickname(message):
	msg = bot.send_message(message.from_user.id, "Введите свой ник в steam (ENGLISH ONLY). Ща мы его украсим")
	bot.register_next_step_handler(msg , create_nickname)

def magic(letter):
	if letter == 'A' or letter =='a':
		return 'À'
	elif letter == 'B' or letter == 'b':
		return 'ß'
	elif letter == 'C' or letter == 'c':
		return 'Ĉ'
	elif letter == 'D' or letter == 'd':
		return 'Ƿ'
	elif letter == 'E' or letter == 'e':
		return 'Ɇ'
	elif letter == 'F' or letter == 'f':
		return 'Ƒ'
	elif letter == 'H' or letter == 'h':
		return 'Ȟ'
	elif letter == 'K' or letter ==	'k':
		return 'Ǩ'
	elif letter == 'G' or letter == 'g':
		return 'Ĝ'
	elif letter == 'R' or letter ==	'r':
		return 'Ř'
	elif letter == 'U' or letter == 'u':
		return 'Ũ'
	elif letter == 'T' or letter == 't':
		return 'Ţ'
	elif letter == 'O' or letter == 'o':
		return 'Ǿ'
	elif letter == 'W' or letter == 'w':
		return 'Ŵ'
	elif letter == 'S' or letter == 's':
		return 'Ş'
	elif letter == 'Z' or letter == 'z':
		return 'Ź'
	elif letter == 'Y' or letter == 'y':
		return 'Ƴ'							
	else:
		return letter	
		

def create_nickname(message):
	chat_id = message.chat.id
	current_nickname = message.text
	nick_length=len(current_nickname)
	for i in range(0,nick_length):
		final_nickname=final_nickname+magic(current_nickname[i])
	bot.send_message(message.from_user.id, final_nickname)	


bot.polling(none_stop=True, interval=0)
