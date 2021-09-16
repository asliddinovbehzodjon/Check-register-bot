from app import bot

from check import checkmember
@bot.message_handler(commands=['start'])
def welcome(message):
    id=message.chat.id
    if checkmember(id):
        bot.send_message(id,'Siz kanalga azosiz')
    else:
        bot.send_message(id,'Kanalga azo boling!!!')