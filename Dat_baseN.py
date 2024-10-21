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
cursor.execute('INSERT INTO Понедельник (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('5', 'Матеша', 'Бегракян', '215' ))
cursor.execute('INSERT INTO Понедельник (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('6', 'Архитектура аппаратных средств', 'Мозговой', '518' ))
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
cursor.execute('INSERT INTO Вторник (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('2', 'Основы алгоритмизации', 'Марченкова', '54' ))
cursor.execute('INSERT INTO Вторник (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('3', 'Информационные технологии', 'Грибова', '615' ))
cursor.execute('INSERT INTO Вторник (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('4', 'История', 'Римка', '620' ))
cursor.execute('INSERT INTO Вторник (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('5', 'МДК 0101', 'Хасуев', '516' ))
cursor.execute('INSERT INTO Вторник (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('6', '-', '-', '-' ))
cursor.execute('INSERT INTO Вторник (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('7', '-', '-', '-' ))
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
cursor.execute('INSERT INTO Среда (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('2','-', '-', '-' ))
cursor.execute('INSERT INTO Среда (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('3', 'Основы проектной деятельности', 'Мохначева', '628' ))
cursor.execute('INSERT INTO Среда (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('4', 'Матеша', 'Бегракян', '415' ))
cursor.execute('INSERT INTO Среда (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('5', 'МДК 0101', 'Хасуев', '619' ))
cursor.execute('INSERT INTO Среда (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('6', 'МДК 0101', 'Хасуев', '619' ))
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
cursor.execute('INSERT INTO Четверг (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('2', '-', '-', '-' ))
cursor.execute('INSERT INTO Четверг (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('3', 'Инглиш', 'Власова', '512' ))
cursor.execute('INSERT INTO Четверг (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('4', 'Основы баз данных', 'Типкина', '627' ))
cursor.execute('INSERT INTO Четверг (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('5', 'Основы баз данных', 'Типкина', '627' ))
cursor.execute('INSERT INTO Четверг (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('6',  '-', '-', '-' ))
cursor.execute('INSERT INTO Четверг (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('7',  '-', '-', '-' ))
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
cursor.execute('INSERT INTO Пятница (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('3', '-', '-', '-' ))
cursor.execute('INSERT INTO Пятница (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('4', 'Психология', 'Волошина', '204' ))
cursor.execute('INSERT INTO Пятница (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('5', 'Физра', 'Телешов', 'зал' ))
cursor.execute('INSERT INTO Пятница (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('6', 'История', 'Римка', '205' ))
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
