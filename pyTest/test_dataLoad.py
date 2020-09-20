import pytest
import self

from pyTest.test_baseClass1 import BaseClass


def test_dataLoad1(dataLoad):
    print(dataLoad[0])


def test_dataLoad2(dataLoad):
    print(dataLoad[0])
    print(dataLoad[1])


def test_dataLoad3(dataLoad):
    print(dataLoad[0])
    print(dataLoad[1])
    print(dataLoad[2])


def test_crossBrowser(crossBrowser):
    print(crossBrowser)
    print(crossBrowser[1])


