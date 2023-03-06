import telebot
from decouple import config


token = config('TOKEN')

stic1 = 'CAACAgIAAxkBAAEIBWZkBYbGuvU-eq87vsPPOSKj9qnLZAACOAADnCV8Py1Ghhu6ufMQLgQ'
stic2 = 'CAACAgIAAxkBAAEIBWlkBYbM-muhNYY7FHWgL95BTnz00gACHAADnCV8P6c5IwkGvb_KLgQ'

keyboard = telebot.types.InlineKeyboardMarkup()
b1 = telebot.types.InlineKeyboardButton('Yes', callback_data='yes')
b2 = telebot.types.InlineKeyboardButton('No', callback_data='no')
keyboard.add(b1, b2)


bot = telebot.TeleBot(token)



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, выбери кнопку', reply_markup=keyboard)
    bot.register_next_step_handler(message, reply_to_button)


@bot.callback_query_handler(func=lambda x: True)
def reply_to_button(call):
    if call.data == 'yes':
        bot.send_sticker(call.from_user.id, stic1)
    elif call.data == 'no':
        bot.send_sticker(call.from_user.id, stic2)

bot.polling()