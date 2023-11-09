import sqlite3
import csv
# Создание базы данных SQLite и таблицы
conn = sqlite3.connect('example.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')

# Заполнение таблицы данными из файла CSV
# Создание и запись данных в файл CSV
with open('users.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['name', 'email'])
    csv_writer.writerow(['Alex Fish', 'Tarantino@example.com'])
    csv_writer.writerow(['Anton Tower', 'UbicaApples@example.com'])

# Заполнение таблицы данными из файла CSV
with open('users.csv', 'r') as file:
    csv_data = csv.reader(file)
    next(csv_data)  # Пропуск заголовка
    for row in csv_data:
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", row)
        
# Извлечение данных из таблицы и вывод на экран
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Закрытие соединения с базой данных
conn.commit()
conn.close()
