from background import keep_alive
import pip

pip.main(['install', 'pytelegrambotapi'])
import telebot
from telebot import types
import change

bot = telebot.TeleBot('Insert_your_bot_token') # сюда нужно закинуть свой бот-токен, который сгенерит BotFather


@bot.message_handler(commands=['start', 'начать'])  # старт
def start(message):  # вывод сообщения
  mess = f'Приветствую, <b><u>{message.from_user.first_name}</u></b>. Чтобы ознакомиться с функциями этого бота нажмите /button.'  # вывод имени пользователя; f - форматированная строка
  bot.send_message(
    message.chat.id, mess,
    parse_mode='html')  # именно в этот чат будем кидать сообщение


@bot.message_handler(commands=['button', 'кнопки']
                     )  # создание кнопки, которая будет изначально
def button(message_4):
  markup = types.ReplyKeyboardMarkup(
    resize_keyboard=True,
    row_width=2)  # встроенная кнопка, кол-во 2 в одной строке
  fio = types.KeyboardButton('ФИО')
  list_of_group = types.KeyboardButton('Список групп')
  report = types.KeyboardButton('Документы')
  holidays = types.KeyboardButton('Командировка')
  markup.add(fio, list_of_group, report, holidays)
  bot.send_message(message_4.chat.id,
                   "Выберите, что вас интересует.",
                   reply_markup=markup)


@bot.message_handler(regexp='ФИО'
                     )  # regexp - сравнить какой-то текст # весь курс
def FIO(mess):
  messe = 'Вот список всех студентов 1 курса: '
  bot.send_message(mess.chat.id, messe, parse_mode='html')
  file = open("Список курса.docx", "rb")
  bot.send_document(mess.chat.id, file) # вывод списка курса

@bot.message_handler(commands=['help', 'команды'])  # хэлпер
def get_help_text(helps):
  helper = (
    "Приветствую! Меня зовут Хэлпер. Я помогу вам узнать об командах бота:\n \n"
    "          * /start, /начать - старт работы бота;\n"
    "          * /button - вывод главных кнопок;\n "
    "         * /doc (название_документа) - вывод нужного документа в .docx формате;\n"
    "          * /website - переход на гит-хаб.\n\n "
    "На этом пока все.")
  bot.send_message(helps.chat.id, helper, parse_mode='html')


@bot.message_handler(regexp='Командировка')  # regexp - сравнить какой-то текст
def weekend(holid):
  messeg = 'Вот список всех студентов 1 курса убывающие в командировку на этой неделе: '
  bot.send_message(holid.chat.id, messeg, parse_mode='html')
  file1 = open("Командировка.docx", "rb")
  bot.send_document(holid.chat.id, file1)


@bot.message_handler(regexp="Документы")  # хелпер-документы
def get_rap(rap):
  bot.send_message(
    rap.chat.id,
    "Хэлпер поможет вам!\n"
    "Сейчас бот имеет следующие файлы:\n\n"
    "      * проездной.\n\n"
    "Чтобы вывести нужный документ пропишите /doc (название файла указанного выше).",
    parse_mode='html')


@bot.message_handler(commands=['doc'])  # документы
def get_file(message_1):
  if message_1.text == '/doc проездной':
    file = open("Проездной.docx", "rb")
    bot.send_document(message_1.chat.id, file)

  else:
    bot.send_message(message_1.chat.id,
                     "Я не знаю, что это за файл. Чтобы узнать, какие файлы имеет бот, нажмите на кнопку \"Документы\".",
                     parse_mode='html')


@bot.message_handler(regexp='website')  # создание кнопки, которая вылезет
def website_2(message_3):
  markup = types.InlineKeyboardMarkup(
  )  # встроенные в сообщение кнопки, фото и т.д.
  markup.add(
    types.InlineKeyboardButton(
      "Посетить веб-сайт:", url="https://github.com/oooNAKooo"))  # текст кнопки
  bot.send_message(message_3.chat.id,
                   "Это мой гит-хаб.",
                   reply_markup=markup)  # текст над кнопкой


@bot.message_handler(regexp="Список групп")  # regexp - сравнить какой-то текст
def list(mess):
  messe = 'Вот список групп 1 курса: '
  markup = types.InlineKeyboardMarkup(
  )  # встроенные в сообщение кнопки, фото и т.д.
  markup.add(types.InlineKeyboardButton(
    "1", callback_data='1'))  # текст кнопки + вызов кнопки
  markup.add(types.InlineKeyboardButton("2",
                                        callback_data='2'))  #  -//-
  markup.add(types.InlineKeyboardButton("3",
                                        callback_data='3'))  #  -//-
  bot.send_message(mess.chat.id, messe, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True
                            )  # работа со встроенными кнопками групп
def callback_function1(callback_obj: telebot.types.CallbackQuery):
  if callback_obj.data == "1":
    bot.send_message(callback_obj.from_user.id, "Вы выбрали группу 1.")
    file1 = open("Штат группы 1.docx", "rb")
    bot.send_document(callback_obj.from_user.id, file1)
    file2 = open("Расписание Март группа 1.docx", "rb")
    bot.send_document(callback_obj.from_user.id, file2)
    file3 = open("Учет лабораторных работ.xlsx", "rb")
    bot.send_document(callback_obj.from_user.id, file3)
  elif callback_obj.data == "2":
    bot.send_message(callback_obj.from_user.id, "Вы выбрали группу 2.")
    file1 = open("Штат группы 2.docx", "rb")
    bot.send_document(callback_obj.from_user.id, file1)
    file2 = open("Расписание Март группа 2.docx", "rb")
    bot.send_document(callback_obj.from_user.id, file2)
    file3 = open("Учет лабораторных работ.xlsx", "rb")
    bot.send_document(callback_obj.from_user.id, file3)
  elif callback_obj.data == "3":
    bot.send_message(callback_obj.from_user.id, "Вы выбрали группу 3.")
    file1 = open("Штат группы 3.docx", "rb")
    bot.send_document(callback_obj.from_user.id, file1)
    file2 = open("Расписание Март группа 3.docx", "rb")
    bot.send_document(callback_obj.from_user.id, file2)
    file3 = open("Учет лабораторных работ.xlsx", "rb")
    bot.send_document(callback_obj.from_user.id, file3)
  bot.answer_callback_query(callback_query_id=callback_obj.id)


@bot.message_handler(
  content_types=['sticker', 'photo', 'audio', 'pinned_message',
                 'document'])  # если не текст
def get_user_type(message_2):
  bot.send_message(message_2.chat.id,
                   'Я не воспринимаю данный тип данных. Только текст!',
                   parse_mode='html')


@bot.message_handler()  # неизвестная команда
def get_user_text(message_1):
  expept = 'Введена неверная команда! Чтобы узнать список команд нажмите \'/help\'.'
  bot.send_message(message_1.chat.id, expept, parse_mode='html')


keep_alive()  # for flask-server
bot.polling(none_stop=True)  # постоянная работа бота #ctrl+c - остановка бота

# <b>...</b> - текст жирный <bold>
# <u>...</u> - текст подчеркнутый <underline>
