import telebot
from telebot import types

bot = telebot.TeleBot('Bot API')

#control start command
@bot.message_handler(commands = ['start'])
def start(message):
    mess =  f'привет <b>{message.from_user.first_name}</b>'
    bot.send_message(message.chat.id, mess , parse_mode = 'html')

#controll text input from user
@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == "Hello":
        bot.send_message(message.chat.id, 'И тебе привет', parse_mode = 'html')
    elif message.text == "id":
        bot.send_message(message.chat.id, f'Твой ID: {message.from_user.id}', parse_mode = 'html')
    elif message.text == "photo":
        photo = open('download.png','rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == "website":
        website(message)
    elif message.text == "help":
        help(message)
            

    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю', parse_mode = 'html')

    
@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'крутое фото!')


@bot.message_handler(commands = ['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Посетить Вебсайт',url='https://google.com'))
    bot.send_message(message.chat.id, 'Перейдите на сайт!', reply_markup=markup)


@bot.message_handler(commands = ['help'])
def help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
    website = types.KeyboardButton('Веб Сайт')
    start = types.KeyboardButton('Старт')

    markup.add(website, start)
    bot.send_message(message.chat.id, 'Перейдите на сайт!', reply_markup=markup)



bot.polling(none_stop = True)