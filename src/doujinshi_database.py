import os
import sqlite3

class doujinsh_database:
    default_database_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Database", "doujinshi.org.db")

    def __init__(self):
        self.__conn = None
        self.__cur = None

    def connect(self) -> None:
        self.__conn = sqlite3.connect(doujinsh_database.default_database_path)
        self.__cur = self.__conn.cursor()

    def close(self) -> None:
        self.__cur.close()
        self.__conn.close()

    def get_book_by_id(self, id:int):
        results = self.__cur.execute("SELECT * FROM Book WHERE BookId = ?", (id,))
        return results.fetchone()
    
    # temp thing to just mess around with params
    def search_book_by_name(self, name:str):
        results = self.__cur.execute("SELECT DISTINCT * FROM Book WHERE Name_EN LIKE ? OR Name_JP LIKE ? OR Name_R LIKE ?", ('%'+name+'%','%'+name+'%','%'+name+'%'))
        return results.fetchall()
    