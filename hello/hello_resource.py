class HelloResource:
    def on_get(self, req, resp):
        """Says hello"""

        resp.media = {
            'message': 'Hello'
        }
