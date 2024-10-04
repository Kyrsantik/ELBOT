import sqlite3


# НЕЕЕЕЕЧЕТНАЯ НЕДЕЛЯ
# Устанавливаем соединение с базой данных
connection = sqlite3.connect('nemmy_database.db')
cursor = connection.cursor()
cursor.execute("""
DROP TABLE IF EXISTS Users
""")

# Создаем таблицу Понедельник
cursor.execute("""
DROP TABLE IF EXISTS Понедельник
""")
cursor.execute('''
CREATE TABLE IF NOT EXISTS Понедельник (
номерпары INTEGER PRIMARY KEY,
название_пары TEXT NOT NULL,
учитель TEXT NOT NULL,
кабинет TEXT NOT NULL
)
''')
cursor.execute('INSERT INTO Понедельник (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('1', '-', '-', '-' ))
cursor.execute('INSERT INTO Понедельник (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('2', '-', '-', '-' ))
cursor.execute('INSERT INTO Понедельник (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('3', '-', '-', '-' ))
cursor.execute('INSERT INTO Понедельник (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('4', '-', '-', '-' ))
cursor.execute('INSERT INTO Понедельник (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('5', 'Основы баз данных', 'Римка', '216' ))
cursor.execute('INSERT INTO Понедельник (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('6', 'Архитектура аппаратных средств', 'Римка', '216' ))
cursor.execute('INSERT INTO Понедельник (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('7', '-', '-', '-' ))

# Создаем таблицу Вторник
cursor.execute("""
DROP TABLE IF EXISTS Вторник
""")
cursor.execute('''
CREATE TABLE IF NOT EXISTS Вторник (
номерпары INTEGER PRIMARY KEY,
название_пары TEXT NOT NULL,
учитель TEXT NOT NULL,
кабинет TEXT NOT NULL
)
''')
cursor.execute('INSERT INTO Вторник (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('1', '-', '-', '-' ))
cursor.execute('INSERT INTO Вторник (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('2', '-', '-', '-' ))
cursor.execute('INSERT INTO Вторник (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('3', '-', '-', '-' ))
cursor.execute('INSERT INTO Вторник (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('4', 'История', 'Римка', '216' ))
cursor.execute('INSERT INTO Вторник (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('5', 'Информационные технологии', 'Римка', '216' ))
cursor.execute('INSERT INTO Вторник (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('6', 'Английский', 'Римка', '216' ))
cursor.execute('INSERT INTO Вторник (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('7', 'Основы алгоритмизации', 'Римка', '216' ))
#Создаем таблицу Среда
cursor.execute("""
DROP TABLE IF EXISTS Среда
""")
cursor.execute('''
CREATE TABLE IF NOT EXISTS Среда (
номерпары INTEGER PRIMARY KEY,
название_пары TEXT NOT NULL,
учитель TEXT NOT NULL,
кабинет TEXT NOT NULL
)
''')
cursor.execute('INSERT INTO Среда (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('1', '-', '-', '-' ))
cursor.execute('INSERT INTO Среда (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('2', 'Архитектура аппаратных средств', 'Римка', '216' ))
cursor.execute('INSERT INTO Среда (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('3', 'Основы проектной деятельности', 'Римка', '216' ))
cursor.execute('INSERT INTO Среда (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('4', 'Матеша', 'Римка', '216' ))
cursor.execute('INSERT INTO Среда (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('5', '-', '-', '-' ))
cursor.execute('INSERT INTO Среда (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('6', '-', '-', '-' ))
cursor.execute('INSERT INTO Среда (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('7', '-', '-', '-' ))
#Создаем таблицу Четверг
cursor.execute("""
DROP TABLE IF EXISTS Четверг
""")
cursor.execute('''
CREATE TABLE IF NOT EXISTS Четверг (
номерпары INTEGER PRIMARY KEY,
название_пары TEXT NOT NULL,
учитель TEXT NOT NULL,
кабинет TEXT NOT NULL
)
''')
cursor.execute('INSERT INTO Четверг (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('1', '-', '-', '-' ))
cursor.execute('INSERT INTO Четверг (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('2', 'Основы баз данных', 'Римка', '216' ))
cursor.execute('INSERT INTO Четверг (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('3', 'Архитектура аппаратных средств', 'Римка', '216' ))
cursor.execute('INSERT INTO Четверг (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('4', 'компьютерные сети', 'Римка', '216' ))
cursor.execute('INSERT INTO Четверг (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('5', 'Основы баз данных', 'Римка', '216' ))
cursor.execute('INSERT INTO Четверг (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('6', 'Основы баз данных', 'Римка', '216' ))
cursor.execute('INSERT INTO Четверг (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('7', 'Матеша', 'Римка', '216' ))
#Создаем таблицу Пятница
cursor.execute("""
DROP TABLE IF EXISTS Пятница
""")
cursor.execute('''
CREATE TABLE IF NOT EXISTS Пятница (
номерпары INTEGER PRIMARY KEY,
название_пары TEXT NOT NULL,
учитель TEXT NOT NULL,
кабинет TEXT NOT NULL
)
''')
cursor.execute('INSERT INTO Пятница (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('1', '-', '-', '-' ))
cursor.execute('INSERT INTO Пятница (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('2', '-', '-', '-' ))
cursor.execute('INSERT INTO Пятница (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('3', 'Психология', 'Римка', '216' ))
cursor.execute('INSERT INTO Пятница (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('4', 'Психология', 'Римка', '216' ))
cursor.execute('INSERT INTO Пятница (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('5', 'Физра', 'Римка', '216' ))
cursor.execute('INSERT INTO Пятница (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('6', 'Матан', 'Римка', '216' ))
cursor.execute('INSERT INTO Пятница (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('7', '-', '-', '-' ))

def read_sqlite_table(records):
    try:
        sqlite_connection = sqlite3.connect('nemmy_database.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")







        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)

read_sqlite_table("")



# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()