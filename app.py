import telebot


bot=telebot.TeleBot(token='1955445317:AAG1t5jNxvDPUljV-dd_cHRKIEZ3-l7sHtM')

from handler import *

if __name__=='__main__':
    bot.polling(none_stop=True)