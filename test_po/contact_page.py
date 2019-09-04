from time import sleep

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from test_po.base_page import BasePage
from test_po.profile_page import ProfilePage


class ContactPage(BasePage):
    def add_member(self, name, alias, id, phone, **kwargs):
        # self.driver.find_element(By.CSS_SELECTOR, ".js_add_member").click()

        # todo:找到元素的位置，确认位置是否正确
        # for index in range(10):
        #     print(self.driver.find_element_by_css_selector(".js_has_name .js_add_member").location)
        #     sleep(0.5)
        # print(self.driver.page_source)


        locator = WebDriverWait(self.driver, 10, 1, ignored_exceptions=(TimeoutException)).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".js_add_member")))
        self.click_by_js(By.CSS_SELECTOR, locator)
        self.driver.find_element(By.NAME, "username").send_keys(name)
        self.driver.find_element(By.NAME, "english_name").send_keys(alias)
        self.driver.find_element_by_name("acctid").send_keys(id)
        self.driver.find_element_by_name("mobile").send_keys(phone)
        self.click_by_js(By.CSS_SELECTOR, ".js_btn_cancel")

        return self  #退回当前页面

    def delete_member(self):
        pass

    def get_tips(self):
        return "OK"

    def search(self, key):
        self.driver.find_element_by_id("memberSearchInput").send_keys(key)
        return ProfilePage(self.driver)
