import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# الحصول على التوكن من متغيرات البيئة
TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')

def start(update, context):
    update.message.reply_text('مرحباً! أنا بوت صدى. أرسل لي أي شيء وسأعيده لك.')

def echo(update, context):
    update.message.reply_text(update.message.text)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

