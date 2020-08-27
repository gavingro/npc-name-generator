from random import choice


class Name_Generator:
    """
    The class for our actual name generators that we can use to
    generate random names from a list of given names.
    """

    def __init__(self, f_names_file, l_names_file):
        self.f_names_file = f_names_file
        self.l_names_file = l_names_file
        self.f_names = make_list_from_file_text(f_names_file)
        self.l_names = make_list_from_file_text(l_names_file)

    def generate_name(self):
        """Returns a tuple of a random name from the first and last name lists."""
        first_name = choice(self.f_names)
        last_name = choice(self.l_names)
        return first_name, last_name

    def remove_name(self, name_tuple):
        """Takes a name tuple and removes them from the files on this Generator."""
        f_name, l_name = name_tuple
        with open(self.f_names_file, "r") as f_names_file:
            f_names_text = f_names_file.read()
        with open(self.f_names_file, "w") as f_names_file:
            f_names_text_cleaned = f_names_text.replace(f_name + ",\n", "")
            f_names_file.write(f_names_text_cleaned)
        with open(self.l_names_file, "r") as l_names_file:
            l_names_text = l_names_file.read()
        with open(self.l_names_file, "w") as l_names_file:
            l_names_text_cleaned = l_names_text.replace(l_name + ",\n", "")
            l_names_file.write(l_names_text_cleaned)
        self.f_names = make_list_from_file_text(self.f_names_file)
        self.l_names = make_list_from_file_text(self.l_names_file)

    def use_name(self, name_tuple):
        """Takes a name tuple and adds it to the "used names" list."""
        f_name, l_name = name_tuple
        name = f_name + " " + l_name
        with open("used_names.txt", "a") as used_names_file:
            used_names_file.write(name + ",\n")

    def grab_name(self):
        """
        Generates a random name, removes it from the name lists, adds it to the
        used list, then returns the name as a string.
        """
        generated_name = self.generate_name()
        self.remove_name(generated_name)
        self.use_name(generated_name)
        f_name, l_name = generated_name
        return f_name + " " + l_name


def make_list_from_file_text(filename_string):
    """
    Gets the string of line/comma seperated names at the filename_string
    and returns them in a clean, stripped list.
    """
    with open(filename_string) as file_contents:
        name_list = []
        name_strings = file_contents.readlines()
        for name in name_strings:
            name = name.strip("\n")
            name = name.strip(",")
            name_list.append(name)
    return name_list
