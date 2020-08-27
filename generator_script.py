from random import choice


class Name_Generator:
    """
    The structure for our actual name generators that we will use to
    generate random names from a list of given names.
    """

    def __init__(self, f_name_file, l_name_file):
        self.f_name_file = f_name_file
        self.l_name_file = l_name_file
        self.f_names = get_names(f_name_file)
        self.l_names = get_names(l_name_file)

    def generate_name(self):
        """Returns a tuple of a random name from the first and last name lists."""
        first_name = choice(self.f_names)
        last_name = choice(self.l_names)
        return first_name, last_name

    def remove_name(self, name_tuple):
        """Takes a name tuple and removes them from the files on this Generator."""
        f_name, l_name = name_tuple
        with open(self.f_name_file, "r") as f_name_file:
            f_name_text = f_name_file.read()
        with open(self.f_name_file, "w") as f_name_file:
            f_name_text_replaced = f_name_text.replace(f_name + ",", "")
            f_name_text_cleaned = f_name_text_replaced.replace("\n\n", "\n")
            f_name_file.write(f_name_text_cleaned)
        with open(self.l_name_file, "r") as l_name_file:
            l_name_text = l_name_file.read()
        with open(self.l_name_file, "w") as l_name_file:
            l_name_text_replaced = l_name_text.replace(l_name + ",", "")
            l_name_text_cleaned = l_name_text_replaced.replace("\n\n", "\n")
            l_name_file.write(l_name_text_cleaned)


def get_names(filename_string):
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
