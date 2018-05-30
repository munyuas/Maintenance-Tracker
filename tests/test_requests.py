import unittest
from app import app

#Test cases for requests
class Test_Requests(unittest.TestCase):
    
    #Creates a testing client
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True 
    
    #Test if a client can POST
    def test_create_request_successfully(self):        
        route = self.client.post('http://[hostname]/requests/api/v3/requests[request_id]', data=dict (
        request_id="001",
        request="Bad Internet Connection",
        request_type="Please repair"
        ))
        self.assertEqual(route.status_code, 201)
    
    #Test for fetching a request successfully via GET
    def test_fetch_request(self):
        route = self.client.get('http://[hostname]/requests/api/v2/requests[request_id]')
        self.assertEqual(route.status_code, 200)
        
    #Test for fetching all requests via GET
    def test_fetch_all_requests(self):
        route = self.client.get('http://[hostname]/request/api/v1/requests')
+       self.assertEqual(route.status_code, 200)

    

if __name__=='__main__':
unittest.main()