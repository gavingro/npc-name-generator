import unittest
from generator_script import Name_Generator, get_names

# Global variables for testing
base_name_gen = Name_Generator("f_names.txt", "l_names.txt")

# for n in range(40):
#     print("My name is " + base_name_gen.generate_name())


class TestNameGenerator(unittest.TestCase):
    def test_get_names_from_file_list_cleaning(self):
        self.assertEqual(type(get_names("f_names.txt")), list)
        self.assertNotIn(",", get_names("f_names.txt"))
        self.assertNotIn("\n", get_names("l_names.txt"))

    def test_generator_class_features(self):
        self.assertEqual(type(base_name_gen.f_names), list)
        self.assertEqual(type(base_name_gen.f_names[0]), str)

    def test_generator_class_generate(self):
        self.assertEqual(type(base_name_gen.generate_name()), str)


if __name__ == "__main__":
    unittest.main()
