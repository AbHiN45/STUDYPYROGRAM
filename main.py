from pyrogram import Client, filters


API_ID = "15476227"
API_HASH = "c64d4881f7d539052942f6f03dfe9d60"
BOT_TOKEN = "5329764861:AAHfUq6IlAfIRE_e8n1zXNQmBuI06R__QPU"



ABHI = Client(
    name="pyrogrambot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


print("Bot Started")

ABHI.run()
