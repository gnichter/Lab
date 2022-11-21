import pytest
from account import Account


def testinit():
    testName = Account('Jimmy')
    assert testName.get_name() == 'Jimmy'
    assert testName.get_balance() == 0


def test_deposit():
    testName = Account('Jimmy')
    testName.deposit(-70)
    assert testName.get_balance() == 0
    testName.deposit(70)
    assert testName.get_balance() == 70
    testName.deposit(0)
    assert testName.get_balance() == 70


def test_withdarawl():
    testName = Account('Jimmy')
    testName.deposit(90)
    testName.withdraw(-75)
    assert testName.get_balance() == 0
    testName.deposit(75)
    assert testName.get_balance() == 15
    testName.deposit(0)
    assert testName.get_balance() == 15
