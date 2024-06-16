import telebot
from telebot import types
bot = telebot.TeleBot('7090987390:AAEJoL-057D9-m1yKIpwK7DIGpd5EECYqpg')




@bot.message_handler(commands=['start']) #создаем команду старт и кнопки
def main(chat):
    buttons = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('ИЗЖ первый том')
    buttons.row(btn1)
    btn2 = types.KeyboardButton('ИЗЖ второй том')
    btn3 = types.KeyboardButton('ИЗЖ третий том')
    buttons.row(btn2, btn3)
    bot.send_message(chat.chat.id, 'Привет всем, я Полибот, ваш помощник', reply_markup=buttons)
    # file = open('./history_tom1.pdf', 'rb')
    # bot.send_document(chat.chat.id, file,  reply_markup=buttons)
    bot.register_next_step_handler(chat, on_click)



def on_click(message): # привязываем к этим кнопкам функции
    if message.text == 'ИЗЖ первый том':
        file = open('./history_tom1.pdf', 'rb')
        bot.send_document(message.chat.id, file)
    elif message.text == 'ИЗЖ второй том':
        file = open('./history_tom2.pdf', 'rb')
        bot.send_document(message.chat.id, file)
    elif message.text == 'ИЗЖ третий том':
        file = open('./history_tom3.pdf', 'rb')
        bot.send_document(message.chat.id, file)



# @bot.message_handler(content_types=['photo'])
# def get_text(message):
#     buttons = types.InlineKeyboardMarkup()
#     btn1 = types.InlineKeyboardButton('ИЗЖ первый том', url='https://google.com')
#     buttons.row(btn1)
#     btn2 = types.InlineKeyboardButton('ИЗЖ второй том', callback_data='delete')
#     btn3 = types.InlineKeyboardButton('ИЗЖ третий том', callback_data='edit')
#     buttons.row(btn2, btn3)
#     bot.reply_to(message, "пожалуйста", reply_markup=buttons)
#
#
#
# @bot.callback_query_handler(func=lambda callback: True)
# def callback_message(callback):
#     if callback.data == 'delete':
#         bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
#     elif callback.data == 'edit':
#         bot.edit_message_text('изменено', callback.message.chat.id, callback.message.message_id)

bot.polling(none_stop=True)