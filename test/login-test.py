from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from support.loginPage import LoginPage
from support.dashboardPage import DashboardPage

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# driver configuration data
desired_caps = {
    "deviceName": "Pixel 5",
    "platformName": "Android",
    "appPackage": "com.chikkanna.tgcloginapp",
    "appActivity": "com.chikkanna.tgcloginapp.LoginActivity",
    "realDevice": True
}

# create driver connection
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

# page object instances
loginPage = LoginPage(driver)
dashboardPage = DashboardPage(driver)

# test case body
loginPage.login('system')
dashboardPage.assertWelcomeMessage()
dashboardPage.logOut()
loginPage.assertLoginLabel()

# test finish
driver.quit()
print('End of test!')