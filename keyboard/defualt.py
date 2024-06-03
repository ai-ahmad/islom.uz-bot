from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton
from aiogram import types
from aiogram.types.web_app_info import WebAppInfo
wrapper_regions_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Toshkent"),
            KeyboardButton(text="Qo'qon"),
            KeyboardButton(text="Andijon"),
        ],
        [
            KeyboardButton(text="Buxoro"),
            KeyboardButton(text="Guliston"),
            KeyboardButton(text="Samarqand"),
        ],
        [
            KeyboardButton(text="Namangan"),
            KeyboardButton(text="Navoiy"),
            KeyboardButton(text="Jizzax"),
        ],
        [
            KeyboardButton(text="Nukus"),
            KeyboardButton(text="Qarshi"),
            KeyboardButton(text="Xiva")
        ],
    ],
    resize_keyboard=True
)
 

wrapper_keyboards_home_pages = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="☪️ Bugungi namoz vaqtlari"),
            KeyboardButton(text="📝 Joyni ozgaritirish")
        ],
        [
            KeyboardButton(text="☪️ Islom haqida ko'proq ma'lumot olish",web_app=types.WebAppInfo(url=f'https://www.islom.uz/'),)
        ]
    ],
    resize_keyboard=True
)