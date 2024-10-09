
FROM python:3.9

WORKDIR /app

RUN pip install pyTelegramBotAPI

COPY . .

CMD ["python", "RUN.py"]
