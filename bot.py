import telebot

import random

# import bot telegram token
from tok import tok

# variables
isRunning = True

botVocabulary = ["Ага", "Ясно", "Каеф"]
botStickos = [
	"CAACAgIAAxkBAAECqPthA9OsR4mLQnsx8fKQr8SETKc3nQACWQADwZxgDGzL6LPYs46GIAQ",
	"CAACAgIAAxkBAAECqP1hA9PK_qJ-2NRQvDPChZIsRauzeQACXgADwZxgDNnDkE2surhQIAQ",
	"CAACAgIAAxkBAAECqP9hA9Pj9xkV82Q2j-3zU-ZEGn2T3QACXwADwZxgDC6UZ2vbTXvUIAQ",
]

# create bot
bot = telebot.TeleBot(tok())

# run bot
bot.polling(none_stop=True)

#handlers
@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
	if not isRunning:
		chat_id = message.chat.id
		msg = bot.send_message(chat_id, "Привет, я - Бот! Как дела?")
		bot.register_next_step_handler(msg, howAreYou)
		isRunning = True
		
def howAreYou(message):
	chat_id = message.chat.id
	text = message.text.lower()
	
	if text.find("хорошо") != -1:
		bot.send_message(chat_id, "Так держать!")
	elif text.find("плохо") != -1:
		bot.send_message(chat_id, "Ну, не расстраивайся")
	else :
		bot.send_message(chat_id, "Понятненько")

@bot.message_handler(content_types=['text'])		
def text_handler(message):
	chat_id = message.chat.id
	
	bot.send_message(chat_id, random.choice(botVocabulary))

@bot.message_handler(content_types=['photo'])
def pic_handler(message):	
	chat_id = message.chat.id
	
	bot.send_message(chat_id, "Красиво")
		
@bot.message_handler(content_types=['sticker'])
def sticker_handler(message):	
	chat_id = message.chat.id
	
	bot.send_sticker(chat_id, random.choice(botStickos))

