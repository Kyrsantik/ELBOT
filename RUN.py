
import telebot
from telebot import types
import sqlite3




bot = telebot.TeleBot("7341944123:AAG5BOXZY-0KFMdYuML_m1_gssMZvDwj-88")




@bot.message_handler(commands=['start'])
def start1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Четная")
    btn2 = types.KeyboardButton("Нечетная")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я тестовый бот расписания".format(message.from_user), reply_markup=markup)


@bot.message_handler(commands=['start'])
def start1(message):
	bot.send_message(message.chat.id, text="Выбор недели", )



@bot.message_handler(content_types=['text'])
def send_hi(message):
	if (message.text == "Нечетная"):
		bot.send_message(message.chat.id, text="Выбирай день")
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn1 = types.KeyboardButton("Понедельник")
		btn2 = types.KeyboardButton("Вторник")
		btn3 = types.KeyboardButton("Среда")
		btn4 = types.KeyboardButton("Четверг")
		btn5 = types.KeyboardButton("Пятница")
		back = types.KeyboardButton("Назад")
		markup.add(btn1, btn2, btn3,btn4,btn5,back)
		bot.send_message(message.chat.id,text="None",reply_markup=markup)

	elif  (message.text == "Понедельник"):
		conn = sqlite3.connect('nemmy_database.db')
		cursor = conn.cursor()

		cursor.execute("SELECT * FROM Понедельник")
		rows = cursor.fetchall()

		response = "Понедельник:\n\n"
		for row in rows:
			response += f"Пара: {row[0]},  {row[1]},  {row[2]}, {row[3]}\n"

		conn.close()
		bot.send_message(message.chat.id, response)

	elif message.text == "Вторник":
		conn = sqlite3.connect('nemmy_database.db')
		cursor = conn.cursor()

		cursor.execute("SELECT * FROM Вторник")
		rows = cursor.fetchall()

		response = "Вторник:\n\n"
		for row in rows:
			response += f"Пара: {row[0]},  {row[1]},  {row[2]}, {row[3]}\n"

		conn.close()
		bot.send_message(message.chat.id, response)
	elif message.text == "Среда":
		conn = sqlite3.connect('nemmy_database.db')
		cursor = conn.cursor()

		cursor.execute("SELECT * FROM Среда")
		rows = cursor.fetchall()

		response = "Среда:\n\n"
		for row in rows:
			response += f"Пара: {row[0]},  {row[1]},  {row[2]}, {row[3]}\n"

		conn.close()
		bot.send_message(message.chat.id, response)
	elif message.text == "Четверг":
		conn = sqlite3.connect('nemmy_database.db')
		cursor = conn.cursor()

		cursor.execute("SELECT * FROM Четверг")
		rows = cursor.fetchall()

		response = "Четверг:\n\n"
		for row in rows:
			response += f"Пара: {row[0]},  {row[1]},  {row[2]}, {row[3]}\n"

		conn.close()
		bot.send_message(message.chat.id, response)
	elif message.text == "Пятница":
		conn = sqlite3.connect('nemmy_database.db')
		cursor = conn.cursor()

		cursor.execute("SELECT * FROM Пятница")
		rows = cursor.fetchall()

		response = "Пятница:\n\n"
		for row in rows:
			response += f"Пара: {row[0]},  {row[1]},  {row[2]}, {row[3]}\n"

		conn.close()
		bot.send_message(message.chat.id, response)

	elif (message.text == "Назад"):
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		button1 = types.KeyboardButton("Четная")
		button2 = types.KeyboardButton("Нечетная")
		markup.add(button1, button2)
		bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
	else:
		bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")


def init_db():
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
def init_db2():
	conn = sqlite3.connect('nemmy_database.db')
	cursor = conn.cursor()


@bot.message_handler(content_types=['text'])
def func1(message):
	if (message.text == "Четная"):
		bot.send_message(message.chat.id, text="Выбирай день")
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn1 = types.KeyboardButton("Понедельник")
		btn2 = types.KeyboardButton("Вторник")
		btn3 = types.KeyboardButton("Среда")
		btn4 = types.KeyboardButton("Четверг")
		btn5 = types.KeyboardButton("Пятница")
		back = types.KeyboardButton("Назад")
		markup.add(btn1, btn2, btn3,btn4,btn5,back)
		bot.send_message(message.chat.id,text="None",reply_markup=markup)

	elif (message.text == "Понедельник"):
		conn = sqlite3.connect('my_database.db')
		cursor = conn.cursor()

		cursor.execute("SELECT * FROM Понедельник")
		rows = cursor.fetchall()

		response = "Понедельник:\n\n"
		for row in rows:
			response += f"Пара: {row[0]},  {row[1]},  {row[2]}, {row[3]}\n"

		conn.close()
		bot.send_message(message.chat.id, response)

	elif message.text == "Вторник":
		conn = sqlite3.connect('my_database.db')
		cursor = conn.cursor()

		cursor.execute("SELECT * FROM Вторник")
		rows = cursor.fetchall()

		response = "Вторник:\n\n"
		for row in rows:
			response += f"Пара: {row[0]},  {row[1]},  {row[2]}, {row[3]}\n"

		conn.close()
		bot.send_message(message.chat.id, response)
	elif message.text == "Среда":
		conn = sqlite3.connect('my_database.db')
		cursor = conn.cursor()

		cursor.execute("SELECT * FROM Среда")
		rows = cursor.fetchall()

		response = "Среда:\n\n"
		for row in rows:
			response += f"Пара: {row[0]},  {row[1]},  {row[2]}, {row[3]}\n"

		conn.close()
		bot.send_message(message.chat.id, response)
	elif message.text == "Четверг":
		conn = sqlite3.connect('my_database.db')
		cursor = conn.cursor()

		cursor.execute("SELECT * FROM Четверг")
		rows = cursor.fetchall()

		response = "Четверг:\n\n"
		for row in rows:
			response += f"Пара: {row[0]},  {row[1]},  {row[2]}, {row[3]}\n"

		conn.close()
		bot.send_message(message.chat.id, response)
	elif message.text == "Пятница":
		conn = sqlite3.connect('my_database.db')
		cursor = conn.cursor()

		cursor.execute("SELECT * FROM Пятница")
		rows = cursor.fetchall()

		response = "Пятница:\n\n"
		for row in rows:
			response += f"Пара: {row[0]},  {row[1]},  {row[2]}, {row[3]}\n"

		conn.close()
		bot.send_message(message.chat.id, response)

	elif (message.text == "Назад"):
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		button1 = types.KeyboardButton("Четная")
		button2 = types.KeyboardButton("Нечетная")
		markup.add(button1, button2)
		bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
	else:
		bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")








if __name__ == "__main__":
	init_db2()
	init_db()
	bot.polling(none_stop=True)
