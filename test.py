"""
Tests for the package.
"""

import unittest

from mock import Mock
import zippy


class TestZippyAPI(unittest.TestCase):

    def setUp(self):
        zippy.core.requests = Mock()
        zippy.core.loads = Mock()

    def test_do_method_calls_requests(self):
        req = zippy.do(12345)
        self.assertTrue(isinstance(req, Mock))
        self.assertTrue(zippy.core.requests.get.called)

    def test_da_method_calls_requests(self):
        req = zippy.do('12345')
        self.assertTrue(isinstance(req, Mock))
        self.assertTrue(zippy.core.requests.get.called)


if __name__ == '__main__':
    unittest.main()
