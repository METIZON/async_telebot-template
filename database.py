import sqlite3


async def create_table(name, *args, db='users'):
    dbb = sqlite3.connect(f'{db}.db')
    bd = dbb.cursor()
    bd.execute(f'''CREATE TABLE IF NOT EXISTS {name} (id integer primary key)''')
    dbb.commit()

    for arg in args[0]:
        bd.execute(f'''ALTER TABLE {name} ADD COLUMN {arg} {args[0][arg]}''')
        dbb.commit()


async def insert_values(name, chatid, *args, db='users'):
    insert_db = sqlite3.connect(f'{db}.db')
    insert_bd = insert_db.cursor()
    insert_bd.execute(f'''INSERT INTO {name}(chatid) VALUES ({chatid})''')
    insert_db.commit()

    for arg in args[0]:
        insert_bd.execute(f'''UPDATE {name} SET {arg} = (?) WHERE chatid = (?)''', (args[0][arg], chatid))
        insert_db.commit()


async def update_values(name, chatid, *args):
    update_db = sqlite3.connect('users.db')
    update_bd = update_db.cursor()
    for arg in args[0]:
        update_bd.execute(f'''UPDATE {name} SET {arg} = (?) WHERE chatid = (?)''', (args[0][arg], chatid))
        update_db.commit()


async def update_values_wkey(name, keyy, *args, db='users'):
    update_db = sqlite3.connect(f'{db}.db')
    update_bd = update_db.cursor()
    for arg in args[0]:
        update_bd.execute(f'''UPDATE {name} SET {arg} = (?) WHERE {list(keyy.keys())[0]} = (?)''', (args[0][arg], keyy[list(keyy.keys())[0]]))
        update_db.commit()


async def update_values_with_key(name, keyy, *args):
    update_db = sqlite3.connect('users.db')
    update_bd = update_db.cursor()
    for arg in args[0]:
        update_bd.execute(f'''UPDATE {name} SET {arg} = (?) WHERE {list(keyy.keys())[0]} = (?)''', (args[0][arg], keyy[list(keyy.keys())[0]]))
        update_db.commit()


async def select_values(name, chatid):
    select_db = sqlite3.connect('users.db')
    select_bd = select_db.cursor()
    select_bd.execute(f'''SELECT * FROM {name} WHERE chatid = (?)''', (chatid, ))
    value = select_bd.fetchall()

    return value


async def select_value_by_key(name, key, value, db='users'):
    select_db = sqlite3.connect(f'{db}.db')
    select_bd = select_db.cursor()
    select_bd.execute(f'''SELECT * FROM {name} WHERE {key} = (?)''', (value, ))
    kvalue = select_bd.fetchall()

    return kvalue


async def select_all_values(name, db='users'):
    select_db = sqlite3.connect(f'{db}.db')
    select_bd = select_db.cursor()
    select_bd.execute(f'''SELECT * FROM {name}''')
    values = select_bd.fetchall()

    return values


async def get_order_by(name, key, mode='DESC'):
    order_db = sqlite3.connect('users.db')
    order_bd = order_db.cursor()
    order_bd.execute(f'''SELECT * FROM {name} ORDER BY {key} {mode}''')
    orders = order_bd.fetchall()

    return orders


async def rename_column(table, old_column, new_column):
    rename_db = sqlite3.connect('users.db')
    rename_bd = rename_db.cursor()
    rename_bd.execute(f'''ALTER TABLE {table} RENAME COLUMN {old_column} to {new_column}''')
    rename_db.commit()


async def get_orders_with_id(name, key):
    select_id_db = sqlite3.connect('users.db')
    select_id_bd = select_id_db.cursor()
    select_id_bd.execute(f'''SELECT id, {key} FROM {name}''')
    valuess = select_id_bd.fetchall()

    return valuess


async def delete_column(table, column, db='users'):
    delete_db = sqlite3.connect(f'{db}.db')
    delete_bd = delete_db.cursor()
    delete_bd.execute(f'''ALTER TABLE {table} DROP COLUMN {column}''')
    delete_db.commit()


async def delete_row(table, key, value, db='users'):
    delete_db = sqlite3.connect(f'{db}.db')
    delete_bd = delete_db.cursor()
    delete_bd.execute(f'''DELETE from {table} where {key}={value}''')
    delete_db.commit()


async def add_rows(name, *args, db='users'):
    dbb = sqlite3.connect(f'{db}.db')
    bd = dbb.cursor()

    for arg in args[0]:
        bd.execute(f'''ALTER TABLE {name} ADD COLUMN {arg} {args[0][arg]}''')
        dbb.commit()


if __name__ == '__main__':
    NotImplemented
