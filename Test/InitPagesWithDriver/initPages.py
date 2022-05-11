from Infra.SeleniumInfra import SeleniumInfra
from Pages.BasePage import BasePage
from Pages.LoginPage.LoginPageActions import LoginPageActions

class InitPagesWithDriver:
    def __init__(self):
        self.seleniumInfra = SeleniumInfra()
        self.bp = BasePage(self.seleniumInfra)
        self.lp = LoginPageActions(self.seleniumInfra)
