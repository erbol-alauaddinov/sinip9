from config import *
from aiogram import executor, types
from key import *

@dp.message_handler(commands=["start"])
async def start(message):
  id = message.from_user.id
  name = message.from_user.first_name
  await message.answer(f"<b>🖐️Сәлем {name} . 🤖Бұл ботда 58-мектептің 9-сыныбы үшін Сабақ кестесі және електрон кітаптары бар</b>", reply_markup=key_start)

from call import call

if __name__=="__main__":
  executor.start_polling(dp, skip_updates=True)