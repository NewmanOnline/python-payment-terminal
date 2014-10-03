import unittest

from nm_payment.tests.bbs import (
    TestBBSFields, TestBBSMessages, TestBBSTerminal, TestBBSPaymentSession,
)
from nm_payment.tests.test_stream import TestStream


loader = unittest.TestLoader()
suite = unittest.TestSuite((
    loader.loadTestsFromTestCase(TestBBSFields),
    loader.loadTestsFromTestCase(TestBBSMessages),
    loader.loadTestsFromTestCase(TestBBSTerminal),
    loader.loadTestsFromTestCase(TestBBSPaymentSession),
    loader.loadTestsFromTestCase(TestStream),
))
