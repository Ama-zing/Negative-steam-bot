import telebot
TOKEN = '986636286:AAGBmIYMoNmH_4VmWdNLHfBE42vi2VStaz4'
bot = telebot.TeleBot('986636286:AAGBmIYMoNmH_4VmWdNLHfBE42vi2VStaz4')

@bot.message_handler(content_types=["text"])
def handle_text(message):
	if message.text == "Hi":
		bot.send_message(message.from_user.id, "Здарова, уеба")

	elif message.text == "сам уеба" or message.text == "How are u?":
		bot.send_message(message.from_user.id, "ясно, клоун")

	else:
		bot.send_message(message.from_user.id, "Каво?")
bot.polling(none_stop=True, interval=0)