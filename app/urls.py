from sockjs.tornado import SockJSRouter

from app.handlers import HelloHandler
from app.socket_connection import MainConnection


socket_router = SockJSRouter(MainConnection, '/echo')


routes = socket_router.urls + [
    (r'/', HelloHandler)
]


