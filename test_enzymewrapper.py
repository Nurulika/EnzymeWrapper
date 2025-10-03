# test_enzymewrapper.py
"""
Tests for EnzymeWrapper module.
"""

import unittest
from enzymewrapper import EnzymeWrapper

class TestEnzymeWrapper(unittest.TestCase):
    """Test cases for EnzymeWrapper class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EnzymeWrapper()
        self.assertIsInstance(instance, EnzymeWrapper)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EnzymeWrapper()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
