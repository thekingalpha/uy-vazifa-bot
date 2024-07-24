import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '7398693196:AAH-auQYvhqK7X_FpKsCh7YiT98lUDdYUiM'

logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Salom!\nMen EchoBot!\nAiogram tomonidan yaratilganman.")
@dp.message_handler(commands=['yordam'])
async def send_helper(msg:types.Message):
    await msg.answer("Bu bot haqida alpha_king09 dan \nbatafsil toliq malumot olishingiz mumkin")



@dp.message_handler()
async def echo(message: types.Message):


    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)