import unittest
from p1 import TwoStack
from p2 import LargeNumber

class OutcomesTest(unittest.TestCase):

    def test_python1(self,p1=TwoStack()):
        self.assertTrue(p1.l_push(1))
        self.assertTrue(p1.r_push(2))
        self.assertTrue(p1.l_push(3))
        self.assertTrue(p1.r_push(4))
        self.assertTrue(p1.l_pop())
        self.assertTrue(p1.r_pop())
        self.assertTrue(p1.l_pop())
        self.assertTrue(p1.r_pop())
        self.assertFalse(p1.r_pop())
        self.assertFalse(p1.l_pop())

    def test_python2(self,p2=LargeNumber()):
        self.assertTrue(p2.addTwoNumbers("1234235436547567","3243547658768956745"))
        self.assertTrue(p2.addTwoNumbers("1234436547567213", "324354956876753745"))
        self.assertTrue(p2.addTwoNumbers("47567", "3243540090907554"))
        self.assertTrue(p2.addTwoNumbers("999999999999", "1"))

if __name__ == '__main__':
    unittest.main(verbosity=2)