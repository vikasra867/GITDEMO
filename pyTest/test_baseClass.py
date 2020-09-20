import pytest

from pyTest.test_baseClass1 import  TestBaseClass


@pytest.mark.usefixtures("dataLoad")
class TestUseBase(TestBaseClass):

    def test_useClass(self, dataLoad):
        #log = BaseClass.getLogger()
        log = self.getLogger()
        log.info(dataLoad)
        #log.INFO(dataLoad[0])

