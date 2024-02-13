from dispatcher import dispatcher
from aiogram.filters.command import Command


@dispatcher.message(Command("start"))
async def cmd_start(message):
    await message.answer("Привіт!\n Я-бот-помічник\n буду радий допомогти тобі записатись на манікюр 💓")