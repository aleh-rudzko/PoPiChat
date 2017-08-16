from sockjs.tornado import SockJSConnection


class MainConnection(SockJSConnection):
    def on_open(self, info):
        print('Client connected')

    def on_message(self, msg):
        print('Got', msg)
        self.send(msg)

    def on_close(self):
        print('Client disconnected')