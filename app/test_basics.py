import os
import unittest

from flaskapp import app
from redis import Redis

class BasicTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
    def tearDown(self):
        pass
        
    # actual tests
    def test_welcome_page_is_working(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
    
    # another test
    def test_redi_counter_increment_is_working(self):
        redis = Redis(host="redis-server",db=0)
        self.app.get('/visit')
        self.assertEqual(int(redis.get("counter")),1)
        
if __name__== "__main__":
    unittest.main()