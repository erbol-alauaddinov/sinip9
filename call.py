from config import *
from key import *
from lesson_table import *

@dp.callback_query_handler()
async def call(call):
  cd = call.data
  et = call.message.edit_text
  ma = call.message.answer
  name = call.from_user.first_name
  id = call.from_user.id
  if cd=="back":
    await et(f"<b>🖐️Сәлем {name} . 🤖Бұл ботда 58-мектептің 9-сыныбы үшін Сабақ кестесі және електрон кітаптары бар</b>", reply_markup=key_start)
  elif cd=="ebook":
    await et("<b>📒Електрон кітаптар өзіңізге керегін таңдаң. \n❗Бұл кітаптар тек 9-сынып үшін.</b>")
    await bot.send_document(chat_id=id, document=f"{kb}/2")
    await bot.send_document(chat_id=id, document=f"{kb}/3")
    await bot.send_document(chat_id=id, document=f"{kb}/4")
    await bot.send_document(chat_id=id, document=f"{kb}/5")
    await bot.send_document(chat_id=id, document=f"{kb}/6")
    await bot.send_document(chat_id=id, document=f"{kb}/7")
    await bot.send_document(chat_id=id, document=f"{kb}/8")
    await bot.send_document(chat_id=id, document=f"{kb}/9")
    await bot.send_document(chat_id=id, document=f"{kb}/10")
    await bot.send_document(chat_id=id, document=f"{kb}/11")
    await bot.send_document(chat_id=id, document=f"{kb}/12")
    await bot.send_document(chat_id=id, document=f"{kb}/13")
    await bot.send_document(chat_id=id, document=f"{kb}/14")
    await bot.send_document(chat_id=id, document=f"{kb}/15")
    await bot.send_document(chat_id=id, document=f"{kb}/16")
    await bot.send_document(chat_id=id, document=f"{kb}/17")
    await bot.send_document(chat_id=id, document=f"{kb}/18")
    await call.message.answer("<b>📒Бұл кітаптар тек 9-сынып үшін.</b>", reply_markup=key_back)
  
  
  elif cd=="lt":
    await et("<b>📃Сабақ кестесі. Күнді таңдаң.</b>", reply_markup=key_lt)
  elif cd=="k1":
    await et(KUN_1, reply_markup=key_back1)
  elif cd=="k2":
    await et(KUN_2, reply_markup=key_back1)
  elif cd=="k3":
    await et(KUN_3, reply_markup=key_back1)
  elif cd=="k4":
    await et(KUN_4, reply_markup=key_back1)
  elif cd=="k5":
    await et(KUN_5, reply_markup=key_back1)
  elif cd=="k6":
    await et(KUN_6, reply_markup=key_back1)
  elif cd=="info":
    await et("<b>🤖Бот туралы.\n👨‍💻Бағдарламашы: @erbol_alauaddinov\n🖥️Бағдарламалау тілі: PYTHON\n⬜ФРЭИМОРК: Aiogram</b>", reply_markup=key_back)



