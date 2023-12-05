from typing import Optional

import pandas as pd

from src.log import log_utils
from src.utils import transactions_xlsx_open

dataFrame = transactions_xlsx_open()
logging = log_utils()


def spending_by_category(
        transactions: pd.DataFrame,
        category: str,
        date: Optional[str] = None
) -> pd.DataFrame:
    start_date = pd.to_datetime(date, format='%d.%m.%Y', dayfirst=True)
    logging.info("Преобразуем задаваему дату в формат даты")
    transactions['Дата операции'] = pd.to_datetime(transactions['Дата операции'], format='%d.%m.%Y %H:%M:%S')
    logging.info("Преобразуем столбец 'Дата операции' в формат даты")
    start_date_ = start_date - pd.DateOffset(months=3)
    logging.info("Рассчитываем начальную дату, как введенную дату минус 3 месяца")
    filtered_transactions = transactions[
        (transactions['Дата операции'] >= start_date_) & (transactions['Дата операции'] <= start_date)]
    result = filtered_transactions.loc[filtered_transactions['Категория'] == category]
    logging.info("Фильтруем данные за 3 месяца")
    return result.to_json(orient='records', indent=4, force_ascii=False)
