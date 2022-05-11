from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as actions
from selenium.webdriver.support.wait import WebDriverWait


class SeleniumInfra:
    TIME_TO_WAIT = 60

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('disable-notifications')
        self.driver = webdriver.Chrome("/home/enot/PycharmProjects/Swag/Tools/chromedriver",  options=chrome_options)

    def genericScroll(self, element=None, direction=None, locatorTypeToWait=None, locatorValueToWait=None,
                      loopsToWait=6, myOwnLoop=None, pixelBorder=100):
        x = element.location['x']
        y = element.location['y']

        if "rightToLeft" == direction:
            xStart = x + element.size['width'] - pixelBorder
            yStart = y + element.size['height'] / 2
            xEnd = x + pixelBorder
            yEnd = y + element.size['height'] / 2

        elif "leftToRight" == direction:
            xStart = x + pixelBorder
            yStart = y + (element.size['height'] / 2)
            xEnd = x + element.size['width'] - pixelBorder
            yEnd = y + (element.size['height'] / 2)

        elif "upToDown" == direction:
            xStart = x + (element.size['width'] / 2)
            yStart = y + pixelBorder
            xEnd = x + element.size['width'] / 2
            yEnd = y + element.size['height'] - pixelBorder

        elif "downToUp" == direction:
            xStart = x + (element.size['width'] / 2)
            yStart = y + element.size['height'] - pixelBorder
            xEnd = x + (element.size['width'] / 2)
            yEnd = y + pixelBorder

        if myOwnLoop:
            self.scrollToCordinate(xStart=xStart, yStart=yStart, xEnd=xEnd, yEnd=yEnd)
        else:
            self.moveToElementUntilHeExist(locatorTypeToWait=locatorTypeToWait, locatorValueToWait=locatorValueToWait,
                                           loopsToWait=loopsToWait, xStart=xStart, yStart=yStart, xEnd=xEnd, yEnd=yEnd)


    def moveToElementUntilHeExist(self, locatorTypeToWait=None, locatorValueToWait=None, loopsToWait=None, xStart=None,
                                  yStart=None, xEnd=None, yEnd=None):
        counter = 0
        while not self.isElementExist(locatorType=locatorTypeToWait, locatorValue=locatorValueToWait,
                                      timeToWait=0) and counter < loopsToWait:
            self.scrollToCordinate(xStart=xStart, yStart=yStart, xEnd=xEnd, yEnd=yEnd)
            counter += 1

    def scrollToCordinate(self, xStart=None, yStart=None, xEnd=None, yEnd=None, element=None):
        try:
            actions.click_and_hold(element).move_to(x=xEnd, y=yEnd).release().perform()
        except:
            raise Exception("not scrolling check if there is a banner ")

    def openSite(self, link):
        self.driver.get(link)
        self.driver.maximize_window()

    def waitUntil(self, timeToWait=None):
        self.driver.implicitly_wait(timeToWait)

    def findElementBy(self, locatorType=None, locatorValue=None, fromElement=None,
                      timeToWait=TIME_TO_WAIT) -> WebElement:
        retries = 1
        wait = WebDriverWait(self.driver, timeToWait)
        while retries > 0:
            try:
                self.waitUntil(timeToWait)
                timeToWait = None
                if (not fromElement):
                    if (locatorType == "id"):
                        element = wait.until(EC.visibility_of_element_located((By.ID, locatorValue)))
                    elif (locatorType == "xpath"):
                        element = wait.until(EC.visibility_of_element_located((By.XPATH, locatorValue)))
                    elif (locatorType == "class_Name"):
                        element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, locatorValue)))
                    elif locatorType == "ids":
                        element = self.driver.find_elements(locatorValue)
                else:
                    if (locatorType == "id"):
                        element = fromElement.find_element_by_id(locatorValue)
                    elif (locatorType == "xpath"):
                        element = fromElement.find_element_by_xpath(locatorValue)
                    elif (locatorType == "class_Name"):
                        element = fromElement.find_elements_by_class_name(locatorValue)
                print("[findElementBy]- Element Does FOUND with:" + str(locatorType) + " " + str(locatorValue))
                return element
            except:
                raise Exception("[findElementBy]- Element Does NOT FOUND with:" + str(locatorType) + " " + str(
                    locatorValue) + " check this warning its can be a bug!!!")

    def isElementExist(self, locatorType=None, locatorValue=None, fromElement=None, timeToWait=TIME_TO_WAIT):
        self.waitUntil(timeToWait)
        try:
            if not fromElement:
                if (locatorType == "id"):
                    element = self.driver.find_element_by_id(locatorValue).is_displayed()
                elif (locatorType == "xpath"):
                    element = self.driver.find_element_by_xpath(locatorValue).is_displayed()
            else:
                if (locatorType == "id"):
                    element = fromElement.find_element_by_id(locatorValue).is_displayed()
                elif (locatorType == "xpath"):
                    element = fromElement.driver.find_element_by_xpath(locatorValue).is_displayed()
            print("[isElementExist] - The element " + str(locatorValue) + " is exist")
            print(element)
            return element
        except:
            print("[isElementExist] -FALSE  The element " + str(locatorValue) + " not exist")
            return False

    def findElementListBy(self, locatorType=None, locatorValue=None, fromElement=None, timeToWait=TIME_TO_WAIT):
        self.waitUntil(timeToWait)
        try:
            if not fromElement:
                fromElement = self.driver
            if locatorType == "id":
                elementList = fromElement.find_elements_by_id(locatorValue)
                print("[findElementListBy]- " + locatorValue + " has found by" + locatorType)
                return elementList
            elif locatorType == "xpath":
                elementList = fromElement.find_elements_by_xpath(locatorValue)
                print("[findElementListBy]- " + locatorValue + " has found by" + locatorType)
                return elementList
            elif locatorType == "class_Name":
                elementList = fromElement.find_elements(locatorValue)
                print("[findElementListBy]- " + locatorValue + " has found by" + locatorType)
                return elementList
        except:
            print("[findElementBy]- Element Does NOT FOUND with:" + str(locatorType) + " " + str(
                locatorValue) + "check this warning its can be a bug!!!")

    def close(self):
        try:
            self.driver.quit()
        except:
            print("There is no option to quit")

    def getTextFromElement(self, locatorType=None, locatorValue=None, element=None, fromElement=None,
                           timeToWait=TIME_TO_WAIT):
        if (not element):
            element = self.findElementBy(locatorType=locatorType, locatorValue=locatorValue,
                                         fromElement=fromElement, timeToWait=timeToWait)
        try:
            text = element.text
            print("[getText]- get text: " + str(text) + " on " + str(locatorValue))
            return text
        except:
            raise Exception("[CouldNOTgetText]- get text: " + str(text) + " on " + str(locatorValue))

    def clickButton(self, locatorType: By = None, locatorValue: str = None, element: WebElement = None,
                    fromElement: WebElement = None, timeToWait: int = TIME_TO_WAIT):
        if not element:
            element = self.findElementBy(locatorType=locatorType, locatorValue=locatorValue, fromElement=fromElement,
                                         timeToWait=timeToWait)
        try:
            element.click()
            print("[Pressed]- element " + str(locatorValue) + " is pressed")
        except Exception as e:
            assert False, "the element " + str(locatorValue) + " found but we cant click on it!"


    def getURL(self):
        return self.driver.current_url

    def goBack(self):
        self.driver.back()