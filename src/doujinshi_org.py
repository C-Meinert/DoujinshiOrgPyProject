from doujinshi_database import doujinsh_database

db = None

try:
    db = doujinsh_database()
    db.connect()
    print(db.get_book_by_id(1))
    print(db.search_book_by_name("ディアマイシスターアンド"))
except Exception as e:
    print(f"Stuff happens\n{e}")
finally:
    if db is not None:
        db.close()