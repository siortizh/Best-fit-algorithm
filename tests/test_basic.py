# Tests
import unittest

class TestBasic(unittest.TestCase):

    def test_not_found(self):
        self.assertEqual('1','1')

if __name__ == '__main__':
    unittest.main()

