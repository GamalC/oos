import requests
import unittest
import json
import redis
from urllib import quote_plus as urlquote

SERVER_URL = 'http://localhost:5000'
r = redis.Redis('localhost')

class OOSAPITests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def test_create_item(self):
        url_endpoint = "/item/-1"
        item_data = {"type": "song", "title": "My Song",
                     "content": "This is my song, the coolest song eveeer"}
        #Test Item is created
        req = requests.post(SERVER_URL + url_endpoint, data = item_data)
        resp = json.loads(req.text)
        iid = resp["id"] if resp else ""
        self.assetEqual(r.get("item:%s:type" % iid), "song")
        self.assetEqual(r.get("item:%s:title" % iid), "My Song")
        self.assetEqual(r.get("item:%s:content" % iid),
                        "This is my song, the coolest song eveeer")
        
def test_suite():
    suite = unittest.TestSuite()
    #Test best carried out in isolation as a previous test may change data that makes a later
    #test fail.
    oos_api_tests= [
        OOSAPITests("test_create_item")
        ]

    suite.addTests(oos_api_tests)
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')    
