from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

key_start = InlineKeyboardMarkup().add(InlineKeyboardButton("📒ЕЛЕКТРОН КІТАПТАР", callback_data="ebook"), InlineKeyboardButton("📃САБАҚ КЕСТЕСІ", callback_data="lt")).add(InlineKeyboardButton("🤖БОТ ТУРАЛЫ", callback_data="info"))
key_back = InlineKeyboardMarkup().add(InlineKeyboardButton("🔙АРҚА", callback_data="back"))

key_lt = InlineKeyboardMarkup().add(InlineKeyboardButton("1️⃣", callback_data="k1"), InlineKeyboardButton("2️⃣", callback_data="k2"), InlineKeyboardButton("3️⃣", callback_data="k3")).add(InlineKeyboardButton("4️⃣", callback_data="k4"), InlineKeyboardButton("5️⃣", callback_data="k5"), InlineKeyboardButton("6️⃣", callback_data="k6")).add(InlineKeyboardButton("🔙АРҚА", callback_data="back"))
key_back1 = InlineKeyboardMarkup().add(InlineKeyboardButton("🔙АРТҚА", callback_data="lt"))