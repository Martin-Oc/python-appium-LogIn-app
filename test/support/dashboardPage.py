from appium import webdriver
from appium.webdriver.common.mobileby import AppiumBy

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    def __init__(self,driver):
        self.driver = driver
        self.welcomeMessage = (AppiumBy.ID, 'com.chikkanna.tgcloginapp:id/successMsg')
        self.logOutButton = (AppiumBy.ID, 'com.chikkanna.tgcloginapp:id/logoutBtn')
        self.confirmLogOutButton = (AppiumBy.ID, 'android:id/button1')
        self.wait = WebDriverWait(self.driver, 3000)

    def assertWelcomeMessage(self):
        welcomeMessage = self.wait.until(EC.visibility_of_element_located((self.welcomeMessage)))
        assert welcomeMessage.is_displayed()
        print('Welcome message assert finished!')

    def logOut(self):
        # click on log out button
        self.driver.find_element(*self.logOutButton).click()
        # click on log out confirmation button
        confirmButton = self.wait.until(EC.visibility_of_element_located(self.confirmLogOutButton))
        confirmButton.click()
        print('Log out finished!')


    