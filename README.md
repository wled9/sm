pyTelegramBotAPI
pyTelegramBotAPI
requests
git add requirements.txt
git commit -m "Add requirements.txt"
git push origin main
import telebot

TOKEN = "your_bot_token_here"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "مرحبًا! أنا بوتك الجديد. جرب /help")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "الأوامر المتاحة: /start, /help")

bot.polling()
worker: python bot.py
