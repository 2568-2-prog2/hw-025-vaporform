import random

class Dice:
    def __init__(self,weight:list=[1/6 for x in range(6)],amount:int=0,faces=[x for x in range(1,7)]):
        self.weight = weight
        self.amount = amount
        self.faces = faces
        self.results = []

    def roll_dice(self):
        # reroll or smth...
        if not(self.valid_prob() and self.valid_length() and self.amount >= 0):
            return False
        self.results = random.choices(self.faces, self.weight, k=self.amount)
        return True

    def valid_length(self):
        return len(self.weight) == len(self.faces)
    
    def valid_prob(self):
        if sum(self.weight) != 1:
            print("Probability does NOT sum to 1! Fix the weights!!")
            return False
        return True

if __name__ == '__main__':
    data = {
        "probabilities": [0.1, 0.2, 0.3, 0.1, 0.2, 0.1],  # Must sum to 1, requested by the user
        "number_of_random": 10 # Number of random values requested by the user
    }
    print(Dice(data['probabilities'],data['number_of_random']))