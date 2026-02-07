# Flask Shop tests
import unittest
from flask_shop import app, db

class FlaskShopTests(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.create_all()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()
    
    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 302)  # Redirect to login
    
    def test_login_page(self):
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
