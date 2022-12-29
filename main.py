from database.db import Database

table = Database(filename='database/test.db', table='todo')


# Create table

# table.create_table('''
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             title TEXT NOT NULL,
#             description TEXT
#         ''')


#  INSERT
# table.insert(title='Post 2', description='Lorem impusum')

# GET
# note = table.get(id=1)
# print(note)

# GET ALL
# notes = table.fetchmany()
# print(notes)


# UPDATE
# table.update(id=3, data={'title': 'Post 3'})

# DELETE
# table.delete(id='3')


# QUERY
# data = table.query('title', id=2)
# print(data)
