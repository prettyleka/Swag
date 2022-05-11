from Infra.SeleniumInfra import SeleniumInfra

class BasePage:
    def __init__(self, seleniumInfra :SeleniumInfra):
        self.seleniumInfra = seleniumInfra


    def moveToSite(self ,link):
        self.seleniumInfra.openSite(link=link)
