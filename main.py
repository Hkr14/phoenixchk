#pylint:disable=C0114
import logging
import os
from pyrogram import Client
from pyrogram.errors import RPCError
from pyrogram.errors import BadRequest
# import asyncio
# from pyrogram.errors import FloodWait
# from pyrogram.handlers import MessageHandler
# os.environ['TZ'] = 'Asia/Kolkata'



logging.basicConfig(level=logging.INFO)



bot = Client(
    'bot',
    api_id= 13221029, #get it from https://my.telegram.org/auth
    api_hash="8ee3c5bfe718a463900933d8f6ef0158", #get it from https://my.telegram.org/auth
    bot_token="5650840926:AAEl1dL99zPqUFfrvl_DFjnBzoltd4mO9o4", #get it from @Botfather
    plugins=dict(root="plugins"),
    parse_mode="html")


try:
    bot.run()
except Exception as e:
    print(e)
        