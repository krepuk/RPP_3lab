import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from discriminant import calculate_discriminant, solve_quadratic


class TestQuadraticEquation(unittest.TestCase):
    """Test cases for quadratic equation functions."""

    def test_discriminant_positive(self):
        """Test discriminant calculation with positive result."""
        self.assertEqual(calculate_discriminant(1, -3, 2), 1)

    def test_discriminant_zero(self):
        """Test discriminant calculation with zero result."""
        self.assertEqual(calculate_discriminant(1, -2, 1), 0)

    def test_discriminant_negative(self):
        """Test discriminant calculation with negative result."""
        self.assertEqual(calculate_discriminant(1, 1, 1), -3)

    def test_solve_quadratic_two_roots(self):
        """Test solving quadratic equation with two real roots."""
        roots = solve_quadratic(1, -3, 2)
        self.assertEqual(len(roots), 2)
        self.assertAlmostEqual(roots[0], 2.0)
        self.assertAlmostEqual(roots[1], 1.0)

    def test_solve_quadratic_one_root(self):
        """Test solving quadratic equation with one real root."""
        roots = solve_quadratic(1, -2, 1)
        self.assertEqual(len(roots), 1)
        self.assertAlmostEqual(roots[0], 1.0)

    def test_solve_quadratic_complex_roots(self):
        """Test solving quadratic equation with complex roots."""
        roots = solve_quadratic(1, 1, 1)
        self.assertEqual(len(roots), 2)
        self.assertIsInstance(roots[0], complex)
        self.assertIsInstance(roots[1], complex)

    def test_invalid_equation(self):
        """Test solving non-quadratic equation."""
        with self.assertRaises(ValueError):
            solve_quadratic(0, 1, 1)


if __name__ == '__main__':
    unittest.main()


