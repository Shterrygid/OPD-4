import unittest
from app import app

class TestFindMostCommonWord(unittest.TestCase):
    def test_most_common_word(self):
        with app.test_client() as client:
            response = client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data, b'Самое частое слово: vel')

if __name__ == '__main__':
    unittest.main()