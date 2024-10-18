import pytest

from Config.config import TestData
from Pages.Loginpage import LoginPage
from Pages.test_base import BaseText


class Test_Login(BaseText):



    def do_Login_page(self):
        self.LoginPage=LoginPage(self.driver)
        self.LoginPage.do_login(TestData.USER_NAME,TestData.PASSWORD)
