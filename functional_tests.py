from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

deployment_url = "http://isaac-jesse-mentalhealthtracker.pbp.cs.ui.ac.id"
class ExampleFunctionalTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()


    def login(self):
        self.browser.get(deployment_url)
        username_input = self.browser.find_element(by=By.NAME, value="username")
        password_input = self.browser.find_element(by=By.NAME, value="password")
        username_input.send_keys("isaac.jesse")
        password_input.send_keys("9a%=i#L=H29X?gr")
        
        # Wait for the submit button to be present and click it using the provided XPath
        submit_button = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/form/table/tbody/tr[3]/td[2]/input"))
        )
        submit_button.click()
        time.sleep(2)

    def test_heading_text_is_correct(self):
        self.login()  # Log in if required
        self.browser.get(deployment_url)
        element: WebElement = self.browser.find_element(by=By.TAG_NAME, value="h1")
        self.assertEqual("Mental Health Tracker", element.text)

    def test_page_title_is_correct(self):
        self.browser.get(deployment_url)
        self.assertEqual("PBD Mental Health Tracker", self.browser.title)

if __name__ == "__main__":
    unittest.main()