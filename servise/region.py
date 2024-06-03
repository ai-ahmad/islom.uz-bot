from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from bot import dp
import requests
import sqlite3
import schedule
import time
from keyboard.defualt import wrapper_keyboards_home_pages,wrapper_regions_buttons
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, user_name TEXT, chat_id TEXT, user_region TEXT)")


def get_namoz_vaqti(region):
    url = f"https://islomapi.uz/api/present/day?region={region}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to retrieve data. Status code:", response.status_code)
        return None

def text_soat(data):
    return (
        f"<b>Bugun {data['date']}-({data['weekday']}).</b>\n\n"
        f"<b>☪️ Namoz vaqtlari:</b>\n\n"
        f"Bomdod: {data['times']['tong_saharlik']}\n"
        f"Quyosh: {data['times']['quyosh']}\n"
        f"Peshin: {data['times']['peshin']}\n"
        f"Asr: {data['times']['asr']}\n"
        f"Shom(Iftor): {data['times']['shom_iftor']}\n"
        f"Xufton: {data['times']['hufton']}\n\n"
        f"<b>Manba: <a href=\"https://islom.uz/\">islom.uz</a></b>"
    )

def save_user_region(user_id, user_name, chat_id, user_region):
    cursor.execute("INSERT OR REPLACE INTO users (user_id, user_name, chat_id, user_region) VALUES (?, ?, ?, ?)",
                   (user_id, user_name, chat_id, user_region))
    conn.commit()

async def get_region(message: types.Message, region_name: str):
    data = get_namoz_vaqti(region_name)
    if data is not None:
        text = text_soat(data=data)
        await message.answer(f"<b>{region_name} namoz vaqti:</b>\n{text}", parse_mode="HTML",reply_markup=wrapper_keyboards_home_pages)
        save_user_region(message.from_user.id, message.from_user.username, message.chat.id, region_name)
    else:
        await message.answer("Ma'lumotlarni olishda xatolik yuz berdi.")

@dp.message_handler(text="Toshkent")
async def get_toshkent(message: types.Message):
    await get_region(message, "Toshkent")

@dp.message_handler(text="Qo'qon")
async def get_qoqon(message: types.Message):
    await get_region(message, "Qo'qon")

@dp.message_handler(text="Andijon")
async def get_andijon(message: types.Message):
    await get_region(message, "Andijon")

@dp.message_handler(text="Buxoro")
async def get_buxoro(message: types.Message):
    await get_region(message, "Buxoro")

@dp.message_handler(text="Guliston")
async def get_guliston(message: types.Message):
    await get_region(message, "Guliston")

@dp.message_handler(text="Samarqand")
async def get_samarqand(message: types.Message):
    await get_region(message, "Samarqand")

@dp.message_handler(text="Namangan")
async def get_namangan(message: types.Message):
    await get_region(message, "Namangan")

@dp.message_handler(text="Navoiy")
async def get_navoiy(message: types.Message):
    await get_region(message, "Navoiy")

@dp.message_handler(text="Jizzax")
async def get_jizzax(message: types.Message):
    await get_region(message, "Jizzax")

@dp.message_handler(text="Nukus")
async def get_nukus(message: types.Message):
    await get_region(message, "Nukus")

@dp.message_handler(text="Qarshi")
async def get_qarshi(message: types.Message):
    await get_region(message, "Qarshi")

@dp.message_handler(text="Xiva")
async def get_xiva(message: types.Message):
    await get_region(message, "Xiva")

@dp.message_handler(text="☪️ Bugungi namoz vaqtlari")
async def get_bugungi_namoz_vaqti(message: types.Message):
    data = cursor.execute("SELECT user_region FROM users WHERE chat_id = ?", (message.chat.id,)).fetchall()
    for i in data:
        await get_region(message,i[0])

@dp.message_handler(text="📝 Joyni ozgaritirish")
async def get_joyni_ozgaritirish(message: types.Message):
    await message.answer("Joyni ozgaritish uchun viloyatni tanlang", reply_markup=wrapper_regions_buttons)

