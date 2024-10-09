from email.message import Message
from time import process_time_ns

import telebot
from telebot import types
import sqlite3




bot = telebot.TeleBot("7092861594:AAEbsf0jhTm6dHpBEs0XNiltMqtp0e5vxVM")




@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Четная")
    btn2 = types.KeyboardButton("Нечетная")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я тестовый бот расписания".format(message.from_user), reply_markup=markup)





@bot.message_handler(content_types=['text'])
def week_sending(message):
	if (message.text == "Нечетная"):
		bot.send_message(message.chat.id, text="Выбирай день")
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn1 = types.KeyboardButton(".Понедельник")
		btn2 = types.KeyboardButton(".Вторник.")
		btn3 = types.KeyboardButton(".Среда.")
		btn4 = types.KeyboardButton(".Четверг.")
		btn5 = types.KeyboardButton(".Пятница.")
		back = types.KeyboardButton("Назад")
		markup.add(btn1, btn2, btn3,btn4,btn5,back)
		bot.send_message(message.chat.id,text="//////////////////",reply_markup=markup)
	elif (message.text == "1Понедельник"):
		conn = sqlite3.connect('nemmy_database.db')
		cursor = conn.cursor()

		cursor.execute("SELECT * FROM Понедельник")
		rows = cursor.fetchall()

		response = "Понедельник:\n\n"
		for row in rows:
			response += f"Пара: {row[0]},  {row[1]},  {row[2]}, {row[3]}\n"

		conn.close()
		bot.send_message(message.chat.id, response)

	elif message.text == ".Вторник.":
		conn = sqlite3.connect('nemmy_database.db')
		cursor = conn.cursor()

		cursor.execute("SELECT * FROM Вторник")
		rows = cursor.fetchall()

		response = "Вторник:\n\n"
		for row in rows:
			response += f"Пара: {row[0]},  {row[1]},  {row[2]}, {row[3]}\n"

		conn.close()
		bot.send_message(message.chat.id, response)
	elif message.text == ".Среда.":
		conn = sqlite3.connect('nemmy_database.db')
		cursor = conn.cursor()

		cursor.execute("SELECT * FROM Среда")
		rows = cursor.fetchall()

		response = "Среда:\n\n"
		for row in rows:
			response += f"Пара: {row[0]},  {row[1]},  {row[2]}, {row[3]}\n"

		conn.close()
		bot.send_message(message.chat.id, response)
	elif message.text == ".Четверг.":
		conn = sqlite3.connect('nemmy_database.db')
		cursor = conn.cursor()

		cursor.execute("SELECT * FROM Четверг")
		rows = cursor.fetchall()

		response = "Четверг:\n\n"
		for row in rows:
			response += f"Пара: {row[0]},  {row[1]},  {row[2]}, {row[3]}\n"

		conn.close()
		bot.send_message(message.chat.id, response)
	elif message.text == ".Пятница.":
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
	if (message.text == "Четная"):
		bot.send_message(message.chat.id, text="Выбирай день")
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn11 = types.KeyboardButton("Понедельник")
		btn22 = types.KeyboardButton("Вторник")
		btn33 = types.KeyboardButton("Среда")
		btn44 = types.KeyboardButton("Четверг")
		btn55 = types.KeyboardButton("Пятница")
		back1 = types.KeyboardButton("Назад")
		markup.add(btn11, btn22, btn33, btn44, btn55, back1)
		bot.send_message(message.chat.id, text="//////////////////", reply_markup=markup)




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




def init_db():
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
def init_db2():
	conn = sqlite3.connect('nemmy_database.db')
	cursor = conn.cursor()





if __name__ == "__main__":
	init_db2()
	init_db()
	bot.polling(none_stop=True)
