import telebot
from config import token
from telebot import types
import random

bot = telebot.TeleBot(token)

f = open('fact.txt', 'r', encoding='utf-8') 
facts = f.read().split('\n')
f.close()

f = open('sovet.txt', 'r', encoding='utf-8')
sovets  = f.read().split('\n')
f.close()

@bot.message_handler(commands=['start'])
def start_message(message):
    nik_name = f'Привет, {message.from_user.first_name} {message.from_user.last_name}!'
    bot.send_message(message.chat.id, nik_name)

@bot.message_handler(commands=['info'])
def get_info(message):
    bot.send_message(message.chat.id, 'Привет! Я полезный бот - Милка! Благодаря мне ты сможешь с пользой скоротать время! У меня есть несколько функций: start, info, button. Воспользоваться ими ты сможешь, отправив мне сообщение с названием выбранной функции. Функция button откроет еще много интересного: ты сможешь узнать прогноз погоды, получить совет дня, интересный факт и счастливое число дня.')

@bot.message_handler(commands=['button'])    
def get_button(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item1=types.KeyboardButton('Факт дня') 
    item2=types.KeyboardButton('Совет дня') 
    item3=types.KeyboardButton('Счастливое число дня')
    item4=types.KeyboardButton('Погода')
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id,'Выбирай кнопку',reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text.strip() == 'Факт дня':
        answer = random.choice(facts)
        bot.send_message(message.chat.id, answer)

    elif message.text.strip() == 'Совет дня':
        answer = random.choice(sovets)
        bot.send_message(message.chat.id, answer)
    
    elif message.text == 'Счастливое число дня':
        bot.send_message(message.chat.id, 'Твое счастливое число на сегодня:  ' + str(random.randint(1, 10)))
    
    elif message.text == 'Погода':
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton('Прогноз погоды на сегодня', url='https://yandex.ru/pogoda')
        keyboard.add(url_button)
        bot.send_message(message.chat.id, 'Для того чтобы узнать прогноз, нажми на кнопку ниже.', reply_markup=keyboard)

    elif message.text=='Привет':
        bot.send_message(message.chat.id, 'И тебе привет!')
    elif message.text=='id':
        bot.send_message(message.chat.id, f'Твой id: {message.from_user.id}')
    elif message.text=='Как дела?':
        bot.send_message(message.chat.id, 'Отлично, как у тебя?')
    elif message.text== 'Хорошо':
        bot.send_message(message.chat.id, 'Я очень рада за тебя!')
    elif message.text=='Нормально':
        bot.send_message(message.chat.id, 'Это хорошо!')
    elif message.text== 'Плохо':
        bot.send_message(message.chat.id, 'Не грусти! Все будет хорошо!')
    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю')

@bot.message_handler(content_types=['sticker'])
def get_sticker(message):
    bot.send_message(message.chat.id, 'Вау, классный стикер!')
    
bot.polling(non_stop=True)