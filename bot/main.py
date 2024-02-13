from dispatcher import dispatcher
from bot import bot
from __init__ import *
import asyncio


async def bot_deploy():
    await dispatcher.start_polling(bot)


asyncio.run(bot_deploy())


