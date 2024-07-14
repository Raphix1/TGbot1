import sqlite3

conn = sqlite3.connect('delivery.db', check_same_thread=False)
sql = conn.cursor()


sql.execute('CREATE TABLE IF NOT EXISTS users '
            '(id INTEGER, name TEXT, number TEXT);')
sql.execute('CREATE TABLE IF NOT EXISTS products '
            '(pr_id INTEGER PRIMARY KEY AUTOINCREMENT, '
            'pr_name TEXT, pr_des TEXT, pr_price REAL, pr_count INTEGER, '
            'pr_photo TEXT);')
sql.execute('CREATE TABLE IF NOT EXISTS cart '
            '(user_id INTEGER, user_product TEXT, user_pr_quantity INTEGER);')


def register(user_id, user_name, user_number):
    sql.execute('INSERT INTO users VALUES(?, ?, ?);',
                (user_id, user_name, user_number))
    conn.commit()


def check_user(user_id):
    if sql.execute('SELECT * FROM users WHERE id=?;', (user_id,)).fetchone():
        return True
    else:
        return False


def get_pr_id():
    all_pr = sql.execute('SELECT pr_id, pr_name, pr_count FROM products;').fetchall()

    return all_pr


def get_all_pr():
    return sql.execute('SELECT * FROM products;').fetchall()


def get_exact_pr(pr_id):
    return sql.execute('SELECT * FROM products WHERE pr_id=?;', (pr_id,)).fetchone()


def get_pr_price(pr_name):
    return sql.execute('SELECT pr_price FROM products WHERE pr_name=?;', (pr_name,)).fetchone()



def pr_to_db(pr_name, pr_des, pr_price, pr_count, pr_photo):
    sql.execute('INSERT INTO products (pr_name, pr_des, pr_price, pr_count, pr_photo) '
                'VALUES (?, ?, ?, ?, ?);', (pr_name, pr_des, pr_price, pr_count, pr_photo))
    conn.commit()


def change_pr_attr(keyword, new_value, attr=''):
    if attr == 'name':
        sql.execute('UPDATE products SET pr_name=? WHERE pr_name=?;',
                    (new_value, keyword))
    elif attr == 'price':
        sql.execute('UPDATE products SET pr_price=? WHERE pr_name=?;',
                    (new_value, keyword))
    elif attr == 'count':
        sql.execute('UPDATE products SET pr_count=? WHERE pr_name=?;',
                    (new_value, keyword))
    elif attr == 'des':
        sql.execute('UPDATE products SET pr_des=? WHERE pr_name=?;',
                    (new_value, keyword))
    elif attr == 'photo':
        sql.execute('UPDATE products SET pr_photo=? WHERE pr_name=?;',
                    (new_value, keyword))

    conn.commit()


def del_pr(pr_name):
    sql.execute('DELETE FROM products WHERE pr_name=?;', (pr_name,))
    conn.commit()


def check_pr():
    if sql.execute('SELECT * FROM products;').fetchone():
        return True
    else:
        return False


def to_cart(user_id, user_pr, user_count):
    sql.execute('INSERT INTO cart VALUES (?, ?, ?);',
                (user_id, user_pr, user_count))
    conn.commit()


def clear_cart(user_id):
    sql.execute('DELETE FROM cart WHERE user_id=?;', (user_id,))
    conn.commit()


def make_order(user_id):
    product_names = sql.execute('SELECT user_product FROM cart WHERE user_id=?;',
                                (user_id,)).fetchall()
    product_quantities = sql.execute('SELECT user_pr_quantity '
                                     'FROM cart WHERE user_id=?;',
                                     (user_id,)).fetchall()
    product_counts = []
    totals = []
    for i in product_names:
        product_counts.append(sql.execute('SELECT pr_count FROM products '
                                          'WHERE pr_name=?;', (i[0])).fetchone()[0])

    for e in product_quantities:
        for c in product_counts:
            totals.append(c - e[0])

    for t in totals:
        for n in product_names:
            sql.execute('UPDATE products SET pr_count=? WHERE pr_name=?;',
                        (t, n[0]))

    conn.commit()
    return product_counts, totals


def show_cart(user_id):
    return sql.execute('SELECT * FROM cart WHERE user_id=?;', (user_id,)).fetchall()