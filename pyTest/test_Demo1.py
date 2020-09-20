# pytest -v -s shows console logs
# pytest test_Demo1 -v -s    for single file
# pytest -k <Reglaur express> -v -s (Regular expression means string )
# -v for Meta data(more info)
# -s for output on console
# mark the test using -m
# mark test case for Skip
# @pytest.mark.xfail execution happens but operation will happen
# Fixtures are to invoke some pre-requisites and post-requisites
# conftest.py is to generalize the fixture for All methods
# Request only when there is params in fixtures
# scope is used in fixture to define scope to class, it will execute before and after class initiated and end
# report can be done using "pytest -v -s --html report.html"


# Logs : Info warming error critical

import pytest




@pytest.mark.usefixtures("setup")
class TestExample():

    @pytest.mark.smoke
    def test_firstProgram(self):
        print("first Hello")

    @pytest.mark.skip
    def test_secondProgram(self):
        print("Second Hello")

    @pytest.mark.xfail
    def test_thirdProgram(self):
        print("Third Hello")
        var = "Third Hello"
        assert "Third" in var, "Not in var"

    def test_call(self):
        print("Call after fixture only")



