#библиотеки, которые загружаем из вне
import telebot
TOKEN = '5233601666:AAH577Gz3DATSN70w9u_7JYnQ3j0LT3v2ko'

from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	button1 = types.KeyboardButton("👋 Поздороваться")
	button2 = types.KeyboardButton("❓ Узнать поближе")

	markup.add(button1, button2)

	bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я бот, созданный с любовью!".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
	if(message.text == "👋 Поздороваться"):
		sti = open('welcome.webp', 'rb')
		bot.send_sticker(message.chat.id, sti)
		bot.send_message(message.chat.id, text="Приветствую!Рад тебя здесь видеть!)")
	elif(message.text == "❓ Узнать поближе"):
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		button4 = types.KeyboardButton("🧡 Мой репозиторий")
		button5 = types.KeyboardButton("🌸 Мой сайт")
		button6 = types.KeyboardButton("🦄 Написать мне в личку")
		back = types.KeyboardButton("Вернуться в главное меню")
		markup.add(button4, button5, button6, back)
		bot.send_message(message.chat.id, text="Переходи по ссылкам", reply_markup=markup)
	elif(message.text == "🧡 Мой репозиторий"):
		bot.send_message(message.chat.id, 'https://github.com/KsuMironova-qa')
	elif message.text == "🌸 Мой сайт":
		bot.send_message(message.chat.id, 'https://ksumir.ru/')
	elif message.text == "🦄 Написать мне в личку":
		bot.send_message(message.chat.id, 'https://t.me/ksusha_mir')
	elif (message.text == "Вернуться в главное меню"):
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		button1 = types.KeyboardButton("👋 Поздороваться")
		button2 = types.KeyboardButton("❓ Узнать поближе")
		markup.add(button1, button2)
		bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
	else:
		bot.send_message(message.chat.id, text="Я тебя не понимаю")

bot.polling(none_stop=True)




#https://core.telegram.org/bots/api#available-methods