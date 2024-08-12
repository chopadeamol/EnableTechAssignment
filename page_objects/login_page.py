from selenium.webdriver.common.by import By


class LoginPage:
    with_google_xpath = "/html/body/div/div/div[1]/div/div/div[2]/button[1]"
    # login_with_google_xpath = "//button[contains(text(),'Login with Google')]"
    email_username_xpath = "//input[@type='email']"
    next_button_xpath = "//span[contains(text(),'Next')]"
    email_password_xpath = "//input[@type='password']"
    more_ways_to_verify_xpath = "//span[contains(text(),'More ways to verify')]"
    tap_yes_xpath = "//div[contains(text(),'Tap ')]"
    continue_xpath = "//span[contains(text(),'Continue')]"

    def __init__(self, driver):
        self.driver = driver

    def login_with_google(self):
        self.driver.find_element(By.XPATH,self.with_google_xpath).click()

    def first_window(self):
        before = self.driver.window_handles[0]
        return before

    def second_window(self):
        after = self.driver.window_handles[1]
        return after

    def setUserName(self,username):
        self.driver.find_element(By.XPATH,self.email_username_xpath).send_keys(username)

    def click_next(self):
        self.driver.find_element(By.XPATH,self.next_button_xpath).click()

    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.email_password_xpath).send_keys(password)

    def verify_auth(self):
        self.driver.find_element(By.XPATH,self.more_ways_to_verify_xpath).click()

    def tap_yes_auth(self):
        self.driver.find_element(By.XPATH, self.tap_yes_xpath).click()

    def continue_button(self):
        self.driver.find_element(By.XPATH,self.continue_xpath).click()
