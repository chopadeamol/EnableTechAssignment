import time
from page_objects.login_page import LoginPage
from page_objects.add_product import AddProduct
from utilities.customLogger import LogGenerator
from utilities.readProperties import ReadConfig
import allure

@allure.feature('Login feature')
@allure.severity(allure.severity_level.NORMAL)
@allure.description("Test to login with google and add product to cart and checkout")
class Test_login_1:
    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGenerator.genLog()

    def test_login_1(self,setup):
        try:
            self.logger.info("The test is being started here....!")
            self.driver = setup
            with allure.step("Opening baseURL in the applied browser"):
                self.driver.get(self.baseURL)
            self.driver.maximize_window()
            time.sleep(5)
            self.login = LoginPage(self.driver)
            with allure.step("Clicking on 'login with google'"):
                self.login.login_with_google()
            time.sleep(5)
            with allure.step("Switching window"):
                self.driver.switch_to.window(self.login.second_window())
            time.sleep(5)
            with allure.step(f"Entering username: {self.username}"):
                self.login.setUserName(self.username)
            time.sleep(5)
            self.login.click_next()
            time.sleep(5)
            with allure.step(f"Entering password: {self.password}"):
                self.login.setPassword(self.password)
            time.sleep(5)
            self.login.click_next()
            try:
                if self.login.verify_auth():
                    self.logger.info("Click on more ways to verify")
                elif self.login.continue_button():
                    self.logger.info("click on continue button")
            except Exception as e:
                self.logger.info(f"Exception occurred: {e}")
                time.sleep(5)
            self.driver.switch_to.window(self.login.first_window())
            time.sleep(5)
            self.addProd = AddProduct(self.driver)
            with allure.step("clicking on Applications"):
                self.addProd.active_application()
            time.sleep(5)
            with allure.step("clicking on start application"):
                self.addProd.start_application()
            time.sleep(5)
            with allure.step("clicking on product to add in cart"):
                self.addProd.product_to_cart()
            time.sleep(5)
            with allure.step("clicking on cart to view"):
                self.addProd.view_cart()
            time.sleep(10)
            with allure.step("clicking on checkout"):
                self.addProd.checkout()
        except Exception as e:
            print(f"An error occurred while running test: {e}")