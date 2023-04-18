import unittest
from palindrome import palindrome

class TestPalindrome(unittest.TestCase):
    def test1(self):
        result = palindrome('neuquen')
        self.assertEqual(result, True)

    def test2(self):
        result = palindrome("mundo")
        self.assertEqual(result, False)

    def test3(self):
        result = palindrome("oso")
        self.assertEqual(result, True)

    def test4(self):
        result = palindrome("RADAR")
        self.assertEqual(result, True)

    def test5(self):
        result = palindrome("hipopotaMO")
        self.assertEqual(result, False) 

    def test6(self):
        result = palindrome("meMOriA")
        self.assertEqual(result, False)

    def test7(self):
        result = palindrome(" radar")
        self.assertEqual(result, True)    

if __name__ == '__main__':
    unittest.main()