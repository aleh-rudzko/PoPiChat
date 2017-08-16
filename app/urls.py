from sockjs.tornado import SockJSRouter

from app.handlers import HelloHandler
from app.socket import MainConnection


socket_router = SockJSRouter(MainConnection, '/echo')


routes = socket_router.urls + [
    (r'/', HelloHandler)
]


