import telebot
from decouple import config


token = config('TOKEN')

stic1 = 'CAACAgIAAxkBAAEIBWZkBYbGuvU-eq87vsPPOSKj9qnLZAACOAADnCV8Py1Ghhu6ufMQLgQ'
stic2 = 'CAACAgIAAxkBAAEIBWlkBYbM-muhNYY7FHWgL95BTnz00gACHAADnCV8P6c5IwkGvb_KLgQ'

bot = telebot.TeleBot(token)

keyboard = telebot.types.ReplyKeyboardMarkup()
b1 = telebot.types.KeyboardButton('Да')
b2 = telebot.types.KeyboardButton('Нет')
keyboard.add(b1, b2)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, выбери кнопку', reply_markup=keyboard)
    bot.register_next_step_handler(message, reply_to_button)


def reply_to_button(message):
    if message.text == 'Да':
        bot.send_sticker(message.chat.id, stic1)
    elif message.text == 'Нет':
        bot.send_sticker(message.chat.id, stic2)
        
    else:
        bot.send_message(message.chat.id, 'Нажмите на кнопку')
    bot.register_next_step_handler(message, reply_to_button)
        
bot.polling()

