from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from pathlib import Path
import yaml
from skytrack.database import user, shop, order, book, order_item

default_file = Path(__file__).parent / 'config.yaml'  # считывание параметров бд из конфиг файла
with open(default_file, 'r') as f:
    config = yaml.safe_load(f)

eng = create_engine(config['db_parameters'])

if not database_exists(eng.url):  # проверка существования базы данных
    create_database(eng.url)


def create_table_user():
    with eng.connect() as con:
        user.create(eng)
        ins1 = user.insert().values(id=1, name='Набоков', surname='Владимир', fathers_name='Владимирович',
                                    email='nabokov@email.ru')
        con.execute(ins1)
        ins2 = user.insert().values(id=2, name='Борис', surname='Пастернак', fathers_name='Леонидович',
                                    email='pasternak@email.ru')
        con.execute(ins2)


def create_table_shop():
    with eng.connect() as con:
        shop.create(eng)
        ins1 = shop.insert().values(id=1, name='Дом книги «Молодая Гвардия»', address='Москва, ул. Б. Полянка, 28',
                                    post_code='119180')
        con.execute(ins1)
        ins2 = shop.insert().values(id=2, name='Московский Дом Книги', address='Москва, ул. Новый Арбат, 8',
                                    post_code='121069')
        con.execute(ins2)


def create_table_book():
    with eng.connect() as con:
        book.create(eng)
        ins1 = book.insert().values(id=1, name='Степной волк', author="Герман Гессе", isbn='9785170837427')
        con.execute(ins1)
        ins2 = book.insert().values(id=2, name='Игра в бисер', author="Герман Гессе", isbn='9785170828432')
        con.execute(ins2)


def create_table_order():
    with eng.connect() as con:
        order.create(eng)
        ins1 = order.insert().values(id=1, reg_date='2020-10-01 08:23:54.000000', user_id=1)
        con.execute(ins1)
        ins2 = order.insert().values(id=2, reg_date='2020-10-01 10:23:54.000000', user_id=1)
        con.execute(ins2)


def create_table_order_item():
    with eng.connect() as con:
        order_item.create(eng)
        ins1 = order_item.insert().values(id=1, order_id=1, book_id=1, book_quantity=1, shop_id=1)
        con.execute(ins1)
        ins2 = order_item.insert().values(id=2, order_id=2, book_id=2, book_quantity=1, shop_id=1)
        con.execute(ins2)


create_table_user()
create_table_shop()
create_table_book()
create_table_order()
create_table_order_item()
