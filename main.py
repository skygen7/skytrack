import argparse
from skytrack.app import load_app
from aiohttp import web
from settings import load_config

# Настройки хоста проекта
parser = argparse.ArgumentParser(description="Demo project")
parser.add_argument('--host', help="Host to listen", default="127.0.0.1")
parser.add_argument('--port', help="Port to accept connections", default=8080)
parser.add_argument("-c", "--config", type=argparse.FileType('r'))   # добавление конфигурационного файла

args = parser.parse_args()

app = load_app(config=load_config(args.config))

if __name__ == '__main__':
    web.run_app(app, host=args.host, port=args.port)
