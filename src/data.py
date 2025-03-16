from datetime import datetime
from typing import Any


def data(current_time: datetime) -> Any:
    """Функция принимает текущую дату и приветствует пользователя."""
    hour = current_time.hour

    if hour < 6:
        return "Доброй ночи"
    elif 6 <= hour < 12:
        return "Доброе утро"
    elif 12 <= hour < 18:
        return "Добрый день"
    elif 18 <= hour < 24:
        return "Добрый вечер"
