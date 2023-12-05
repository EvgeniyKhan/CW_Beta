import pandas as pd
import json

from config import OPEN_XLS
from src.log import log_utils

logging = log_utils()


def search_transactions(filename, querys):
    df = pd.read_excel(filename)
    filtered_df = df[df["Описание"].str.contains(querys, case=False,na=False)]
    result = filtered_df.to_dict(orient="records")
    logging.info("Преобразование фильтрованного DataFrame в список словарей")
    return json.dumps(result, indent=4, ensure_ascii=False)


# Пример использования функции
file_path = OPEN_XLS  # Путь к файлу Excel
query = "Аптеки"  # Строка запроса
result = search_transactions(file_path, query)
print(result)
