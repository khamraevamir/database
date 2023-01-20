import sqlite3


class Database:

    def __init__(self, **kwargs):
        self._db = sqlite3.connect(kwargs.get('filename'))
        self._table = kwargs.get('table')
        self._cursor = self._db.cursor()

    def create_table(self, sql):
        self._cursor.execute(f'''CREATE TABLE IF NOT EXISTS {self._table}({sql})''')

    def insert(self, **kwargs):
        keys = ', '.join([key for key in kwargs.keys()])
        values = [value for value in kwargs.values()]
        quantity = ', '.join(['?' for i in range(0, len(kwargs))])
        sql = f'INSERT INTO {self._table} ({keys}) VALUES ({quantity})'
        self._cursor.execute(sql, tuple(values))
        self._db.commit()

    def update(self, id, data):
        keys = ', '.join([key + ' = ?' for key in data.keys()])
        values = [value for value in data.values()]
        sql = f'UPDATE {self._table} SET {keys} WHERE id = {id}'
        self._cursor.execute(sql, tuple(values))
        self._db.commit()

    def delete(self, id):
        sql = f'DELETE FROM {self._table} WHERE id = ?'
        self._cursor.execute(sql, tuple(str(id), ))
        self._db.commit()

    def query(self, *args, **kwargs):
        columns = ', '.join(args) if len(args) != 0 else '*'
        if kwargs:
            get_by = ', '.join([f"{key} = '{value}' " for key, value in kwargs.items()])
            sql = f'SELECT {columns} FROM {self._table} WHERE {get_by}'
        else:
            sql = f'SELECT {columns} FROM {self._table}'
        data = self._cursor.execute(sql)
        keys = [key[0] for key in data.description]
        result = [{keys[index]: value for index, value in enumerate(item)} for item in list(data)]
        return  result


    def __enter__(self):
        # make a database connection and return it
        return self._db

    def __exit__(self, ext_type, exc_value, traceback):
        # make sure the database connection gets closed
        self._cursor.close()
        if isinstance(exc_value, Exception):
            self._db.rollback()
        else:
            self._db.commit()
        self._db.close()

