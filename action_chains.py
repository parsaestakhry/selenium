from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)

driver.get("https://orteil.dashnet.org/cookieclicker/")
# in action chains we create a list of things to do in order of sequence 
actions = ActionChains(driver)
#cookie consent automation
try:
    consent_element = WebDriverWait(driver , 10).until(
        EC.presence_of_element_located((By.CLASS_NAME , "fc-button-label"))
    )
    consent_element.click()
except:
    pass
#selecting the english as the main language 
driver.implicitly_wait(5)
lang_element = driver.find_element(By.ID , "langSelect-EN")
lang_element.click()
# finding the cookie and the cookie count
cookies = driver.find_element(By.ID , "bigCookie")
cookie_count = driver.find_element(By.ID , "cookies")
