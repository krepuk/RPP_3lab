import unittest
import sys
import os

# Add current directory to path to import module
sys.path.insert(0, os.path.dirname(__file__))

# Измените эту строку:
from discrimination import calculate_discriminant, solve_quadratic

class TestDiscriminant(unittest.TestCase):
    """Test cases for discriminant calculation"""

    # Positive tests - discriminant >= 0
    
    def test_positive_discriminant(self):
        """Test case with positive discriminant (D > 0)"""
        result = calculate_discriminant(1, -3, 2)
        self.assertEqual(result, 1)
    
    def test_zero_discriminant(self):
        """Test case with zero discriminant (D = 0)"""
        result = calculate_discriminant(1, -2, 1)
        self.assertEqual(result, 0)
    
    def test_negative_discriminant(self):
        """Test case with negative discriminant (D < 0)"""
        result = calculate_discriminant(1, 1, 1)
        self.assertEqual(result, -3)
    
    # Test solve_quadratic function
    
    def test_solve_two_roots(self):
        """Test solving quadratic equation with two roots"""
        roots = solve_quadratic(1, -3, 2)
        self.assertEqual(len(roots), 2)
        self.assertAlmostEqual(roots[0], 2.0)
        self.assertAlmostEqual(roots[1], 1.0)
    
    def test_solve_one_root(self):
        """Test solving quadratic equation with one root"""
        roots = solve_quadratic(1, -2, 1)
        self.assertEqual(len(roots), 1)
        self.assertAlmostEqual(roots[0], 1.0)
    
    def test_solve_no_roots(self):
        """Test solving quadratic equation with no real roots"""
        roots = solve_quadratic(1, 1, 1)
        self.assertEqual(len(roots), 0)
    
    # Negative tests - edge cases and error conditions
    
    def test_invalid_zero_coefficient_a(self):
        """Test case with a=0 (should raise ValueError)"""
        with self.assertRaises(ValueError):
            calculate_discriminant(0, 1, 1)
    
    def test_large_numbers(self):
        """Test with large numbers to check for overflow"""
        result = calculate_discriminant(1e10, 2e10, 1e10)
        self.assertEqual(result, 0.0)
    
    def test_fractional_coefficients(self):
        """Test with fractional coefficients"""
        result = calculate_discriminant(0.5, 1.5, 1.0)
        self.assertAlmostEqual(result, 0.25)
    
    def test_negative_coefficients(self):
        """Test with all negative coefficients"""
        result = calculate_discriminant(-1, -2, -1)
        self.assertEqual(result, 0)
    
    def test_solve_with_fractional_roots(self):
        """Test solving with fractional roots"""
        roots = solve_quadratic(2, -3, 1)
        self.assertEqual(len(roots), 2)
        self.assertAlmostEqual(roots[0], 1.0)
        self.assertAlmostEqual(roots[1], 0.5)

if __name__ == '__main__':
    unittest.main()