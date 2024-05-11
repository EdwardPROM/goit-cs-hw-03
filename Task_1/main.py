import psycopg2

conn = psycopg2.connect(
    database="postgres", user="postgres", host="localhost", password="mysecretpassword", port=5432
)

# Відкрити курсор для виконання операцій з базою даних
cur = conn.cursor()

# Виконати команду: створити таблицю users
cur.execute(
    """CREATE TABLE if not exists users(
            id SERIAL PRIMARY KEY,
            fullname VARCHAR (100) UNIQUE NOT NULL,
            email VARCHAR (100) UNIQUE NOT NULL);
            """
)
# Зробити зміни в базі даних постійними
conn.commit()

# Виконати команду: створити таблицю status
cur.execute(
    """CREATE TABLE if not exists status(
            id SERIAL PRIMARY KEY,
            name VARCHAR (50) UNIQUE NOT NULL);
            """
)
# Зробити зміни в базі даних постійними
conn.commit()


# Виконати команду: створити таблицю tasks
cur.execute(
    """CREATE TABLE if not exists tasks(
            id SERIAL PRIMARY KEY,
            title VARCHAR (100) NOT NULL,
            description TEXT NOT NULL,         
            status_id INT,
            user_id INT,   
            FOREIGN KEY (status_id) REFERENCES status (id)
                ON DELETE SET NULL
                ON UPDATE CASCADE,
            FOREIGN KEY (user_id) REFERENCES users (id)
                ON DELETE CASCADE
                ON UPDATE CASCADE);
            """
)
# Зробити зміни в базі даних постійними
conn.commit()

# Закрити курсор та з'єднання з базою даних
cur.close()
conn.close()