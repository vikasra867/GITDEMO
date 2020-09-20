#Request only when there is params in fixtures

import pytest


@pytest.fixture(scope="class")
def setup():
    print("Used in Chrome open or get function for URL opening")
    yield
    print("I am last executing")


@pytest.fixture()
def dataLoad():
    print("In data Load fixture")
    return ["Rahul", "Shetty", "Email@rahul.sheety"]


@pytest.fixture(params=[("chrome","Vikas"),"firefox","IE"])
def crossBrowser(request):
    return request.param

