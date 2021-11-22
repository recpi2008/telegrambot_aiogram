from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db



# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятных покупок', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/Elesya_bot')


# @dp.message_handler(commands=['Режим_работы'])
async def shop_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Пн-Пт с 9:00 до 20:00, Сб-Вс c 11:00 до 20:00')


# @dp.message_handler(commands=['Расположение'])
async def shop_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Таллин, ул.Героев д.15') #, reply_markup=ReplyKeyboardRemove())

@dp.message_handler(commands=['Меню'])
async def shop_menu_command(message: types.Message):
    await sqlite_db.sql_read(message)

def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(shop_open_command, commands=['Режим_работы'])
    dp.register_message_handler(shop_place_command, commands=['Расположение'])
    dp.register_message_handler(shop_menu_command, commands=['Меню'])
