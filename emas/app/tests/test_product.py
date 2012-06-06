import unittest


class TestProduct(unittest.TestCase):
    """Unit test for the Product type
    """
    
    def test_one(self):
        pass


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
