import unittest
import os
import json

from app import create_app, db


class PulllistTestCase(unittest.TestCase):
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.pulllist = {'name': 'My first pull list'}

        with self.app.app_context():
            db.create_all()

    def test_pulllist_create(self):
        res = self.client().post('/pulllists/', data=self.pulllist)
        self.assertEqual(res.status_code, 201)
        self.assertIn('My first pull list', str(res.data))

if __name__ == "__main__":
    unittest.main()
