from . import view
from aiohttp import web


def setup_routes(app):
    app.add_routes([web.get('/', view.hello),
                    web.get('/shop_list', view.shop_list),
                    web.get('/{name}', view.profile),
                    web.get('/{name}/history', view.history),
                    web.get('/{name}/history/{name1}', view.order_history),
                    web.get('/shop_list/{name}', view.shop_assortment),
                    ])
