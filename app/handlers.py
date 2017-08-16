from tornado import web


class HelloHandler(web.RequestHandler):

    def get(self):
        self.render('base.html')
