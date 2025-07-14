import pytest
import numpy as np
from TwentyFourOrAnyNumGameSolver.solver import game_solver

"""Test game_solver function in 24orAnyNumGameSolver.function.

game_solver
------------

The function is tested with the following cases:

1. get 8 with [8]
2. get 8 with [7]
3. get 8 with [4,4]
4. get 0 with [4,4]
5. get 16 with [4,4]
6. get 1 with [4,4]
7. get 16 with [2,2,2]
8. get 4 with [2,2]
9. get 101 with [1111,8,10,8,7,2,101]


"""


class Test_game_solver:
    def test_get_8_with_8(self):
        assert game_solver([8], 8) == "8"

    def test_get_8_with_7(self):
        assert game_solver([7], 8) is np.nan

    def test_get_8_with_4_4(self):
        assert game_solver([4, 4], 8) == "4 add 4"

    def test_get_0_with_4_4(self):
        assert game_solver([4, 4], 0) == "4 subtract 4"

    def test_get_16_with_4_4(self):
        assert game_solver([4, 4], 16) == "4 multiply 4"

    def test_get_1_with_4_4(self):
        assert game_solver([4, 4], 1) == "4 divide 4"

    def test_get_16_with_2_2_2(self):
        assert game_solver([2, 2, 2], 16) == "2 power 2 power 2" or "2 add 2 power 2"

    def test_get_4_with_2_2(self):
        assert (
            game_solver([2, 2], 4) == "2 add 2" or "2 multiply 2"
        )  # this case can have mutiple solutions

    def test_big_number_case(self):
        assert (
            game_solver([1111, 8, 10, 8, 7, 2, 101], 101)
            == "7 subtract 101 subtract 8 multiply 10 add 2 add 8 add 1111"
        )
