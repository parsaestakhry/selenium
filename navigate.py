from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)

driver.get("https://www.techwithtim.net/")
driver.implicitly_wait(5)
#you can navigate through the links, by using the link text element in html (not rhe link itself )
python_element = driver.find_element(By.LINK_TEXT , "Python Programming")
python_element.click()

try:
    element = WebDriverWait(driver , 10).until(
        EC.presence_of_element_located((By.LINK_TEXT , "Beginner Python Tutorials"))
    )
    py_tutorial = driver.find_element(By.LINK_TEXT , "Beginner Python Tutorials")
    py_tutorial.click()

    get_started = WebDriverWait(driver , 10).until(
        EC.presence_of_element_located((By.ID , "sow-button-19310003"))
    )
    get_started.click()
    
except:
    pass
