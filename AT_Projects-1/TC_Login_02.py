from selenium import webdriver
from selenium.webdriver.common.by import By
from Locators import first_login
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# LOGIN FAILED PROCESS
class orangeHRM:

    def __init__(self, web_url):
        self.url = web_url
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.implicitly_wait(8)
        wait = WebDriverWait(self.driver, 20)
        try:
            wait.until(EC.url_matches('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'))

            admin_box = wait.until(EC.presence_of_element_located((By.NAME, first_login().admin)))
            admin_box.send_keys('Admin')

            pass_box = wait.until(EC.presence_of_element_located((By.NAME, first_login().password_fail)))
            pass_box.send_keys('admin1234')

            login_box = wait.until(EC.element_to_be_clickable((By.XPATH, first_login().login_button)))
            login_box.click()

            inavaild_text = wait.until(EC.presence_of_element_located((By.XPATH, first_login().invaild)))
            ele_1 = inavaild_text.text

            assert ele_1 == 'Invalid credentials'

            print("SUCCESS : Login failed Username ")

        except TimeoutException:
            print("FAIL : Login passed Username ")

    def shutdown(self):
        self.driver.quit()


url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

login_web = orangeHRM(url)

login_web.login()

login_web.shutdown()
