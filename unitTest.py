import unittest
from game import cardGame


class Test(unittest.TestCase):
    def __init__(self):
        self.g = cardGame()

    def testRule1(self):
        goodhand = ["4", "4", "4"]
        badhand = ["K", "1", "4"]
        self.assertTrue(self.g.Rule1(goodhand))
        self.assertFalse(self.g.Rule1(badhand))

    def testRule2(self):
        goodhand = ["8", "9", "10"]
        badhand = ["J", "9", "10"]
        self.assertTrue(self.g.Rule2(goodhand))
        self.assertFalse(self.g.Rule2(badhand))

    def testRule3(self):
        goodhand = ["3", "6", "3"]
        badhand = ["Q", "3", "1"]
        self.assertTrue(self.g.Rule3(goodhand))
        self.assertFalse(self.g.Rule3(badhand))

    def testRule4_without_tie(self):
        player = {
            1:  ['2', '4', 'A'],
            2:  ['3', '9', '8'],
            3:  ['J', 'K', 'A'],
            4:  ['J', 'A', '5'],
        }
        self.assertTrue(self.g.Rule4(player) == "3")

    def testgetHighest(self):
        player = {
            1:  ['2', '4', 'K'],
            2:  ['3', '9', '8'],
            3:  ['J', '10', 'Q'],
            4:  ['J', 'A', '5'],
        }
        self.assertTrue(self.g.getHighest(player) == [12, 8, 11, 10])

    def testDecision(self):
        t1 = {
            1:  ['K', 'Q', 'J'],
            2:  ['2', '3', 'A'],
            3:  ['A', '6', 'Q'],
            4:  ['6', '2', '6'],
        }
        t2 = {
            1:  ['5', '5', '5'],
            2:  ['Q', 'K', 'J'],
            3:  ['A', '6', 'Q'],
            4:  ['6', '2', '6'],
        }
        t3 = {
            1:  ['K', 'A', '7'],
            2:  ['Q', '4', 'J'],
            3:  ['A', '6', 'Q'],
            4:  ['6', 'A', 'A'],
        }
        self.assertTrue(self.g.decision(t1) == "2")
        self.assertTrue(self.g.decision(t2) == "1")
        self.assertTrue(self.g.decision(t3) == "4")

    def testapplyRules(self):
        h1 = ["5", "7", "3"]
        h2 = ["3", "A", "A"]
        h3 = ["8", "6", "7"]
        h4 = ["6", "6", "6"]
        self.assertTrue(self.g.applyRules(h1) == 0)
        self.assertTrue(self.g.applyRules(h2) == 1)
        self.assertTrue(self.g.applyRules(h3) == 2)
        self.assertTrue(self.g.applyRules(h4) == 3)


mytest = Test()
mytest.testRule1()
mytest.testRule2()
mytest.testRule3()
mytest.testgetHighest()
mytest.testDecision()
mytest.testapplyRules()
mytest.testRule4_without_tie()
