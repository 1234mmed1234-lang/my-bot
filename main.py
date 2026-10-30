import os
import telebot

BOT_TOKEN = os.environ.get("BOT_TOKEN")
TEXT = "للسعر تواصل خاص"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, TEXT)

@bot.message_handler(func=lambda m: True)
def all_msg(m):
    bot.reply_to(m, TEXT)

print("البوت شغال للابد...")
bot.infinity_polling()
