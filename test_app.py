import unittest
from app import greet

class TestApp(unittest.TestCase):

    def test_greet(self):
        result = greet("Saravanan")
        self.assertEqual(result, "Hello, Saravanan!")

if __name__ == "__main__":
    unittest.main()
