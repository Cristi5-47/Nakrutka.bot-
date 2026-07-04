from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🛒 Xizmatlar"), KeyboardButton(text="💳 Hisobni to'ldirish")],
        [KeyboardButton(text="📦 Buyurtmalar"), KeyboardButton(text="👤 Profil")],
        [KeyboardButton(text="☎️ Yordam")]
    ],
    resize_keyboard=True
)
