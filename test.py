import unittest
from generator_script import Name_Generator, make_list_from_file_text


# Personal Exploratory Tests

# base_name_gen = Name_Generator("f_names.txt", "l_names.txt")
# print(base_name_gen.grab_name())


# Unit testing
class TestFileCleaning(unittest.TestCase):
    def test_make_list_from_file_list_cleaning(self):
        self.assertEqual(type(make_list_from_file_text("f_names.txt")), list)
        self.assertNotIn(",", make_list_from_file_text("f_names.txt"))
        self.assertNotIn("\n", make_list_from_file_text("l_names.txt"))


class TestNameGenerator(unittest.TestCase):
    def setUp(self):
        self.base_name_gen = Name_Generator("f_names.txt", "l_names.txt")

    def test_generator_class_init(self):
        self.assertEqual(type(self.base_name_gen.f_names), list)
        self.assertEqual(type(self.base_name_gen.f_names[0]), str)

    def test_generator_class_generate_func(self):
        self.assertEqual(type(self.base_name_gen.generate_name()), tuple)
        self.assertNotEqual(
            self.base_name_gen.generate_name(),
            self.base_name_gen.generate_name(),
            "Theres a TINY chance it could generate the exact same name twice.",
        )

    def test_generator_class_remove_name_func(self):
        with open(self.base_name_gen.f_names_file, "a") as f_names:
            f_names.write("Test1,\n")
        with open(self.base_name_gen.l_names_file, "a") as l_names:
            l_names.write("Testson1,\n")

        test_name = ("Test1", "Testson1")
        self.base_name_gen.remove_name(test_name)
        with open(self.base_name_gen.f_names_file, "r") as f_names:
            f_names_text = f_names.read()
            self.assertNotIn("Test1", f_names_text)
            self.assertNotIn("\n\n", f_names_text)
        with open(self.base_name_gen.l_names_file, "r") as l_names:
            l_names_text = l_names.read()
            self.assertNotIn("Testson1", l_names_text)
            self.assertNotIn("\n\n", l_names_text)

    def test_generator_class_use_name_func(self):
        # make sure theres no test name first
        test_name = "Test2 Testson2"
        with open("used_names.txt", "r") as u_names_file:
            u_names_text = u_names_file.read()
        with open("used_names.txt", "w") as u_names_file:
            u_names_text_replaced = u_names_text.replace(test_name + ",\n", "")
            u_names_file.write(u_names_text_replaced)

        test_name_tuple = ("Test2", "Testson2")
        self.base_name_gen.use_name(test_name_tuple)
        with open("used_names.txt", "r") as u_names_file:
            u_names_text = u_names_file.read()
            self.assertIn(test_name, u_names_text)

        # just go ahead and clean it up after too
        with open("used_names.txt", "r") as u_names_file:
            u_names_text = u_names_file.read()
        with open("used_names.txt", "w") as u_names_file:
            u_names_text_replaced = u_names_text.replace(test_name + ",\n", "")
            u_names_file.write(u_names_text_replaced)

    def test_generator_class_get_names_func(self):
        # grab name items
        grabbed_name = self.base_name_gen.grab_name()
        grabbed_name_parts = grabbed_name.split()
        grabbed_f_name = grabbed_name_parts[0]
        grabbed_l_name = grabbed_name_parts[1]

        # grabbed name tests
        self.assertEqual(type(grabbed_name), str)
        self.assertNotIn(grabbed_f_name, self.base_name_gen.f_names)
        self.assertNotIn(grabbed_l_name, self.base_name_gen.l_names)

        # removing grabbed name from used list
        with open("used_names.txt", "r") as u_names_file:
            u_names_text = u_names_file.read()
        with open("used_names.txt", "w") as u_names_file:
            u_names_text_replaced = u_names_text.replace(grabbed_name + ",\n", "")
            u_names_file.write(u_names_text_replaced)

        # putting the name back into the lists
        # BUGS WHEN CLEANING MULTI WORD NAMES
        with open(self.base_name_gen.f_names_file, "a") as f_names:
            f_names.write(grabbed_f_name + ",\n")
        with open(self.base_name_gen.l_names_file, "a") as l_names:
            l_names.write(grabbed_l_name + ",\n")


if __name__ == "__main__":
    unittest.main()
