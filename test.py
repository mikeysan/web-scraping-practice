import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options 

# Set the options we want. In this case headless
options = Options() 
options.headless = True


driver = webdriver.Firefox(executable_path=r'C:\WebDrvTools\bin\geckodriver.exe', options=options)

with driver:
    driver.get("https://www.reddit.com/")
    search = driver.find_element(By.NAME, "q")

    search.send_keys("scraping")
    search.send_keys(Keys.ENTER)

    search_results = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, "rpBJOHq2PR60pnwJlUyP0"))
    )
    posts = search_results.find_elements_by_css_selector("h3._eYtD2XCVieq6emjKBH3m")

    for post in posts:
        header = post.find_element_by_tag_name("span")
        print(header.text)

