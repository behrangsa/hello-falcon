from falcon import testing
from hello.hello_api import HelloApi


class HelloApiTest(testing.TestCase):
    def setUp(self):
        super(HelloApiTest, self).setUp()
        self.app = HelloApi()

    def test_get_root(self):
        result = self.simulate_get("/")
        self.assertEqual(result.json, {'message': 'Hello'})
