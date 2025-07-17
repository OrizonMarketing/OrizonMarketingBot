import telebot
import os

API_TOKEN = os.getenv('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['process'])
def process_start(message):
    bot.reply_to(message, "Willkommen! Hier ist dein Onboarding:\n\n📹 Video 1: [LINK]\n📹 Video 2: [LINK]\n\nSchreib „ready“, wenn du fertig bist.")

@bot.mes
