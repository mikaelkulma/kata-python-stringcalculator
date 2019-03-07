import unittest

from strcalc import calculator


class CalculatorTest(unittest.TestCase):

    def test_empty_string_returns_0(self):
        self.assertEqual(calculator.add(""), 0)

    def test_single_number_returns_the_number(self):
        self.assertEqual(calculator.add("1"), 1)

    def test_two_numbers_return_their_sum(self):
        self.assertEqual(calculator.add("1,2"), 3)

    def test_newlines_can_be_used_as_separators(self):
        self.assertEqual(calculator.add("1\n2"), 3)

    def test_extra_separator_can_be_configured_on_the_first_line(self):
        self.assertEqual(calculator.add("//[@]\n1\n2@3"), 6)

    def test_exception_negatives_not_allowed_is_thrown_for_negative_numbers(self):
        with self.assertRaises(ValueError) as cm:
            calculator.add("-1")
        self.assertEqual('negatives not allowed', str(cm.exception))

    def test_numbers_larger_than_1000_are_ignored(self):
        self.assertEqual(calculator.add("1001,1"), 1)

    def test_separators_can_be_of_any_length(self):
        self.assertEqual(calculator.add("//[@@@@@]\n1\n2@@@@@3"), 6)

    def test_multiple_separators_are_allowed(self):
        self.assertEqual(calculator.add("//[@@@@@][;;;;]\n1\n2@@@@@3"), 6)

if __name__ == '__main__':
    unittest.main()
