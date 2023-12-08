import unittest

class Cube:
    def __init__(self, cube_string: str) -> None:
        self.digit = 0
        for character in cube_string:
            if character.isdigit():
                self.digit = self.digit * 10
                self.digit += int(character)


class Handful:
    def __init__(self, handful_string: str) -> None:
        self.red = Cube("0")
        self.blue = Cube("0")
        self.green = Cube("0")

        cube_string_array = handful_string.split(",")
        for cube_string in cube_string_array:
            if (cube_string.find("red") != -1):
                self.red = Cube(cube_string)
            elif (cube_string.find("blue") != -1):
                self.blue = Cube(cube_string)
            elif (cube_string.find("green") != -1):
                self.green = Cube(cube_string)


class Game:
    def __init__(self, game_string: str) -> None:
        game_text = game_string.split(":")[0]
        game_number_cube = Cube(game_text)
        self.game_number = game_number_cube.digit

        self.max_red = 0
        self.max_blue = 0
        self.max_green = 0
        handful_text_array = game_string.split(":")[1].split(";")
        for handful_text in handful_text_array:
            handful = Handful(handful_text)
            if (handful.red.digit > self.max_red):
                self.max_red = handful.red.digit
            if (handful.blue.digit > self.max_blue):
                self.max_blue = handful.blue.digit
            if (handful.green.digit > self.max_green):
                self.max_green = handful.green.digit

        self.power = self.max_red * self.max_blue * self.max_green


class GameFinder:
    def __init__(self, red, green, blue, games_string) -> None:
        self.game_sum = 0
        self.power_sum = 0
        games_array = games_string.split("\n")
        for game_string in games_array:
            current_game = Game(game_string)
            self.power_sum += current_game.power
            if (current_game.max_red <= red and current_game.max_green <= green and current_game.max_blue <= blue):
                self.game_sum += current_game.game_number
        

# Test Classes
class TestCube(unittest.TestCase):
    def test_singe_digit(self):
        cube = Cube(" 1 red")
        self.assertEqual(cube.digit, 1, "Singe Digit Cube")

    def test_double_digit(self):
        cube = Cube(" 15 blue")
        self.assertEqual(cube.digit, 15, "Double Digit Cube")
    
    def test_tripple_digit(self):
        cube = Cube("Game 100")
        self.assertEqual(cube.digit, 100, "Tripple Digit Cube")


class TestHandful(unittest.TestCase):
    def test_one_color(self):
        handful = Handful(" 2 green")
        self.assertEqual(handful.green.digit, 2, "One Color Handful")
        
    def test_two_colors(self):
        handful = Handful(" 3 blue, 4 red")
        self.assertEqual(handful.blue.digit, 3, "Two Color Handful 1")
        self.assertEqual(handful.red.digit, 4, "Two Color Handful 2")

    def test_three_colors(self):
        handful = Handful(" 3 green, 4 blue, 1 red")
        self.assertEqual(handful.blue.digit, 4, "Three Color Handful 1")
        self.assertEqual(handful.red.digit, 1, "Three Color Handful 2")
        self.assertEqual(handful.green.digit, 3, "Three Color Handful 3")


class TestGame(unittest.TestCase):
    def test_one_handful(self):
        game = Game("Game 13: 3 blue")
        self.assertEqual(game.game_number, 13, "One Handful Game Number")
        self.assertEqual(game.max_blue, 3, "One Handful Game Max Blue")
    
    def test_three_handful(self):
        game = Game("Game 67: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue")
        self.assertEqual(game.game_number, 67, "Three Handful Game Number")
        self.assertEqual(game.max_blue, 4, "Three Handful Game Max Blue")
        self.assertEqual(game.max_green, 3, "Three Handful Game Max Green")
        self.assertEqual(game.max_red, 1, "Three Handful Game Max Red")


class TestGameFinder(unittest.TestCase):
    def provided_test_1(self):
        string = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
                    Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
                    Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
                    Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
                    Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
        game_finder = GameFinder(12, 13, 14, string)
        self.assertEqual(game_finder.game_sum, 8, "Provided Example 1")
    
    def provided_test_2(self):
        string = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
                    Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
                    Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
                    Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
                    Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
        game_finder = GameFinder(12, 13, 14, string)
        self.assertEqual(game_finder.game_sum, 8, "Provided Example 2")


puzzle_string = """Game 1: 1 green, 2 blue; 15 blue, 12 red, 2 green; 4 red, 6 blue; 10 blue, 8 red; 3 red, 12 blue; 1 green, 12 red, 8 blue
Game 2: 5 green, 2 red, 18 blue; 18 blue, 6 red, 9 green; 6 blue, 3 green; 6 green, 1 red, 9 blue; 19 blue, 2 green, 6 red
Game 3: 16 red, 10 green; 12 red, 6 blue, 9 green; 10 green, 5 blue; 10 green, 16 red; 5 red, 8 green, 8 blue
Game 4: 9 blue, 20 green; 1 red, 3 blue, 10 green; 7 blue, 18 green; 4 blue, 20 green; 8 blue, 1 green, 1 red; 1 green
Game 5: 3 green, 8 red; 1 blue, 10 red; 6 red, 4 green; 8 red, 1 blue, 3 green; 1 blue, 4 green, 3 red; 1 green, 1 blue, 4 red
Game 6: 7 green, 15 red, 11 blue; 2 red, 12 blue; 11 red, 11 green
Game 7: 14 green, 10 blue, 4 red; 3 red, 11 green, 14 blue; 1 red, 2 green, 11 blue; 9 green, 1 red; 6 red, 6 blue, 9 green
Game 8: 1 red, 6 green, 3 blue; 4 green; 4 red, 3 green, 1 blue; 2 red, 10 green, 3 blue; 2 green, 6 red, 3 blue
Game 9: 2 green, 8 red, 3 blue; 2 green, 4 blue, 2 red; 2 green, 5 blue, 2 red
Game 10: 9 green, 1 blue; 2 blue, 12 green, 3 red; 2 red, 3 blue, 1 green; 3 blue, 8 green; 4 blue, 4 red, 1 green; 5 green, 4 blue
Game 11: 5 red, 2 blue, 2 green; 3 blue, 2 green, 8 red; 6 red, 1 green
Game 12: 8 blue, 7 green; 2 green, 2 red, 7 blue; 4 green, 1 red, 20 blue; 5 green, 13 blue, 2 red
Game 13: 1 blue, 11 green, 13 red; 6 blue, 13 red, 19 green; 5 blue, 6 green, 6 red
Game 14: 12 blue, 1 red, 15 green; 16 green; 1 red, 18 blue, 15 green; 14 blue; 12 blue, 1 red, 8 green; 4 blue, 16 green
Game 15: 6 blue, 3 green; 1 red, 1 blue, 2 green; 3 green, 4 blue, 7 red
Game 16: 17 red, 14 green, 6 blue; 5 blue, 2 red; 1 blue, 11 red, 2 green; 13 green, 12 red
Game 17: 14 green, 4 red; 1 green, 5 blue, 15 red; 5 green, 14 red, 5 blue
Game 18: 8 blue, 2 green, 1 red; 12 blue, 1 green; 1 green, 1 red, 5 blue; 1 green, 1 red, 9 blue
Game 19: 1 red, 2 blue; 2 green, 5 red; 1 blue, 2 green, 11 red; 10 red; 4 green, 11 red
Game 20: 5 red, 11 green, 5 blue; 2 red, 5 blue, 7 green; 12 blue, 5 green, 10 red; 4 blue, 15 red, 10 green; 11 green, 12 blue, 7 red; 15 red, 12 blue, 5 green
Game 21: 5 blue, 6 green, 1 red; 18 blue, 13 green; 7 blue, 3 red; 9 blue, 2 red, 14 green
Game 22: 4 blue, 2 green, 19 red; 11 green, 5 blue, 17 red; 12 red, 4 blue, 13 green; 2 blue, 11 green; 1 blue, 19 red, 10 green; 8 blue, 2 green
Game 23: 12 green, 6 red; 1 blue, 1 red, 11 green; 1 blue, 3 red, 8 green; 4 green, 8 red
Game 24: 8 blue, 1 green, 6 red; 6 blue, 9 red; 8 red, 1 green, 1 blue
Game 25: 2 red, 4 blue, 1 green; 1 blue, 4 red, 2 green; 1 green, 5 blue, 1 red; 3 red, 2 blue
Game 26: 2 green, 10 blue, 5 red; 14 blue, 6 green, 12 red; 7 green, 2 red, 1 blue; 3 blue, 5 green, 3 red; 7 blue, 1 red, 3 green; 5 red, 2 green, 6 blue
Game 27: 8 blue, 2 red; 2 green, 8 blue, 6 red; 4 green, 2 red; 2 blue, 4 green, 7 red
Game 28: 8 green; 1 red, 9 blue, 10 green; 8 green, 9 blue, 2 red
Game 29: 5 red, 3 green, 2 blue; 12 red, 6 blue, 1 green; 6 red, 12 blue; 2 green, 4 blue, 5 red
Game 30: 9 red, 1 blue, 2 green; 13 green, 12 blue, 11 red; 11 red, 5 green, 9 blue; 4 blue, 12 green, 3 red; 10 red, 8 green; 2 red, 3 blue, 12 green
Game 31: 11 green, 5 red; 1 green, 4 red; 6 green, 9 red, 2 blue
Game 32: 6 blue, 3 red; 2 red, 11 blue, 4 green; 1 green, 4 red, 12 blue; 3 blue, 2 red
Game 33: 1 green, 7 red; 15 red, 15 green, 1 blue; 15 green, 3 red; 1 blue, 13 green, 6 red; 1 blue, 13 green, 20 red
Game 34: 3 red, 5 green, 1 blue; 13 green, 5 blue, 2 red; 3 red, 3 blue, 8 green; 3 blue, 1 red, 1 green; 4 blue, 3 red; 9 green, 3 red
Game 35: 6 blue, 8 green; 6 red, 9 blue, 12 green; 4 green, 3 blue; 5 red, 3 blue
Game 36: 17 green, 1 red, 1 blue; 1 red, 7 blue, 13 green; 6 blue, 5 green; 9 blue, 6 red, 5 green
Game 37: 2 green, 16 blue, 1 red; 3 red, 5 blue, 4 green; 3 green, 5 red, 2 blue
Game 38: 10 red, 3 blue, 1 green; 2 blue, 4 red; 7 red, 1 blue; 8 blue, 5 red, 11 green; 12 green, 4 blue, 8 red
Game 39: 3 blue, 3 green, 1 red; 5 green, 9 blue; 1 green, 6 blue; 5 blue, 7 green, 1 red; 9 blue, 1 green
Game 40: 1 blue, 2 red, 2 green; 2 green, 14 blue; 2 red, 6 blue; 13 blue; 2 green, 10 blue
Game 41: 1 red, 1 blue, 1 green; 11 green, 1 red; 4 green; 5 green; 1 blue, 1 red, 10 green
Game 42: 4 blue, 3 red, 2 green; 6 red, 1 blue, 6 green; 11 red, 7 blue, 3 green; 6 blue, 7 red, 1 green; 11 red, 1 green, 6 blue; 2 blue, 4 green, 10 red
Game 43: 3 red, 5 blue; 2 green, 4 red, 3 blue; 7 red, 10 blue, 13 green
Game 44: 13 green, 5 blue, 3 red; 1 green, 5 blue, 8 red; 11 green, 4 blue, 9 red; 5 blue, 7 green, 9 red
Game 45: 12 red, 9 blue, 5 green; 9 green, 3 red; 3 green, 11 blue, 15 red
Game 46: 5 blue, 2 green, 1 red; 1 blue, 3 red, 3 green; 2 green, 7 blue
Game 47: 8 red, 8 green, 5 blue; 12 blue, 8 green, 7 red; 5 red, 1 blue, 2 green; 1 red, 4 green, 6 blue; 1 red, 3 blue; 5 green, 1 red, 3 blue
Game 48: 3 blue, 2 red, 5 green; 4 green, 5 blue; 3 blue, 13 green, 5 red
Game 49: 4 red, 9 blue, 1 green; 12 red, 8 blue; 5 red, 2 blue, 1 green; 11 red, 2 green, 9 blue; 8 red, 9 blue, 3 green
Game 50: 3 blue, 2 red; 3 blue, 7 green; 4 red, 2 blue, 8 green; 7 green, 2 blue, 4 red; 3 red, 3 green; 6 green, 4 red, 2 blue
Game 51: 9 blue, 4 red, 2 green; 5 red, 3 green, 3 blue; 5 green, 10 blue, 5 red; 8 red, 11 blue, 5 green; 1 red, 3 blue, 7 green
Game 52: 1 blue, 9 red, 6 green; 8 red, 1 blue, 4 green; 13 green, 3 blue, 6 red; 3 green, 9 red; 3 blue, 12 green, 7 red
Game 53: 1 blue, 9 green; 1 red, 2 green; 7 green, 1 red
Game 54: 3 green, 3 blue, 9 red; 6 blue, 11 green, 1 red; 6 green, 1 red, 4 blue; 4 blue, 2 red, 13 green; 3 green, 1 red; 6 blue, 3 green, 8 red
Game 55: 1 blue, 6 green; 4 red, 5 green; 8 red, 12 green; 5 red, 1 blue, 7 green; 1 blue, 11 red, 3 green
Game 56: 1 green, 11 red, 1 blue; 2 green, 8 blue, 3 red; 5 blue, 6 red, 1 green
Game 57: 5 green, 3 red, 2 blue; 10 green, 12 blue, 16 red; 7 blue, 13 red, 11 green
Game 58: 5 green, 16 blue, 5 red; 9 blue, 2 green, 5 red; 5 blue, 3 red, 9 green
Game 59: 2 blue, 2 red; 7 blue, 3 green, 4 red; 2 green, 1 blue
Game 60: 12 red, 5 green, 1 blue; 2 blue, 12 red, 4 green; 16 red, 4 green, 2 blue
Game 61: 3 green, 1 blue, 6 red; 4 green, 1 blue, 8 red; 4 red, 1 blue, 1 green; 4 green, 13 red
Game 62: 2 red, 4 blue; 2 blue, 13 green, 8 red; 4 red, 9 green, 4 blue; 8 green, 3 red, 7 blue; 3 blue, 6 red, 3 green
Game 63: 1 green, 3 blue; 6 blue, 4 red, 3 green; 3 blue, 1 green, 1 red; 2 green, 2 blue, 3 red; 1 red, 2 blue; 5 red, 6 blue
Game 64: 7 red, 10 blue, 4 green; 1 green, 18 red, 2 blue; 7 blue, 2 green; 10 red, 1 green, 7 blue; 3 green, 5 blue, 11 red
Game 65: 11 red, 2 blue; 1 green, 2 blue, 1 red; 3 blue, 2 green, 3 red; 3 blue, 3 red, 7 green
Game 66: 3 red, 7 blue, 11 green; 10 blue, 4 green, 9 red; 11 blue, 11 red, 12 green; 8 red, 7 blue, 10 green; 5 red, 14 green, 3 blue
Game 67: 5 green, 1 red; 7 green, 4 blue; 3 red, 1 green, 3 blue
Game 68: 9 blue, 11 green, 10 red; 12 blue, 3 red, 3 green; 8 red, 7 green, 9 blue
Game 69: 1 green, 7 blue, 1 red; 1 red, 9 blue; 1 green, 2 red
Game 70: 9 green, 2 blue, 1 red; 1 red, 2 blue, 16 green; 13 green, 4 blue, 13 red; 8 red, 7 green, 6 blue; 12 green, 3 blue, 3 red
Game 71: 2 green, 4 red, 6 blue; 11 green, 6 blue, 2 red; 3 green, 1 blue, 5 red; 7 blue, 6 green
Game 72: 4 blue, 1 green; 4 blue; 1 green, 3 blue; 4 blue; 1 red, 4 blue; 3 blue
Game 73: 4 red, 1 green, 7 blue; 15 green, 4 blue, 17 red; 19 green, 3 blue, 11 red; 13 green, 5 blue, 1 red; 10 blue, 13 green, 17 red
Game 74: 9 green, 2 blue, 18 red; 5 red, 8 green; 3 green, 4 blue, 3 red; 5 green, 3 blue
Game 75: 1 red, 10 blue, 1 green; 2 red, 19 blue; 4 red, 10 blue; 3 red, 7 blue, 1 green; 2 red, 3 blue
Game 76: 4 green, 9 red, 7 blue; 8 green, 7 blue; 12 green, 9 red
Game 77: 1 red, 6 blue, 2 green; 8 red, 5 green, 4 blue; 4 blue, 2 red, 3 green
Game 78: 9 blue, 1 red, 8 green; 2 green, 9 blue; 2 green, 9 blue
Game 79: 4 blue, 4 green, 1 red; 4 blue, 4 red, 4 green; 4 green, 1 blue, 6 red; 6 green; 6 red
Game 80: 13 red, 8 blue; 2 green, 14 red, 13 blue; 7 red, 9 blue; 11 red, 18 blue; 2 blue, 3 red, 1 green
Game 81: 2 green, 9 red, 12 blue; 5 green, 5 red, 13 blue; 5 blue, 5 red; 2 red, 8 blue
Game 82: 6 red, 15 green; 1 blue, 15 red, 13 green; 6 green, 1 blue, 1 red; 5 red, 6 green, 1 blue
Game 83: 1 green; 1 blue, 1 green, 10 red; 7 red, 1 blue; 1 green, 11 red; 2 blue, 1 green, 3 red
Game 84: 17 green, 8 red; 1 blue, 14 green, 2 red; 6 red, 1 blue, 6 green; 4 red, 10 green, 1 blue; 2 red, 2 blue, 1 green; 4 blue, 5 green, 3 red
Game 85: 5 blue, 3 red; 1 blue, 1 green; 6 green, 1 blue, 1 red; 4 green, 2 blue, 7 red
Game 86: 7 red, 3 blue, 4 green; 1 blue, 13 red; 3 red, 3 blue, 6 green; 1 blue, 1 green, 17 red; 8 blue, 13 red, 4 green; 6 blue, 4 green, 17 red
Game 87: 10 red, 3 green, 4 blue; 12 green, 10 red, 3 blue; 2 green, 16 red; 16 red, 3 blue, 14 green; 14 green, 11 red, 1 blue; 9 red, 4 blue, 6 green
Game 88: 7 green, 4 red, 19 blue; 1 green, 5 red, 18 blue; 19 blue, 3 green, 6 red; 9 green, 14 blue, 5 red; 3 green, 5 red
Game 89: 4 red, 2 blue, 10 green; 6 blue, 5 red; 3 green, 4 blue, 1 red; 12 green, 2 red, 2 blue; 3 blue, 3 green, 3 red
Game 90: 1 green, 19 red, 1 blue; 7 blue, 4 green, 10 red; 6 blue, 3 green, 13 red
Game 91: 1 green, 9 blue; 7 green, 4 red, 3 blue; 6 green, 2 red, 8 blue; 1 red, 1 blue; 3 red, 2 green
Game 92: 18 red, 2 green, 2 blue; 6 blue, 4 red, 6 green; 3 blue, 10 red; 8 blue, 2 green, 7 red
Game 93: 13 blue, 3 green, 15 red; 14 red, 2 green, 7 blue; 1 blue, 4 green, 13 red; 19 red, 5 green
Game 94: 6 blue; 5 green, 8 blue; 1 red, 9 blue; 1 red, 8 blue; 5 green, 6 blue; 1 red
Game 95: 9 blue, 14 green; 2 green, 1 red, 1 blue; 1 red, 3 green, 2 blue; 6 green, 1 red; 1 red, 8 blue, 14 green; 1 green, 5 blue
Game 96: 7 blue, 17 green; 19 green, 3 red, 2 blue; 6 green, 2 red, 2 blue; 3 blue, 16 green; 3 red, 20 green; 4 green, 2 blue
Game 97: 1 green, 1 red, 1 blue; 4 red, 2 blue; 7 red; 6 red; 7 red
Game 98: 2 red, 15 green; 10 green, 1 red; 1 red, 11 blue, 11 green; 13 blue, 8 green, 2 red; 1 red, 12 green, 7 blue
Game 99: 14 red, 2 blue, 1 green; 3 green, 13 red, 9 blue; 9 red, 9 blue, 2 green; 13 red, 7 green, 5 blue; 5 blue, 3 green, 11 red
Game 100: 1 blue, 1 red, 1 green; 8 blue, 1 green; 1 green, 7 blue, 1 red; 1 green, 4 blue, 1 red; 1 green, 3 blue"""

puzzle_solver = GameFinder(12, 13, 14, puzzle_string)
print(puzzle_solver.game_sum)
print(puzzle_solver.power_sum)

unittest.main()