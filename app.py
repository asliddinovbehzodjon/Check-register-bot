import telebot


bot=telebot.TeleBot(token='API token')

from handler import *

if __name__=='__main__':
    bot.polling(none_stop=True)
