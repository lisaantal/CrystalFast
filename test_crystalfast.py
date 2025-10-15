# test_crystalfast.py
"""
Tests for CrystalFast module.
"""

import unittest
from crystalfast import CrystalFast

class TestCrystalFast(unittest.TestCase):
    """Test cases for CrystalFast class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CrystalFast()
        self.assertIsInstance(instance, CrystalFast)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CrystalFast()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
