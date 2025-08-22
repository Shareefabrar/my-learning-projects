import unittest
# import sys
# sys.path.append("D:\Python\self\my-learning-projects\Week1\calculatorProject")


from src.dataProcessing import Calculator, FileHandler


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_sub(self):
        self.assertEqual(self.calc.sub(5, 2), 3)

    def test_mul(self):
        self.assertEqual(self.calc.mul(5, 2), 10)

    def test_div(self):
        self.assertEqual(self.calc.div(6, 2), 3)

    def test_pow(self):
        self.assertEqual(self.calc.pwr(5, 2), 25)

    def fail_div(self):
        with self.assertRaises(ValueError):
            self.calc.div(2, 0)


class TestFileHandler(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_results.txt"
        self.file_handler = FileHandler(self.test_file)

    def test_save_read(self):
        self.file_handler.savedata("2 + 3 = 5")
        results = self.file_handler.readData()
        self.assertIn("2 + 3 = 5\n", results)

