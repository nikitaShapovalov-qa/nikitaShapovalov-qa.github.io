# подключение библиотек
# В google colab добавить: !pip install pyTelegramBotAPI
# для установки необходимо в файл requirements.text добавить строку
# 'PyTelegramBotApi'

from telebot import TeleBot, types
import random


bot = TeleBot(token='6862454908:AAHsSTYqj1Ym_bV1J32LgXXshkktVZGJqms', parse_mode='html') # создание бота

#библиотека блюд по категориям:
breakfast_list = ["Картофельные блины с зеленью/nhttps://www.russianfood.com/recipes/recipe.php?rid=149679" , "Панкейки (американские блинчики)/nhttps://www.russianfood.com/recipes/recipe.php?rid=134468"]
lunch_list = ["Лагман с курицей/nhttps://www.russianfood.com/recipes/recipe.php?rid=140715" , "Сырный суп по‑французски, с курицей/nhttps://www.russianfood.com/recipes/recipe.php?rid=130026"]
dinner_list = ["Жаркое по-деревенски/nhttps://www.russianfood.com/recipes/recipe.php?rid=159506" , "Макароны с куриными фрикадельками и томатным соусом/nhttps://www.russianfood.com/recipes/recipe.php?rid=159448"]

# обработчик команды '/start'
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Завтрак")
    btn2 = types.KeyboardButton("Обед")
    btn3 = types.KeyboardButton("Ужин")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Ну что, когда на пп?\nВыбор блюда исключительно за Тобой😉".format(message.from_user), reply_markup=markup)
    bot.send_video(message.chat.id, 'https://media.tenor.com/YufCI62GowIAAAAM/parks-and-rec-april-ludgate.gif', None, 'Text')

# обработчик всех остальных сообщений    
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Завтрак"):
     bot.send_message(message.chat.id,"Твой выбор на сегодня:\n\n{0}".format(random.choice(breakfast_list)))
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton("Да, спасибо за рекомендацию!🤩")
     btn2 = types.KeyboardButton("Давай другой завтрак")
     btn3 = types.KeyboardButton("Выбрать другую категорию")
     markup.add(btn1, btn2, btn3)
     bot.send_message(message.chat.id,text="Ну что, пойдёшь кушотб?☺️", reply_markup=markup)

    elif(message.text == "Давай другой завтрак"):
      bot.send_message(message.chat.id,"Твой выбор на сегодня:\n\n{0}".format(random.choice(breakfast_list)))
      bot.send_message(message.chat.id,text="А если этот?👉🏻👈🏻")

    elif(message.text == "Обед"):
     bot.send_message(message.chat.id,"Твой выбор на сегодня:\n\n{0}".format(random.choice(lunch_list)))
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton("Да, спасибо за рекомендацию!🤩")
     btn2 = types.KeyboardButton("Давай другой обэд")
     btn3 = types.KeyboardButton("Выбрать другой жанр🧐")
     markup.add(btn1, btn2, btn3)
     bot.send_message(message.chat.id,text="Ну что, пойдёшь куоштб?☺️", reply_markup=markup)

    elif message.text == "Давай другой обэд":
      bot.send_message(message.chat.id,"Твой выбор на сегодня:\n\n{0}".format(random.choice(lunch_list)))
      bot.send_message(message.chat.id,text="А если этот?👉🏻👈🏻")

    elif(message.text == "Ужин"):
      bot.send_message(message.chat.id,"Твой выбор на сегодня:\n\n{0}".format(random.choice(dinner_list)))
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      btn1 = types.KeyboardButton("Да, спасибо за рекомендацию!🤩")
      btn2 = types.KeyboardButton("Давай другой ужин")
      btn3 = types.KeyboardButton("Выбрать другой жанр🧐")
      markup.add(btn1, btn2, btn3)
      bot.send_message(message.chat.id,text="Ну что, пойдёшь куоштб?☺️", reply_markup=markup)

    elif message.text == "Давай другой ужин":
      bot.send_message(message.chat.id,"Твой выбор на сегодня:\n\n{0}".format(random.choice(dinner_list)))
      bot.send_message(message.chat.id,text="А если этот?👉🏻👈🏻")
    
    elif(message.text == "Да, спасибо за рекомендацию!🤩"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("/start")
        markup.add(btn1)
        bot.send_message(message.chat.id,text="Обращайся!😇", reply_markup=markup)
        bot.send_video(message.chat.id, 'https://gifdb.com/images/high/naruto-shippuden-rock-lee-ip8r3dyc7qfqwccq.gif', None, 'Text')
    
    elif (message.text == "Выбрать другой жанр🧐"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Завтрак")
        btn2 = types.KeyboardButton("Обед")
        btn3 = types.KeyboardButton("Ужин")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню😉", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="Я такое не проходил😟")


# главная функция программы
def main():
    # запускаем нашего бота
    bot.infinity_polling()


if __name__ == '__main__':
    main()