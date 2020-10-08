from aiohttp import web
from .routes import setup_routes
import aiohttp_jinja2
import jinja2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


async def load_app(config: dict):
    app = web.Application()
    app['config'] = config  # сохранение конфигурации в словаре приложения
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.PackageLoader('skytrack', 'templates')  # загрузка шаблонов
    )
    setup_routes(app)
    app.on_startup.append(start)  # открытие и закрытие соединения
    app.on_cleanup.append(close)
    return app


async def start(app):
    config = app['config']
    eng = create_engine(config['db_parameters'])
    app['database'] = sessionmaker(bind=eng)  # добавление объекта подключения в словарь приложения


async def close(app):
    app['database'].close()
