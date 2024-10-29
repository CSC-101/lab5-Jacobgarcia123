import data
import unittest


class TestCases(unittest.TestCase):
    #### Time tests
    def test_Time_1(self):
        time = data.Time(7, 20, 1)
        self.assertEqual(7, time.hour)
        self.assertEqual(20, time.minute)
        self.assertEqual(1, time.second)


    def test_Time_2(self):
        time = data.Time(4, 19, 45)
        self.assertEqual(4, time.hour)
        self.assertEqual(19, time.minute)
        self.assertEqual(45, time.second)


    #### Add tests for Time.__eq__
    def test_Eq_1(self):
        time = data.Time(7,54,32)
        self.assertEqual(7, time.hour)
        self.assertEqual(54, time.minute)
        self.assertEqual(32, time.second)
    def test_Eq_2(self):
        time = data.Time(7,13,5)
        self.assertNotEqual('seven',time.hour)
        self.assertNotEqual('thirteen',time.hour)
        self.assertNotEqual('five',time.hour)



    #### Add tests for Time.__repr__
    def test_repr_1(self):
        time = data.Time(9,23,45)
        expected_time = "Hour: 9, Minute: 23, Second: 45"
        self.assertTrue(time,expected_time)

    def test_repr_1(self):
        time = data.Time(11, 56, 3)
        expected_time = "Hour: 11, Minute: 56, Second: 3"
        self.assertTrue(time, expected_time)




    #### Point tests
    def test_Point_1(self):
        point = data.Point(7, 20)
        self.assertAlmostEqual(7, point.x)
        self.assertAlmostEqual(20, point.y)


    def test_Point_2(self):
        point = data.Point(4, 19)
        self.assertAlmostEqual(4, point.x)
        self.assertAlmostEqual(19, point.y)


    def test_Point_eq_1(self):
        point1 = data.Point(1, 20)
        point2 = data.Point(1, 20)
        self.assertEqual(point1, point2)


    def test_Point_eq_2(self):
        point1 = data.Point(1, 20)
        self.assertEqual(point1, point1)


    def test_Point_eq_3(self):
        point1 = data.Point(1, 20)
        point2 = data.Point(2, 20)
        self.assertNotEqual(point1, point2)


    def test_Point_eq_4(self):
        point = data.Point(1, 20)
        other = 1.20
        self.assertNotEqual(point, other)


    def test_Point_repr(self):
        point = data.Point(5, 75)
        self.assertEqual('Point(5, 75)', repr(point))


if __name__ == '__main__':
    unittest.main()
