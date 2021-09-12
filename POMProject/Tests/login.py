from selenium import webdriver
import unittest
from POMProject.Pages.loginPage import LoginPage
from POMProject.Pages.homePage import HomePage


class LoginTest(unittest.TestCase):
    def setUp(self) :
        self.driver=webdriver.Firefox()

        self.driver.implicitly_wait(10)

    def Test_Login_valid(self):
        driver=self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        login=LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage=HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()
        #self.driver.find_element_by_name("txtUsername").send_keys("Admin")
        #self.driver.find_element_by_name("txtPassword").send_keys("admin123")
        #self.driver.find_element_by_name("Submit").click()
        #time.sleep(5)
        #self.driver.find_element_by_id("welcome").click()
        #self.driver.find_element_by_link_text("Logout").click()
        #time.sleep(2)

    def tearDown(self):
        self.driver.close()
        self.driver.quit() 
        print("test completed")
        
if __name__== '__main__':
    unittest.main()