from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os

from dotenv import load_dotenv

load_dotenv(r'/home/eles/projects/telegram_bot_shop/.env')
token = os.getenv("TOKEN",None)

storage = MemoryStorage()

bot = Bot(token=token)
dp = Dispatcher(bot, storage=storage)
