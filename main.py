from aiogram import Bot, Dispatcher, executor
from dotenv import load_dotenv
import os
from keyboards import *
from asia_pars import pars_asia
from aiogram.types import Message
from configs import *


load_dotenv()

TOKEN = os.getenv('TOKEN')

bot = Bot(TOKEN)

db = Dispatcher(bot)


@db.message_handler(commands=['start'])
async def command_start(message: Message):
    chat_id = message.chat.id
    await message.answer('Salom! Texnomartga xush kelibsiz!')
    await show_category_news(message)


async def show_category_news(message: Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, 'Kategoriyani tanlang: ', reply_markup=buttons_category())


@db.message_handler(content_types=['text'])
async def get_news_by_category(message: Message):
    chat_id = message.chat.id
    category_text = message.text
    get_news = pars_asia(get_value(category_text))

    for news in get_news:
        content = news.get('content')
        link = news.get('link')
        title = news.get('title')

        await message.answer(f'''
Link: {link}
Nomi:{title}''', reply_markup=button_link(link))


executor.start_polling(db)
