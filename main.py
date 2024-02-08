#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import MenuButtonWebApp, WebAppInfo

from os import getenv
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message) -> None:
	keyboard_open = KeyboardButton(text="Открыть приложение", web_app=WebAppInfo(url="https://wolt.com"))
	markup = ReplyKeyboardMarkup(keyboard=[[keyboard_open]], resize_keyboard=True)
	await message.reply("Здравствуйте!", reply_markup=markup)

async def main() -> None:
	bot = Bot(token=getenv("TOKEN"), parse_mode=ParseMode.HTML)
	await dp.start_polling(bot)

if __name__ == "__main__":
	logging.basicConfig(level=logging.INFO, stream=sys.stdout)
	asyncio.run(main())
