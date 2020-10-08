from sqlalchemy import (
    Table, Text, Integer, MetaData, Column, TIMESTAMP, ForeignKey
)

__all__ = ('user', 'shop', 'order', 'book', 'order_item')

meta = MetaData()

user = Table(
    'User', meta,
    Column('id', Integer, primary_key=True),
    Column('name', Text),
    Column('surname', Text),
    Column('fathers_name', Text),
    Column('email', Text)
)

shop = Table(
    'Shop', meta,
    Column('id', Integer, primary_key=True),
    Column('name', Text),
    Column('address', Text),
    Column('post_code', Text),
)

book = Table(
    'Book', meta,
    Column('id', Integer, primary_key=True),
    Column('name', Text),
    Column('author', Text),
    Column('isbn', Text),
)

order = Table(
    'Order', meta,
    Column('id', Integer, primary_key=True),
    Column('reg_date', TIMESTAMP),
    Column('user_id', Integer, ForeignKey('User.id')),
)

order_item = Table(
    'OrderItem', meta,
    Column('id', Integer, primary_key=True),
    Column('order_id', Integer, ForeignKey('Order.id')),
    Column('book_id', Integer, ForeignKey('Book.id')),
    Column('book_quantity', Integer),
    Column('shop_id', Integer, ForeignKey('Shop.id')),
)
