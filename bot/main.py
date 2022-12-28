import markups as kb

from config import TOKEN, SP_ID

from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware


bot = Bot(token = TOKEN)
dp = Dispatcher(bot, storage = MemoryStorage())
dp.middleware.setup(LoggingMiddleware())


@dp.callback_query_handler(lambda call: call.data == "button_audit_8507")
async def button_ru(callback_query: types.CallbackQuery):
    status_8507 = "свободна"
    count_8507 = 24
    if count_8507 != 0:
        status_8507 = "занята"
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           "Аудитория #8507\n\n"
                           f"Человек в аудитории: {count_8507}\n"
                           f"Статус: {status_8507}",
                           reply_markup = kb.kb_back)


"""
@dp.callback_query_handler(lambda call: call.data == "button_audit_8508")
async def button_ru(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           "Аудитория #8508\n\n"
                           f"Человек в аудитории: {count_8508}\n"
                           f"Статус: {status_8508}",
                           reply_markup = kb.kb_back)

@dp.callback_query_handler(lambda call: call.data == "button_audit_8509")
async def button_ru(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           "Аудитория #8509\n\n"
                           f"Человек в аудитории: {count_8509}\n"
                           f"Статус: {status_8509}",
                           reply_markup = kb.kb_back)
"""


@dp.callback_query_handler(lambda call: call.data == "button_back")
async def button_ru(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Привет, выбери номер аудитории🔗", reply_markup = kb.kb_audit)


@dp.message_handler(commands = ["start"])
async def start_command(message: types.Message):
    await message.answer("Привет, выбери номер аудитории🔗", reply_markup = kb.kb_audit)


if __name__ == '__main__':
	executor.start_polling(dp, skip_updates = True)
