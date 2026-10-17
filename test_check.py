import unittest
from check import check_reading


class TestCheckReading(unittest.TestCase):
    def test_nominal_passes(self):
        self.assertEqual(check_reading("5.0"), "PASS")

    def test_low_voltage_fails(self):
        self.assertEqual(check_reading("4.4"), "FAIL")

    def test_high_voltage_fails(self):
        self.assertEqual(check_reading("5.4"), "FAIL")

    def test_lower_limit_passes(self):
        self.assertEqual(check_reading("4.75"), "PASS")

    def test_upper_limit_passes(self):
        self.assertEqual(check_reading("5.25"), "PASS")

    def test_empty_is_missing(self):
        self.assertEqual(check_reading(""), "MISSING")

    def test_none_is_missing(self):
        self.assertEqual(check_reading(None), "MISSING")

    def test_spaces_only_is_missing(self):
        self.assertEqual(check_reading("   "), "MISSING")

    def test_text_is_invalid(self):
        self.assertEqual(check_reading("abc"), "INVALID")


if __name__ == "__main__":
    unittest.main()