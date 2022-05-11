from selenium.webdriver.common.by import By


class LoginPageLocators:
    def __init__(self):
        self.userNames = (By.XPATH, "//*[@id='login_credentials']")
        self.userPassword = (By.XPATH, "//div[@class='login_password']")
        self.userNameInput = (By.ID, "user-name")
        self.passwordInput = (By.ID, "password")
        self.loginBtn = (By.ID, "login-button")
        self.errorMsgContainer = (By.XPATH, "//div[@class='error-message-container error']")
        self.imgLink = (By.XPATH, '//div[@class="inventory_list"]//img')

