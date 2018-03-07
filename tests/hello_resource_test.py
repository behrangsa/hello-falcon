import unittest

from falcon import Response

from hello.hello_resource import HelloResource


class HelloResourceTest(unittest.TestCase):
    def test_on_get(self):
        resp = Response()
        hello_resource = HelloResource()
        hello_resource.on_get(None, resp)
        self.assertEqual(resp.media, {'message': 'Hello'})
