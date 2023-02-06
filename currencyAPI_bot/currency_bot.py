import telebot
from config import keys, TOKEN
from extensions import APIException, CurrencyConverter
from telebot import types


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'старт', 'help'])
def start(message: telebot.types.Message):
    text = "Вас приветствует Бот-конвертор курса валют.\
    Пожалуйста, выберите валюту, которую хотите конвертировать.\
    Для выбора валюты введите:    /values."

    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def choice(message: telebot.types.Message):
    text = "После выбора валют через пробел, укажите сумму для конвертации!\nДоступные валюты:\n"
    for key in keys.keys():
        text = '\n'.join((text, key,))

    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
    try:
        values = message.text.split(" ")

        if len(values) != 3:
            raise ConvertionException('Необходимо указать 2 вида валюты!')

        quote, base, amount = values
        total_base = CurrencyConverter.get_price(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось выполнить запрос.\n{e}')
    else:
        text = f"Цена {amount} {quote} в {base} - {total_base}"
        bot.send_message(message.chat.id, text)




bot.polling()