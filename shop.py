from aiogram.utils import executor
from create_bot import dp




async def on_startup(_):
    print('Бот вышел в онлайн')

from handlers import client, admin, other

client.register_handler_client(dp)
admin.register_handler_admin(dp)
other.register_handler_other(dp) # последний


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

# if message.text == 'Привет':
#     await message.answer("И тебе привет!")
# await message.answer(message.text)
# await message.reply(message.text) # ответ под сообщением
# await bot.send_message(message.from_user.id,message.text) # в личку
