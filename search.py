from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#preventing chrome from closing automatically
options = Options()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
#going to the website
driver.get("https://www.techwithtim.net/")
driver.implicitly_wait(5)
#finding the search element
search_element = driver.find_element(By.NAME , "s")
driver.implicitly_wait(6)
#sending keys in a search box
search_element.send_keys("test")
#pressing enter to see the result for the sent key
search_element.send_keys(Keys.RETURN)
driver.implicitly_wait(5)


try:
    main_element = WebDriverWait(driver , 10).until(
        EC.presence_of_element_located((By.ID , "main"))
    )
    #there are multiple article tags in the page, we search through all of them, then in each article tag there is a class called entry header that
    #we can access it by looping through each tag which is stored in articles tag
    articles = driver.find_elements(By.TAG_NAME , "article")
    for article in articles:
        header = driver.find_element(By.CLASS_NAME , "entry-header")
        print(header.text)
finally:
    driver.quit()

