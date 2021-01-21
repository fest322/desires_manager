import pymysql
from pymysql.cursors import DictCursor
from application.configParse.config_read import Config


class DataBase:
    def __init__(self):
        self.conf = Config('passwd.ini')
        self.user = self.conf.getSetting('DataBase', 'user')
        self.password = self.conf.getSetting('DataBase', 'password')
        self.host = self.conf.getSetting('DataBase', 'host')
        self.name_bd = self.conf.getSetting('DataBase', 'name_bd')
        self.__conn = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            charset='utf8mb4',
            cursorclass=DictCursor,
            database='desire',
        )
        self.__cursor = self.__conn.cursor()
        self.create_db()
        self.connect_to_bd()
        self.create_table()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @property
    def connection(self):
        return self.__conn

    @property
    def cursor(self):
        return self.__cursor

    def commit(self):
        self.connection.commit()

    def close(self, commit=True):
        if commit:
            self.commit()
        self.connection.close()

    def execute(self, sql):
        self.cursor.execute(sql)

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def query(self, sql):
        self.execute(sql)
        return self.fetchall()

    def connect_to_bd(self):
        self.__conn = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            charset='utf8mb4',
            cursorclass=DictCursor,
            database=self.name_bd,
        )
        self.__cursor = self.__conn.cursor()

    def create_db(self):
        query = f'Create DATABASE if not exists {self.name_bd}'
        self.execute(query)
        self.commit()
        self.close()

    def create_table(self):
        query = 'CREATE TABLE IF NOT EXISTS desire (' \
                'id_desire int PRIMARY KEY AUTO_INCREMENT, ' \
                'name varchar(16), ' \
                'cost DECIMAL(10,2), ' \
                'link text, ' \
                'note text);'
        self.execute(query)
        self.commit()
        self.close()
