from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

updater = Updater(token='986636286:AAGBmIYMoNmH_4VmWdNLHfBE42vi2VStaz4')
dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

def start(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text='Здарова, клоун! Я тупой бот, ничего не умею, как и ты)) KEKW')

start_handler = CommandHandler('start', start)
restart_handler=CommandHandler('restart', restart)
text_message_handler = MessageHandler(Filters.text, textMessage)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(restart_handler)
dispatcher.add_handler(text_message_handler)
updater.start_polling(clean=True)
updater.idle()