import BalancedAB
import unittest


# inherit all methods from unittest methods
class TestBalancedAB(unittest.TestCase):

    def testBalancedAB(self):
        self.assertEqual(BalancedAB.BalancedAB('AAZZBB'), True)
        self.assertEqual(BalancedAB.BalancedAB('AAAXXXXYB'), True)
        self.assertEqual(BalancedAB.BalancedAB('BBYYYXXXAXX'), False)
        self.assertEqual(BalancedAB.BalancedAB('XXXXXYYYYZZZZB'), True)
        self.assertEqual(BalancedAB.BalancedAB(' XXXXXYYYYZZZZ'), True)
        self.assertEqual(BalancedAB.BalancedAB('XXXX XYYYY ZZZZB'), True)
        self.assertEqual(BalancedAB.BalancedAB('YYYBABYYYXXXAXX'), False)
        self.assertEqual(BalancedAB.BalancedAB('ABABABA'), False)
        self.assertEqual(BalancedAB.BalancedAB('A'), False)