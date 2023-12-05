import requests

from dotenv import load_dotenv

from src.log import log_utils

logging = log_utils()
load_dotenv()


def get_stocks(data_stocks):
    try:
        list_stocks = []
        for stock in data_stocks:
            url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock}&apikey=VDHDS2LIGY9O50SZ'
            data = requests.get(url).json()
            list_stocks.append({
                "stock": data['Global Quote']['01. symbol'],
                "price": data['Global Quote']['05. price']
            })
        logging.info("Из файла user_settings.json получен список акций")
        return list_stocks
    except Exception as e:
        logging.error(f"Произошла ошибка: {e}")
        return [], []


def get_currencies(data_currencies):
    try:
        list_currencies = []
        for currencie in data_currencies:
            url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={currencie}&to_currency=RUB&apikey=N64DYQB2WV5QR1WW"
            data = requests.get(url).json()
            list_currencies.append({
                "currency": data['Realtime Currency Exchange Rate']['1. From_Currency Code'],
                "rate": data['Realtime Currency Exchange Rate']['5. Exchange Rate']
            })
        logging.info("Из файла user_settings.json получен список валют")
        return list_currencies
    except Exception as e:
        logging.error(f"Произошла ошибка: {e}")
        return [], []
