from tornado import web, ioloop

from app.settings import APPLICATION_SETTINGS
from app.urls import routes
from app.logger import get_logger


log = get_logger(__name__)


def make_app():
    return web.Application(routes, **APPLICATION_SETTINGS)


if __name__ == '__main__':
    app = make_app()
    app.listen(8001)
    log.debug('Start app')
    ioloop.IOLoop.current().start()
