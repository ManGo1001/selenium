from test_po.contact_page import ContactPage
from time import sleep, time
from selenium import webdriver

from test_po.wework_page import Wework


class TestContact:
    def setup(self):
        self.work = Wework()
        self.contact = ContactPage(self.driver)
        

    def teardown(self):
        self.work.quit()

    def test_add_member(self):
        contact = ContactPage(self.driver)
        contact.add_member("mango", "man", "go", "13011112222")
        assert contact.get_tips() == "OK"

    def test_add_member_Chinese(self):
        self.contact.add_member("慢慢", "满", "go_1", "13011112223")
        assert self.contact.get_tips() == "OK"

    def test_delete_member(self):
        udid = str(time())
        #如果一个对象方法返回的是PO自身，那么可以采用链式调用
        self.contact.add_member("慢慢"+udid, "满"+udid, "go_1"+udid, "13011112224")\
            .delete_member()

    def test_update_profile(self):
        self.contact.search("121")
