import unittest

class Cube:
    def __init__(self, cube_string) -> None:
        self.digit = 0
        for character in cube_string:
            if character.isdigit():
                self.digit = self.digit * 10
                self.digit += int(character)

class Handful:
    def __init__(self, handful_string: str) -> None:
        cube_string_array = handful_string.split(",")
        for cube_string in cube_string_array:
            if (cube_string.find("red") != -1):
                self.red = Cube(cube_string)
            elif (cube_string.find("blue") != -1):
                self.blue = Cube(cube_string)
            elif (cube_string.find("green") != -1):
                self.green = Cube(cube_string)


# Test Classes
class TestCube(unittest.TestCase):
    def test_singe_digit_alone(self):
        cube = Cube(" 1 red")
        self.assertEqual(cube.digit, 1, "Singe Digit Cube")

    def test_double_digit_alone(self):
        cube = Cube(" 15 blue")
        self.assertEqual(cube.digit, 15, "Double Digit Cube")

unittest.main()