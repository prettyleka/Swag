import time

from Infra.SeleniumInfra import SeleniumInfra
from Pages.LoginPage.LoginPageLocators import LoginPageLocators


class LoginPageActions:
    def __init__(self, seleniumInfra: SeleniumInfra):
        self.seleniumInfra = seleniumInfra
        self.locators = LoginPageLocators()

    def getAllUserNames(self):
        uNames = self.seleniumInfra.getTextFromElement(*self.locators.userNames)
        onlyNames = uNames.split(":\n")[1].split("\n")
        return onlyNames

    def checkThePicturesAreSame(self):
        allLinks=[]
        allPictures = self.seleniumInfra.findElementListBy(*self.locators.imgLink)
        for x in allPictures:
            link = x.get_attribute("src")
            if link in allLinks:
                pass
            else:
                allLinks.append(link)
        if len(allLinks)==1:
            return True
        else:
            return False




    def getPassword(self):
        password = self.seleniumInfra.getTextFromElement(*self.locators.userPassword)
        onlyP = password.split(":\n")[1]
        return onlyP

    def insertDifferentValidCredentials(self, unames, password):
        for x in unames:
            inputUN = self.seleniumInfra.findElementBy(*self.locators.userNameInput)
            inputP = self.seleniumInfra.findElementBy(*self.locators.passwordInput)
            inputUN.clear()
            inputUN.send_keys(x)
            inputP.clear()
            inputP.send_keys(password)
            self.seleniumInfra.clickButton(*self.locators.loginBtn)
            if x=='standard_user':
                assert self.seleniumInfra.getURL()=="https://www.saucedemo.com/inventory.html"
                self.seleniumInfra.goBack()
            elif x=='locked_out_user':
                assert self.seleniumInfra.isElementExist(*self.locators.errorMsgContainer)==True
            elif x=='problem_user':
                assert self.checkThePicturesAreSame()==True
                assert self.seleniumInfra.getURL()=="https://www.saucedemo.com/inventory.html"
                self.seleniumInfra.goBack()
            elif x=='performance_glitch_user':
                assert self.seleniumInfra.getURL()=="https://www.saucedemo.com/inventory.html"
                self.seleniumInfra.goBack()

    def clickLoginBtnWithoutCredentials(self):
        inputUN = self.seleniumInfra.findElementBy(*self.locators.userNameInput)
        inputP = self.seleniumInfra.findElementBy(*self.locators.passwordInput)
        inputUN.clear()
        inputP.clear()
        self.seleniumInfra.clickButton(*self.locators.loginBtn)
        assert self.seleniumInfra.isElementExist(*self.locators.errorMsgContainer)==True

    def insertOnlyPassword(self, password):
        inputP = self.seleniumInfra.findElementBy(*self.locators.passwordInput)
        inputP.send_keys(password)
        assert self.seleniumInfra.isElementExist(*self.locators.errorMsgContainer)==True


    def insertOnlyUsername(self, username):
        inputP = self.seleniumInfra.findElementBy(*self.locators.passwordInput)
        inputP.clear()
        inputUN = self.seleniumInfra.findElementBy(*self.locators.userNameInput)
        inputUN.clear()
        inputUN.send_keys(username)
        assert self.seleniumInfra.isElementExist(*self.locators.errorMsgContainer)==True

    def insertWrongCredentials(self, username, password):
        inputP = self.seleniumInfra.findElementBy(*self.locators.passwordInput)
        inputUN = self.seleniumInfra.findElementBy(*self.locators.userNameInput)
        inputUN.clear()
        inputP.clear()
        inputUN.send_keys(username)
        inputP.send_keys(password)
        assert self.seleniumInfra.isElementExist(*self.locators.errorMsgContainer)==True



