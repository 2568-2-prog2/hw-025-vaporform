import unittest
from basic_client import call_api

url = "http://127.0.0.1:8081/roll_dice"
'''
data = {
    "probabilities": [0.1, 0.2, 0.3, 0.1, 0.2, 0.1],  # Must sum to 1, requested by the user
    "number_of_random": 10 # Number of random values requested by the user
}

print("Calling the API with the following payload:")
print(data)

# Call the API and get the result
result = call_api(url, data)
'''

class ApiTest(unittest.TestCase):
    def test_try_call(self):
        # checking if we can call at all...
        garbage = {
            "Hello":"World"
        }
        result = call_api(url,garbage)
        self.assertIsInstance(result,dict)
    
    def test_try_call_wrong(self):
        # checking if the call returns error or not.
        data = {
            "probabilities": [0, 0, 0, 0, 0, 1],  # Must sum to 1, requested by the user
            "blah blah": 10 # Number of random values requested by the user
        }
        result = call_api(url,data)
        self.assertEqual(result['status'],'error')
    
    def test_try_call_correct(self):
        # calling it correctly...
        data = {
            "probabilities": [0, 0, 0, 0, 0, 1],  # Must sum to 1, requested by the user
            "number_of_random": 10 # Number of random values requested by the user
        }
        result = call_api(url,data)
        self.assertEqual(sum(result['dice']),60)

if __name__ == '__main__':
    unittest.main()
