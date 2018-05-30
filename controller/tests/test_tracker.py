from app import app
import unittest



class FlaskTestCase(unnittest.TestCase):
    
    #Ensures that Flask Loads correctly
    def test_index_page(self):
        tester = app.test_client(self)
        response = tester.get('/index', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        
      #Tests that the sign in page loads correctly
    def test_signin_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/signin', content_type='html/text')
        self.assertTrue (b'Sign In' in response.data)
        
    #Tests that sign in works
    def test_authentication(self):
        tester = app.test_client(self)
        response = tester.post('/sigin', data = dict{username="simon", password="simon123"}, follow_redirects=True)
        self.assertIn(b'welcome', response.data)
        
     #Tests that login fails
    def test_l(self):
        tester = app.test_client(self)
        response = tester.post('/sigin', data = dict{username="fail", password="fail"}, follow_redirects=True)
        self.assertIn(b'signin', response.data)
    
    
if __name__ == '__main__':
unittest.main()
    
    
    
    