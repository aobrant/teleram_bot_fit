from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from aiogram.utils.helper import Helper, HelperMode, ListItem

import keyboards as kb
from aiogram.utils.markdown import text

help_message = text(
    "/start",
    "/help",
    "/remove",
    sep="\n"
)


class MenuStates(Helper):
    mode = HelperMode.snake_case


async def handler_start(message: types.Message):
    user_id = message.from_user.id
    # await message.reply(f"Ваш Telegram ID: {user_id}")
    await message.reply(f"Hi! I'm BioBitBot 👽", reply_markup=kb.inline_kb_0)


async def handler_help(message: types.Message):
    await message.reply(help_message)


async def handler_remove(message: types.Message):
    await message.reply("Keyboard removed.", reply_markup=ReplyKeyboardRemove())


async def process_callback_kb1btn1(bot, callback_query: types.CallbackQuery):
    code = callback_query.data[-2:]
    if code.isdigit():
        code = int(code)
    if code == 2:
        await bot.answer_callback_query(callback_query.id, text='Нажата вторая кнопка')
    elif code == 5:
        await bot.answer_callback_query(
            callback_query.id,
            text='Нажата кнопка с номером 5.\nА этот текст может быть длиной до 200 символов 😉', show_alert=True)
    else:
        await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, f'Нажата инлайн кнопка! code={code}')
