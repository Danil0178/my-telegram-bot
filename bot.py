import os
from telegram.ext import Updater, CommandHandler

TOKEN = os.getenv("TOKEN")

def start(update, context):
    update.message.reply_text("Привет! Я твой Telegram-бот!")

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
