import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
@pytest.fixture
def driver():
    chrome_driver_path = "C:\\Users\\Admin\\OneDrive\\Рабочий стол\\project\\first\\chromedriver.exe"  # Путь к драйверу
    service = Service(chrome_driver_path)
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
