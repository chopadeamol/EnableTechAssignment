from selenium.webdriver.common.by import By

class AddProduct:
    active_app_xpath = "/html/body/div[1]/div/main/div[2]/div/div/div[1]/div/div/h6/a"
    start_application_xpath = "/html/body/div[1]/div/main/div[2]/div/div[2]/div/div[1]/button"
    business_checking_xpath = "/html/body/div[1]/div/main/div[2]/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/button"
    view_cart_xpath = "/html/body/div[1]/div/main/div[2]/div/div/div/div/div[1]/button"
    checkout_xpath = "/html/body/div[4]/div[3]/div/div[2]/button[2]"

    def __init__(self,driver):
        self.driver = driver

    def active_application(self):
        self.driver.find_element(By.XPATH,self.active_app_xpath).click()

    def start_application(self):
        self.driver.find_element(By.XPATH,self.start_application_xpath).click()

    def product_to_cart(self):
        self.driver.find_element(By.XPATH,self.business_checking_xpath).click()

    def view_cart(self):
        self.driver.find_element(By.XPATH, self.view_cart_xpath).click()

    def checkout(self):
        self.driver.find_element(By.XPATH,self.checkout_xpath).click()
