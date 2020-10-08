from aiohttp_jinja2 import template
from .database import user, shop, book, order, order_item


@template('shop_list.html')
async def shop_list(request):
    session = request.app['database']()
    shops = ''

    for row in session.query(shop).all():
        shops += f'{row.name} {row.address} ' \
                    f'<a href="/shop_list/{row.id}">Ассортимент</a> <br> '

    return {'shops': shops}


@template('profile.html')
async def profile(request):
    session = request.app['database']()
    res = session.query(user).filter(user.c.id == request.match_info['name'])
    info = f"{res[0].name} {res[0].surname} {res[0].fathers_name}<br>{res[0].email}"
    orders = f"""<a href="/{request.match_info['name']}/history">Мои заказы</a>"""

    return {'info': info,
            'orders': orders}


@template('history.html')
async def history(request):
    session = request.app['database']()
    orders = ''

    for row in session.query(order).filter(order.c.user_id == request.match_info['name']).all():
        orders += f"""<a href="/{request.match_info['name']}/history/{row.id}">
        Заказ № {row.id}</a> {row.reg_date}<br>"""

    return {'orders': orders}


@template('order.html')
async def order_history(request):
    session = request.app['database']()
    subq = session.query(order_item).filter(order_item.c.order_id == request.match_info['name1']).subquery()

    res = session.query(
        book.c.name.label('book_name'), book.c.author, subq.c.book_quantity, shop.c.name.label('shop_name'),
        shop.c.address
    ).filter(order.c.id == subq.c.order_id).filter(book.c.id == subq.c.book_id).filter(shop.c.id == subq.c.shop_id)

    info = f"Товар: {res[0].book_name} {res[0].author}<br>Количество: {res[0].book_quantity}<br>" \
           f"Магазин: {res[0].shop_name} ({res[0].address})"

    return {'order': request.match_info['name1'],
            'info': info}


@template('assortment.html')
async def shop_assortment(request):
    session = request.app['database']()
    res = session.query(book.c.name, book.c.author, book.c.isbn).filter(shop.c.id == request.match_info['name'])
    assortment = ''

    for row in res.all():
        assortment += f"{row.name} {row.author}<br>"

    return {'assortment': assortment}


@template('index.html')
async def hello(request):
    name = request.app['config'].get('name')
    personal_page = f'<a href="/1">Личный кабинет</a>'
    shops = '<a href="/shop_list">Список магазинов</a>'
    return {'name': name,
            'personal_page': personal_page,
            'shops': shops}
