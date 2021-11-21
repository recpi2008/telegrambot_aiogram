import config
import requests
import telebot
from telebot import types
from bs4 import BeautifulSoup as BS

bot = telebot.TeleBot(config.token)


def send_weather(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('Таллин')
    itembtn2 = types.KeyboardButton('Москва')
    # itembtn3 = types.KeyboardButton('ННовгород')
    itembtn4 = types.KeyboardButton('Новосибирск')
    itembtn5 = types.KeyboardButton('Меню')

    markup.add(itembtn1, itembtn2, itembtn4, itembtn5)
    bot.send_message(message.chat.id,
                           "Какой город погода?", reply_markup=markup)



def weather(city):
    r = requests.get(f'https://sinoptik.ua/погода-{city}')
    html = BS(r.content, 'html.parser')
    # bot = telebot.TeleBot(config.token)

    for el in html.select('#content'):
        t_min = el.select('.temperature .min')[0].text
        t_max = el.select('.temperature .max')[0].text
        text = el.select('.wDescription .description')[0].text
    return (f"{city.title()} - погода на сегодня:\n {t_min}, {t_max}\n {text}")
