from recursion_functions import fibonacci, get_max_number_from_list, get_range_list
from unittest import TestCase


class FibonacciTest(TestCase):
    def setUp(self):
        self.fibonacci_test_data = [
            [1, 1], [2, 1], [3, 2], [4, 3],
            [5, 5], [6, 8], [7, 13], [8, 21],
            [9, 34], [10, 55], [11, 89], [12, 144]
        ]
        self.max_number_test_data = [
            [[92, 1, 2, 3, 4, 5, 6, 9, 11, 17, 0, 2, 7, 49, -17], 92],
            [[-347, 92, 192, 33, 64], 192],
            [[1, 2, 3, 4, 5, 6, 0, 10, 11, 11, 9, -9999999], 11]
        ]
        self.get_range_list_test_data = [
            [[0, 20], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]],
            [[-9, 5], [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]],
            [[-117, -9],
             [-117, -116, -115, -114, -113, -112, -111, -110, -109, -108, -107, -106, -105, -104, -103, -102,
              -101,
              -100, -99, -98, -97, -96, -95, -94, -93, -92, -91, -90, -89, -88, -87, -86, -85, -84, -83, -82, -81, -80,
              -79, -78, -77, -76, -75, -74, -73, -72, -71, -70, -69, -68, -67, -66, -65, -64, -63, -62, -61, -60, -59,
              -58, -57, -56, -55, -54, -53, -52, -51, -50, -49, -48, -47, -46, -45, -44, -43, -42, -41, -40, -39, -38,
              -37, -36, -35, -34, -33, -32, -31, -30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17,
              -16, -15, -14, -13, -12, -11, -10, -9]]]

    def test_fibonacci_test_data(self):
        for n, expected_number in self.fibonacci_test_data:
            actual_number = fibonacci(n)
            message = "%d-число Фибоначчи должно быть %d, а получили %d " % (n, expected_number, actual_number)
            self.assertEqual(actual_number, expected_number, message)

    def test_max_number_data(self):
        for num_list, expected_max in self.max_number_test_data:
            actual_max = get_max_number_from_list(num_list)
            message = "%d-й тест в функции max_number провален, ожидалось %d, получено %d" % (
                self.max_number_test_data.index(
                    [num_list, expected_max]), expected_max, actual_max)
            self.assertEqual(actual_max, expected_max, message)

    def test_get_range_list_data(self):
        for num_range, expected_range_list in self.get_range_list_test_data:
            actual_range_list = get_range_list(num_range[0], num_range[1], [])
            message = "\n %d-й тест в функции get_range_list провален \n ожидалось %s \n получено %s" % (
                self.get_range_list_test_data.index([num_range, expected_range_list]), str(expected_range_list),
                actual_range_list)
            self.assertEqual(actual_range_list, expected_range_list, message)
