import telebot
import requests
import json
from config import keys


class APIException(Exception):
    pass

class CurrencyConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):

        if quote == base:
            raise APIException(f'Конвертация одинаковых валют невозможна {base}!')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Ошибка при обработке валюты {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Ошибка при обработке валюты {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Ошибка при обработке указанной суммы {amount}')

        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}")
        total_base = json.loads(r.content)[keys[base]]
        return total_base