from appium import webdriver
from appium.webdriver.common.mobileby import AppiumBy
import re

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    
    def __init__(self,driver):
        self.driver = driver
        self.usernameInput = (AppiumBy.ID,'com.chikkanna.tgcloginapp:id/usernameField')
        self.otpLabel = (AppiumBy.ID,'com.chikkanna.tgcloginapp:id/otptxt')
        self.passwordInput = (AppiumBy.ID, 'com.chikkanna.tgcloginapp:id/passwordField')
        self.logInButton = (AppiumBy.ID, 'com.chikkanna.tgcloginapp:id/loginBtn')
        self.logInLabel = (AppiumBy.ID,'com.chikkanna.tgcloginapp:id/loginLabel')
        self.wait = WebDriverWait(self.driver, 3000)

    def login(self,username):
        # fill username
        self.driver.find_element(*self.usernameInput).send_keys(username)
        # get otp text
        otp = self.driver.find_element(*self.otpLabel).text
        # extract password from otp
        password = re.findall(r'\d+', otp)[0]
        # fill in password
        self.driver.find_element(*self.passwordInput).send_keys(password)
        # click on log in button
        self.driver.find_element(*self.logInButton).click()
        print('Log in function finished!')

    def assertLoginLabel(self):
        logInLabel = self.wait.until(EC.visibility_of_element_located(self.logInLabel))
        assert logInLabel.is_displayed()
        print('Login assert finished!')



