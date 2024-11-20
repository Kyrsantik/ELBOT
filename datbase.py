import sqlite3


# ЧЕТНАЯ НЕДЕЛЯ
# Устанавливаем соединение с базой данных
connection = sqlite3.connect('my_database.db')
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
cursor.execute('INSERT INTO Понедельник (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('3', 'Физкультура', 'Телешов', 'зал' ))
cursor.execute('INSERT INTO Понедельник (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('4', 'Английский', 'Власова', '428' ))
cursor.execute('INSERT INTO Понедельник (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('5', 'Основы баз данных', 'Типикина', '518' ))
cursor.execute('INSERT INTO Понедельник (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('6', '-', '-', '-' ))
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
cursor.execute('INSERT INTO Вторник (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('2', 'Матеша', 'Бегракян', '227' ))
cursor.execute('INSERT INTO Вторник (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('3', 'Основы алгоритмизации', 'Марченкова', '619' ))
cursor.execute('INSERT INTO Вторник (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('4', 'Основы проектной деятельности', 'Мохначева', '628' ))
cursor.execute('INSERT INTO Вторник (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('5', '-', '-', '-' ))
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
cursor.execute('INSERT INTO Среда (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('2', '-', '-', '-' ))
cursor.execute('INSERT INTO Среда (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('3', '-', '-', '-' ))
cursor.execute('INSERT INTO Среда (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('4', 'МДК_0101', 'Хасуев', '512' ))
cursor.execute('INSERT INTO Среда (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('5', 'Психология', 'Волошина', '204' ))
cursor.execute('INSERT INTO Среда (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('6', 'История', 'Римка', '614' ))
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
cursor.execute('INSERT INTO Четверг (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('2',  '-', '-', '-' ))
cursor.execute('INSERT INTO Четверг (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('3', 'Архитектура аппаратных средств', 'Мозговой', '518' ))
cursor.execute('INSERT INTO Четверг (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('4', 'компьютерные сети', 'Караева', '513' ))
cursor.execute('INSERT INTO Четверг (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('5', 'МДК_0101', 'Хасуев', '515' ))
cursor.execute('INSERT INTO Четверг (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('6', 'МДК_0101', 'Хасуев', '515' ))
cursor.execute('INSERT INTO Четверг (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('7', '-', '-', '-' ))
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
cursor.execute('INSERT INTO Пятница (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('4', '-', '-', '-' ))
cursor.execute('INSERT INTO Пятница (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('5', 'Матан', 'Бегракян', '401' ))
cursor.execute('INSERT INTO Пятница (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('6', 'Архитектура аппаратных средств', 'Мозговой', '518' ))
cursor.execute('INSERT INTO Пятница (номерпары, название_пары, учитель, кабинет) VALUES (?, ?, ?, ?)', ('7', '-', '-', '-' ))

def read_sqlite_table(records):
    try:
        sqlite_connection = sqlite3.connect('my_database.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_select_query = """SELECT * from Вторник"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()

        #for row in records:
          #  print("Номер пары:", row[0],"название", row[1],"препод:", row[2],"кабинет:", row[3],)
          #  """print("название", row[1])
           # print("препод:", row[2])
           # print("кабинет:", row[3], )"""


        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)

read_sqlite_table("")



# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()
