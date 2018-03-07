import falcon

from hello.hello_resource import HelloResource


class HelloApi(falcon.API):
    def __init__(self):
        super(HelloApi, self).__init__()

        self.add_route("/", HelloResource())

    def start(self):
        """ A hook to when a Gunicorn worker calls run()."""
        pass

    def stop(self, signal):
        """ A hook to when a Gunicorn worker starts shutting down. """
        pass
