import unittest
from dice import Dice

class ProgrammingTest(unittest.TestCase):
    def test_case1(self):
        # case 1, normal stuff..
        dice1 = Dice([1/6 for _ in range(6)],10)
        self.assertIsInstance(dice1,Dice)
        
    def test_case2(self):
        # case 2, try checking if probability is correct.
        corr = [0.1,0.1,0.1,0.1,0.3,0.3]
        dice1 = Dice(corr)
        check = dice1.valid_prob()
        self.assertEqual(check,True)
    
    def test_case3(self):
        # case 3, try checking if probability NOT correct.
        corr = [0.1,0.1,0.1,0.1,0.3,0.7]
        dice1 = Dice(corr)
        check = dice1.valid_prob()
        self.assertEqual(check,False)

    def test_case4(self):
        # case 4, try checking if weights have the same length as a D6
        corr = [0.1,0.1,0.1,0.1,0.3,0.3]
        dice1 = Dice(corr)
        check = dice1.valid_length()
        self.assertEqual(check,True)
    
    def test_case4(self):
        # case 4, try checking if weights does NOT have the same length as a D6
        corr = [0.1,0.1,0.1,0.1,0.3,0.2,0.1]
        dice1 = Dice(corr)
        check = dice1.valid_length()
        self.assertEqual(check,False)
    
    def test_case5(self):
        # case 5, try rolling a D20 with a probability of a D6
        corr = [0.1,0.1,0.1,0.1,0.3,0.3]
        dice1 = Dice(corr,10,[x for x in range(1,21)])
        res = dice1.roll_dice()
        self.assertEqual(res,False)
    
    def test_case6(self):
        # case 6, try rolling a D4 with a probability of a D4
        corr = [0.3,0.2,0.3,0.2]
        dice1 = Dice(corr,10,[x for x in range(1,5)])
        res = dice1.roll_dice()
        self.assertEqual(res,True)
    
    def test_case7(self):
        # case 7, try rolling a D6 negative times...
        dice1 = Dice(amount=-1)
        res = dice1.roll_dice()
        self.assertEqual(res,False)
    
    def test_case8(self):
        # case 8, try rolling a D6 that gets 6 all the time.
        corr = [0,0,0,0,0,1]
        dice1 = Dice(corr,10)
        res = dice1.roll_dice()
        self.assertEqual(sum(dice1.results),60)


if __name__ == '__main__':
    unittest.main()