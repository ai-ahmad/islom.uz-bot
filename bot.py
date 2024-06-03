import logging
import asyncio
from aiogram import Bot, Dispatcher, executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
API_TOKEN = '7421048776:AAFB6Psfd_kTLW-tLDRigAE-Lw9AB4eL_iY'
logging.basicConfig(level=logging.DEBUG)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)  

from servise.start import *
from servise.region import *

async def main():
    await dp.start_polling()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
