from telebot import types
import database as db


def num_button():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton('Отправить номер📞', request_contact=True)
    kb.add(but1)
    return kb


def loc_button():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton('Отправить локацию🌎', request_location=True)
    kb.add(but1)
    return kb


def main_menu(products):
    kb = types.InlineKeyboardMarkup(row_width=2)
    cart = types.InlineKeyboardButton(text='Корзина', callback_data='cart')
    all_products = [types.InlineKeyboardButton(text=f'{i[1]}',
                                               callback_data=f'{i[0]}')
                    for i in products if i[2] > 0]
    kb.add(*all_products)
    kb.row(cart)
    return kb


def choose_pr_count(pr_amount, plus_or_minus='', amount=1):
    kb = types.InlineKeyboardMarkup(row_width=3)
    minus = types.InlineKeyboardButton(text='-', callback_data='decrement')
    count = types.InlineKeyboardButton(text=str(amount), callback_data=str(amount))
    plus = types.InlineKeyboardButton(text='+', callback_data='increment')
    to_cart = types.InlineKeyboardButton(text='В корзину', callback_data='to_cart')
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    if plus_or_minus == 'increment':
        if amount < pr_amount:
            count = types.InlineKeyboardButton(text=str(amount + 1), callback_data=amount)
    elif plus_or_minus == 'decrement':
        if amount > 1:
            count = types.InlineKeyboardButton(text=str(amount - 1), callback_data=amount)
    kb.add(minus, count, plus)
    kb.row(to_cart, back)
    return kb


def cart_buttons():
    kb = types.InlineKeyboardMarkup(row_width=2)
    order = types.InlineKeyboardButton(text='Оформить заказ',
                                       callback_data='order')
    clear = types.InlineKeyboardButton(text='Очистить корзину',
                                       callback_data='clear')
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    kb.add(order, clear)
    kb.row(back)
    return kb


def admin_menu():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton('Добавить товар')
    but2 = types.KeyboardButton('Удалить товар')
    but3 = types.KeyboardButton('Изменить товар')
    but4 = types.KeyboardButton('В главное меню')
    kb.add(but1, but2, but3)
    kb.row(but4)
    return kb


def admin_pr(products):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    all_products = [types.KeyboardButton(f'{i[1]}') for i in products]
    back = types.KeyboardButton('Назад')
    kb.add(all_products)
    kb.row(back)
    return kb


def change_buttons():
    kb = types.InlineKeyboardMarkup(row_width=2)
    name = types.InlineKeyboardButton(text='Название',
                                      callback_data='name')
    des = types.InlineKeyboardButton(text='Описание',
                                     callback_data='des')
    count = types.InlineKeyboardButton(text='Количество',
                                       callback_data='count')
    price = types.InlineKeyboardButton(text='Цена',
                                       callback_data='price')
    photo = types.InlineKeyboardButton(text='Фото',
                                       callback_data='photo')
    back = types.InlineKeyboardButton(text='Назад',
                                      callback_data='back')
    kb.row(name)
    kb.add(des, count, price, photo)
    kb.row(back)
    return kb


def confirm_buttons():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    yes = types.KeyboardButton('Да')
    no = types.KeyboardButton('Нет')
    kb.add(yes, no)
    return kb