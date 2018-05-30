import unittest
import os
import json

from app import create_app, db

TEST_DB = 'test.db'
#Test cases for requests
class Base_Tests(unittest.TestCase):
    
    #Creates a testing client
    def setUp(self):        
        tester = app.test_client(self)
        route = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
#        
class Test_Requests(unittest.TestCase):
    #Test if a client can POST
    def test_create_request_successfully(self):        
        route = tester.post('api/v1/request', data=dict (
        request_id="001",
        request_description="Fix my window", request_status="inprogress",
        request_date='30/05/2018'
        ))
        self.assertEqual(route.status_code, 201)
    
    #Test for fetching a request successfully via GET
    def test_fetch_request(self):
        route = tester.get('api/v1/request')
        self.assertEqual(route.status_code, 200)
        
    #Test for fetching all requests via GET
    def test_fetch_all_requests(self):
        route = tester.get('api/v1/request')
+       self.assertEqual(route.status_code, 200)

    #Test for modifying a request successfully
    def test_modify_request(self):
        route = tester.post('api/v1/request[request_id]', data=dict (
        request_id="001",
        request_description="Fix my window", request_status="resolved",
        request_date='30/05/2018'
        ))
        self.assertEqual(route.status_code, 200)
        
if __name__=='__main__':
unittest.main()