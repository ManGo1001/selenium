from selenium import webdriver


class Wework:
    def __init__(self):
        # 远程调试：
        chrome_options = webdriver.ChromeOptions()
        chrome_options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(5)

    def quit(self):
        self.driver.quit()