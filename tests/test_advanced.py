import pytest
from exercises.advanced import factorial


def test_factorial():
    assert sorted(factorial(1)) == [1]
    assert sorted(factorial(2)) == [2]
    assert sorted(factorial(7)) == [7]
    assert sorted(factorial(21)) == [3, 7]
    assert sorted(factorial(40)) == [2, 2, 2, 5]
    assert sorted(factorial(693)) == [3, 3, 7, 11]
    assert sorted(factorial(39270)) == [2, 3, 5, 7, 11, 17]


def test_yahtzee_score():
    pass  # Här skriver du som elev tester till uppgiften.


def test_blackjack_score():
    assert blackjack_score(cards())
