import sqlite3

connection = sqlite3.connect('sqlite (1).db')
cursor = connection.cursor()
#cursor.execute('DROP TABLE comment')
cursor.execute('''
    CREATE TABLE comment (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        post_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        content TEXT NOT NULL);
    ''')

connection.commit()
connection.close()