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

    def test_generator_class_generate_func(self):
        self.assertEqual(type(base_name_gen.generate_name()), tuple)

    def test_generator_class_remove_name_func(self):

        with open("f_names.txt", "a") as f_names:
            f_names.write("Test,\n")
        with open("l_names.txt", "a") as l_names:
            l_names.write("Testson,\n")

        test_name = ("Test", "Testson")
        base_name_gen.remove_name(test_name)
        with open("f_names.txt", "r") as f_names:
            f_names_text = f_names.read()
            self.assertNotIn("Test", f_names_text)
            self.assertNotIn("\n\n", f_names_text)
        with open("l_names.txt", "r") as l_names:
            l_names_text = l_names.read()
            self.assertNotIn("Testson", l_names_text)
            self.assertNotIn("\n\n", l_names_text)


if __name__ == "__main__":
    unittest.main()
