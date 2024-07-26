from email import message

from  aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states.personalData import PersonalData



@dp.message_handler(Command("form"), state=None)
async def enter_test(meessage: types.Message):
    await message.answer("Toliq ismingizni kiriting")
    await PersonalData.fullName.set()


@dp.message_handler(state=PersonalData.fullName)
async def answer_fullname(message: types.Message, state: FSMContext):
    fullname = message.text

    await state.update_data(
        {"name": fullname}
    )

    await message.answer("Email manzil kiriting")

    await PersonalData.next()

@dp.message_handler(state=PersonalData.email)
async def answer_email(message: types.Message, state: FSMContext):
    email = message.text