import unittest
from longestConsecutiveSeq import longestConsecutive


class longTest(unittest.TestCase):
    def test_long(self):
        myList = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
        result = longestConsecutive(myList)
        self.assertEqual(result, 9)

    def test_long_not_equal(self):
        myList = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
        result = longestConsecutive(myList)
        self.assertNotEqual(result, 8)


if __name__ == '__main__':
    unittest.main()
