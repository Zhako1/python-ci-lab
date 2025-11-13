# Используем официальный образ Python
FROM python:3.11-slim

# Рабочая директория в контейнере
WORKDIR /app

# Копируем зависимости и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь код проекта
COPY src/ src/
COPY tests/ tests/

# Команда по умолчанию — запуск тестов
CMD ["python", "-m", "pytest", "tests/"]
