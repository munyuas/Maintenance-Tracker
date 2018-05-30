from app import app
import unittest



class FlaskTestCase(unnittest.TestCase):
    
    #Ensures that Flask Loads correctly
    def test_index_page(self):
        tester = app.test_client(self)
        response = tester.get('/index', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        
      #Ensures that the login page loads correctly
    def test_signin_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/signin', content_type='html/text')
        self.assertTrue (b'Sign In' in response.data)
        
    
    
    
    
if __name__ == '__main__':
unittest.main()
    
    
    
    