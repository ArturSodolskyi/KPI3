import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(ChromeDriverManager().install())

def testing():
    phone = 'new balance 1500'
    driver.implicitly_wait(20)
    driver.get('https://hotline.ua/')

    driver.find_element(By.CSS_SELECTOR, "input.field").send_keys(phone, Keys.ENTER)
    time.sleep(5)
    result = driver.find_element(By.CSS_SELECTOR, 'div.search__no-items-title').text

    assert phone.lower() in result.lower(), 'За запитом new balance 1500 нічого не знайдено'

    driver.quit()

testing()