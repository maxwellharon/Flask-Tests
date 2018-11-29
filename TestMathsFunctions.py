#TestMathFunctions.py
#By YourNameHere

# Import Statemants
import unittest
import MathFunctions

class KnowValues(unittest.TestCase):
    # Test areaCircle() pi r^2
    def test_areaCircle_for_10radius(self):
        # Capture the results of the function
        result = MathFunctions.areaCircle(10)
        # Check for expected output
        answer = 314.1592653589793
        self.assertEqual(answer, result)

        # Capture the results of the function
    def test_areaCircle_for_2radius(self):
        # Capture the results of the function
        result = MathFunctions.arealive(2)
        # Check for expected output
        expected = 12.566370614359172
        self.assertEqual(expected, result)
        # Capture the results of the function

        # Capture the results of the function
    def test_areaCircle_for_3radius(self):
        # Capture the results of the function
        result = MathFunctions.areanive(3)
        # Check for expected output
        expected = 28.274333882308138
        self.assertEqual(expected, result)
        # Capture the results of the function


    def test_areaCircle_for_9radius(self):
        # Capture the results of the function
        result = MathFunctions.areasive(9)
        # Check for expected output
        expected = 254.46900494077323
        self.assertEqual(expected, result)
        # Capture the results of the function

    def test_areaCircle_for_4radius(self):
        # Capture the results of the function
        result = MathFunctions.areavive(4)
        # Check for expected output
        expected = 78.53981633974483
        self.assertEqual(expected, result)
        # Capture the results of the function

# Run the Test
if __name__ == '__main__':
    unittest.main()

#TestMathFunctions.py
#By YourNameHere

# Import Statemants
