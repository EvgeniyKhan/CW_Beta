import pandas as pd
import json
from src.utils import get_greeting, transactions_xlsx_open, process_data, top_transactions, open_json, collect_response


def test_get_greeting():
    # Тест для функции get_greeting()
    greetings = ["Добрый ночи!", "Доброе утро!", "Добрый день!", "Добрый вечер!"]
    greeting = get_greeting()
    assert greeting in greetings


def test_transactions_xlsx_open():
    # Тест для функции transactions_xlsx_open()
    # Создаем временный DataFrame и сохраняем его в файл
    data = {'Номер карты': [1111, 2222, 3333], 'Сумма платежа': [100, 200, 300], 'Дата операции': ['2023-12-01', '2023-12-02', '2023-12-03']}
    df = pd.DataFrame(data)
    file_path = 'test_transactions.xlsx'
    df.to_excel(file_path, index=False)

    # Проверяем, что функция корректно читает файл
    result = transactions_xlsx_open(file_path)
    assert isinstance(result, pd.DataFrame)
    assert len(result) == 3  # Проверяем количество записей в DataFrame


def test_process_data():
    # Тест для функции process_data()
    # Создаем временный DataFrame
    data = {'Номер карты': [1111, 2222, 3333], 'Сумма платежа': [100, 200, 300], 'Дата операции': ['2023-12-01', '2023-12-02', '2023-12-03']}
    df = pd.DataFrame(data)

    # Вызываем функцию process_data() с начальной датой и проверяем корректность обработки данных
    result = process_data(df, "2023-12-02")
    assert isinstance(result, list)
    assert len(result) == 2  # Проверяем количество записей в списке данных


def test_top_transactions():
    # Тест для функции top_transactions()
    # Создаем временный DataFrame
    data = {'Дата операции': ['2023-12-01', '2023-12-02', '2023-12-03'],
            'Сумма платежа': [100, 200, 300],
            'Категория': ['Продукты', 'Одежда', 'Техника'],
            'Описание': ['Покупка продуктов', 'Покупка одежды', 'Покупка техники']}
    df = pd.DataFrame(data)

    # Вызываем функцию top_transactions() и проверяем формат возвращаемых данных
    result = top_transactions(df)
    assert isinstance(result, list)
    assert len(result) == 3  # Проверяем количество записей в списке топ-транзакций


def test_open_json():
    # Тест для функции open_json()
    # Создаем временный JSON файл
    data = {'user_currencies': ['USD', 'EUR', 'GBP']}
    file_path = 'test_settings.json'
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file)

    # Проверяем, что функция правильно открывает и читает JSON файл
    result = open_json(file_path, 'user_currencies')
    assert isinstance(result, list)
    assert len(result) == 3  # Проверяем количество валют в списке