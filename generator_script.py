from random import choice


class Name_Generator:
    """
    The structure for our actual name generators that we will use to
    generate random names from a list of given names.
    """

    def __init__(self, f_name_file, l_name_file):
        self.f_names = get_names(f_name_file)
        self.l_names = get_names(l_name_file)

    def generate_name(self):
        first_name = choice(self.f_names)
        last_name = choice(self.l_names)
        return first_name + " " + last_name


def get_names(filename_string):
    """
    Gets the string of line/comma seperated names at the filename_string and returns
    them in a clean, stripped list to be worked with.
    """
    with open(filename_string) as file_contents:
        name_list = []
        name_strings = file_contents.readlines()
        for name in name_strings:
            name = name.strip("\n")
            name = name.strip(",")
            name_list.append(name)
    return name_list


# Placeholder for testing purposes.
# Eventually to be replaced by name generator class.
