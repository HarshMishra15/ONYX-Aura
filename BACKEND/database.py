import sqlite3

# Connect to SQLite database (or create it)
conn = sqlite3.connect('store.db')

# Create a cursor object
cursor = conn.cursor()

# Create products table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        description TEXT NOT NULL,
        image_url TEXT
    )
''')

# Commit changes and close connection
conn.commit()
conn.close()