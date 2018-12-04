import unittest
from flaskapp import create_app


class FlaskTestCase(unittest.TestCase):
    """
    Test flask views
    """

    def setUp(self):
        self.app = create_app("config.TestingConfig")
        self.client = self.app.test_client()

    def test_get_data_index(self):
        response = self.client.get('/data/')
        self.assertEqual(response.status_code, 200)
