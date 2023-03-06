import telebot
from decouple import config

token = config('TOKEN')

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello')
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEIBS5kBXYZ3_TbfTkpkrKGr4dNCNUeQwACHwADnCV8P_tr0JbOH3rmLgQ')
    bot.send_photo(message.chat.id, 'https://cs12.pikabu.ru/post_img/big/2022/08/09/7/1660042588198544626.png')



@bot.message_handler(content_types=['text'])
def aaa(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет')
    else:
        bot.send_message(message.chat.id, 'Сообщение не разпознанно')

bot.polling()


# @bot.message_handler(content_types=['stiker'])
# def bbb(message):
#     bot.send_sticker(message.chat.id, message)

# bot.polling()