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
        

if __name__=='__main__':
unittest.main()