#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables

API_ID = 26664450
API_HASH = "4c5aa841602e381f07dfd5b8ff77a54f"
BOT_TOKEN = "6297068371:AAHPutheUQ0n0I0bhVoCM1bg1eRF3YvQsw4"
SESSION = "AQA95uE5b8i-Bl-BLQ7gtSDymurNTg2RCzF2aAvKWxxMMu9F7EraWokYHCJT31qhyxWmGRm5d7Yg2BeVjTZUJ7KiqYpaFVhsJUwM0uFVXBtF6xW_7VPVVYfaCFWi6FFmepvM16cv1jjYe6qJN0UES9UxcijTCwu9WJt5Ep45rh8ehGBqmKwPM7DcY7olLJE7Z_a-qRwsr5z2z8YgkmGHHMCqMIswaKsyJM1gx2gZ-EXCFfVDS7sB3dwEnBJT5Qa6_SVsvszE9hG5XYxSpbb6s4ER40rdwpILlurPqNsQRM0sO3VyRJUvaGPrsSH2PONtl4AozsGnjvzvf7pYlBMrvqm8AAAAAW2kLsUA"
FORCESUB = "fvckkkkkkkkkks"
AUTH = 6134443717

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
