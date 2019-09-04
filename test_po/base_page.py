from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click_by_js(self, locator):

        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element(locator)
                                   )