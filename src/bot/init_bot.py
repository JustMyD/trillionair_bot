import os, emoji

from aiogram import Bot, Dispatcher, types

from dotenv import load_dotenv

load_dotenv()
bot_token = os.getenv('API_TOKEN')
calendar_url = os.getenv('CALENDAR_URL')
members_list_url = os.getenv('MEMBERS_LIST')

bot = Bot(token=bot_token)
dp = Dispatcher(bot)

'''Тест'''

@dp.message_handler(commands='test')
async def test(message: types.Message):
    await message.answer(emoji.emojize('test :calendar:'))

@dp.message_handler(commands='calendar')
async def start_message(message: types.Message):
    inline_keyboard = types.InlineKeyboardMarkup(row_width=1, inline_keyboard=[
        [types.InlineKeyboardButton(emoji.emojize('Календарь :calendar:'), url=calendar_url)]
    ])
    await message.delete()
    await message.answer(text=emoji.emojize(':pushpin:\nПредстоящие выступления Триллионеров'),
                         reply_markup=inline_keyboard)

@dp.message_handler(commands='list')
async def end_message(message: types.Message):
    inline_keyboard = types.InlineKeyboardMarkup(row_width=1, inline_keyboard=[
        [types.InlineKeyboardButton(emoji.emojize('Список :page_with_curl:'), url=members_list_url)]
    ])
    await message.delete()
    await message.answer(text=emoji.emojize(':pushpin:\nУчастники "Мой Проект"'),
                         reply_markup=inline_keyboard)
