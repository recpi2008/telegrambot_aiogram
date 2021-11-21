import telebot
from config import token
from telebot import types

from datetime import datetime
from random import randint
import weather


def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start'])
    def welcome(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Рандомное число")
        item2 = types.KeyboardButton("Погода")

        markup.add(item1,item2)

        bot.send_message(message.chat.id,
                         "Добро пожаловать, <b>{0.first_name}</b>!\nЯ - <b>Eles</b>, бот созданный чтобы тебе помогать.".format(
                             message.from_user, bot.get_me()),
                         parse_mode='html', reply_markup=markup)

    @bot.message_handler(content_types=['text'])
    def lalala(message):
        if message.chat.type == 'private':

            if message.text == 'Рандомное число':
                bot.send_message(message.chat.id, str(randint(0, 100)))

            elif message.text == 'Погода':
                weather.send_weather(message)

            elif message.text in ['Таллин','Москва','Новосибирск']:
                bot.send_message(message.from_user.id, weather.weather(message.text.lower()))

            elif message.text == 'Меню':
                welcome(message)

            else:
                bot.send_message(message.chat.id, 'Я не знаю что ответить')

    bot.polling()

if __name__ == '__main__':
    telegram_bot(token)






