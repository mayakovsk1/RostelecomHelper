import telebot
import os
from relevance import entry_relevance


TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN, parse_mode=None)


string1 = '''Зравствуйте, вас приветствует служба поддержки Ростелекома.
Пожалуйста введите ваш запрос...'''


string2 = '''Пожалуйста введите ваш запрос...'''


@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, string1)


@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.send_message(message.chat.id, string2)


@bot.message_handler(content_types=['text'])
def send_answer(message):
	bot.send_message(message.chat.id, '''Ожидайте, ваш запрос обрабатывается...''')
	answer = entry_relevance(str(message))
	bot.send_message(message.chat.id, answer)
	bot.send_message(message.chat.id, '''Пожалуйста введите ваш запрос...''')
	print('<<', message, '>>')
	print('{{', answer, '}}')
	print()


bot.polling()