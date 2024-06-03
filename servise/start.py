from aiogram import types
from bot import dp  # Import the Dispatcher object from the main bot module
from keyboard.defualt import wrapper_regions_buttons

@dp.message_handler(text="/start")
async def bot_start(message: types.Message):
    await message.answer("Assalomu aleykum. Namoz vaqtlari botga xush kelibsiz. Ushbu bot \nyordamida hohlagan viloyatdagi namoz vaqtlarini bilib olishingiz\n mumkin.\n\nBarcha ma'lumotlar islom.uz saytidan olinadi!.",reply_markup=wrapper_regions_buttons)
