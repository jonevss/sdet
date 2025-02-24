from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import random
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains

class FormPage(BasePage):
    URL = "https://practice-automation.com/form-fields/"

    NAME = (By.ID, "name-input")
    PASSWORD = (By.XPATH, "//label[contains(text(), 'Password')]/input")
    DRINKS = (By.NAME, "fav_drink")
    COLOR = (By.NAME, "fav_color")
    AUTOMATION = (By.NAME, "automation")
    EMAIL = (By.ID, "email")
    MESSAGE = (By.ID, "message")
    SUBMIT = (By.ID, "submit-btn")

    def open_page(self):
        self.open(self.URL)

    def fill_form(self, name, password, email):
        self.driver.find_element(*self.NAME).send_keys(name)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        drink = self.driver.find_elements(*self.DRINKS)
        for checkbox in drink:
            if checkbox.get_attribute("value") == "Milk" or checkbox.get_attribute("value") == "Coffee":
                ActionChains(self.driver).move_to_element(checkbox).click().perform()
        colr = self.driver.find_elements(*self.COLOR)
        for radio in colr:
            if radio.get_attribute("value") == "Yellow":
                ActionChains(self.driver).move_to_element(radio).click().perform()
                break

        dropdown = Select(self.driver.find_element(*self.AUTOMATION))
        options = dropdown.options[1:]  # Исключаем первый пустой <option>
        random_option = random.choice(options)
        dropdown.select_by_value(random_option.get_attribute("value"))

        self.driver.find_element(*self.EMAIL).send_keys(email)

        tools = self.driver.find_elements(By.XPATH, "//label[contains(text(), 'Automation tools')]/following-sibling::ul/li")
        count = len(tools)
        longest = max(tools, key=lambda item: len(item.text)).text
        message = str(count) + '\n' + str(longest)

        self.driver.find_element(*self.MESSAGE).send_keys(message)

    def submit_form(self):
        submit_button = self.driver.find_element(*self.SUBMIT)
        ActionChains(self.driver).move_to_element(submit_button).click().perform()

    def get_alert_text(self):
        return self.driver.switch_to.alert.text
