#!/usr/bin/env python3

import unittest
from unittest.mock import patch

import numpy as np

from src.extract_numbers import extract_numbers


class TestExtractNumbers(unittest.TestCase):

    def test_worked_example(self):
        s = "abd 123 1.2 test 13.2 -1"
        result = extract_numbers(s)
        self.assertEqual(
            result, [123, 1.2, 13.2, -1],
            msg="Incorrect result for string %r! Non-numeric tokens like "
                "'abd' and 'test' must be skipped." % s)

    def test_calls_float_for_each_number_token(self):
        with patch('builtins.float', wraps=float) as fl:
            extract_numbers("abd 123 1.2 test 13.2 -1")
            self.assertEqual(
                fl.call_count, 4,
                msg="Expected 4 calls of 'float', one per numeric token in "
                    "'abd 123 1.2 test 13.2 -1'. Use float() to convert each "
                    "number, rather than a custom parser.")

    def test_random_values(self):
        values = list(np.random.randint(-100, 100, 50))
        s = " ".join(map(str, values))
        result = extract_numbers(s)
        self.assertEqual(
            values, result,
            msg="Incorrect result for string %r!" % s)

    def test_empty_string_gives_an_empty_list(self):
        result = extract_numbers("")
        self.assertEqual(
            result, [],
            msg="extract_numbers('') should return an empty list: there are "
                "no tokens to extract a number from.")

    def test_no_numbers_gives_an_empty_list(self):
        result = extract_numbers("just some words here")
        self.assertEqual(
            result, [],
            msg="extract_numbers('just some words here') should return an "
                "empty list: none of the tokens are numbers.")


if __name__ == '__main__':
    unittest.main()
