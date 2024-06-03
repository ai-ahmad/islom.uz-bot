import sqlite3 

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# cursor.execute("CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, user_name TEXT, chat_id TEXT, user_region TEXT)")