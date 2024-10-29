import data
import lab5
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    #    Part 1 tests should be in data_tests.py.

    # Part 2
    #    Part 2 tests should be in data_tests.py.


    # Part 3
    def test_time_add_1(self):
        input = data.Time(10,56,48)
        input2 = data.Time(11, 32, 17)
        result = lab5.time_add(input,input2)
        expected = (22,29,5)
        self.assertEqual(expected,result)

    def test_time_add_2(self):
        input = data.Time(3,37,6)
        input2 = data.Time(6, 22, 1)
        result = lab5.time_add(input,input2)
        expected = (9,59,7)
        self.assertEqual(expected,result)

    # Part 4
    def test_is_descending_1(self):
        input = [56.6,56,34,21.89,5]
        result = lab5.is_descending(input)
        expected = True
        self.assertEqual(expected,result)
    def test_is_descending_2(self):
        input = [73,43,89,0,8.8]
        result = lab5.is_descending(input)
        expected = False
        self.assertEqual(expected,result)


    # Part 5
    def test_largest_between_1(self):
        input = ([0,5,3,2,7,8,4])
        input1 = 1
        input2 = 5
        result = lab5.largest_between(input,input1,input2)
        expected = 5
        self.assertEqual(expected,result)

    def test_largest_between_2(self):
        input = ([45,7,8,32,99])
        input1 = 0
        input2 = 3
        result = lab5.largest_between(input,input1,input2)
        expected = 0
        self.assertEqual(expected,result)


    # Part 6
    def test_furthest_from_origin_1(self):
        input1 = data.Point(6,7)
        input2 = data.Point(9,23)
        input3 = data.Point(43,9)
        input = [input1,input2,input3]
        result = lab5.furthest_from_origin(input)
        expected = 2
        self.assertEqual(expected,result)

    def test_furthest_from_origin_2(self):
        input1 = data.Point(0,0)
        input2 = data.Point(4,5)
        input3 = data.Point(0,0)
        input = [input1,input2,input3]
        result = lab5.furthest_from_origin(input)
        expected = 1
        self.assertEqual(expected,result)





if __name__ == '__main__':
    unittest.main()
