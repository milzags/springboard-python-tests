from unittest import TestCase
import algorithms

class AlgorithmsTestCase(TestCase):
    def test_reverse(self):
        self.assertEqual(algorithms.reverse_str('hello'), 'olleh')
        self.assertEqual(algorithms.reverse_str('Apple'), 'elppA')
    
    def test_palindrome(self):
        self.assertEqual(algorithms.is_Palindrome('racecar'), True)
        self.assertTrue(algorithms.is_Palindrome('racecar'))
        self.assertTrue(algorithms.is_Palindrome('KAYAk'))
        #should ignore casing, make changes in algorithms.py file
        self.assertFalse(algorithms.is_Palindrome('taco'))
    
    def test_factorial(self):
        self.assertEqual(algorithms.factorial(5), 120)
        self.assertRaises(ValueError, algorithms.factorial, -5)
        self.assertRaises(ValueError, algorithms.factorial, 4.3)