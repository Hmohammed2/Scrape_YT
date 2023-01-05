from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time 
import re
import pandas as pd
# provide the url of the channel whose data you want to fetch

bulk_list = pd.read_excel('YTData.xlsx', sheet_name=0) # can also index sheet by name or fetch all sheets
mylist = bulk_list['URLs'].tolist()

def options(url_id, headless):
    options = ChromeOptions()
    if headless == "yes":
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
    else:
        options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get(url_id)
    return driver

def main():
    for url in mylist:
        
        driver = options(url, "yes")
        wait_in_seconds = 10
        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, 
            "//*[@id='yDmH0d']/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/form[2]/div/div/button/span"))).click()
        except:
            driver.quit()
        # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='tabsContent']/tp-yt-paper-tab[7]/div"))).click()
        time.sleep(2)
        try:
            c_name = driver.find_element(By.XPATH, "//*[@id='text']")
            sub_count = driver.find_element(By.XPATH, "//*[@id='subscriber-count']")
            join_date = driver.find_element(By.XPATH, "//*[@id='right-column']/yt-formatted-string[2]/span[2]")
            Total_channel_views = driver.find_element(By.XPATH, "//*[@id='right-column']/yt-formatted-string[3]")
            description = driver.find_element(By.XPATH, '//*[@id="description" and @class="style-scope ytd-channel-about-metadata-renderer"]')
            # pattern_email = re.compile("[A-z0-9]+(.)[A-z0-9]+@[a-z]+\.[a-z]{2,3}")
            pattern_info = re.compile("(?:https?:\/\/)?(?:www\.)?(?:twitter|tiktok|facebook|instagram|twitch)?(?:\.com)\/([@a-z+A-Z0-9-_])+")
            # search_email = pattern_email.search(description.text)
            search_info = pattern_info.search(description.text)
        except:
            driver.quit()

        if search_info is None:
            print(f'Subscriber Count: {sub_count.text}, Channel name: {c_name.text}, Joined: {join_date.text}, Total Channel views: {Total_channel_views.text}, Email Address: Hidden')
        else:
            print(f'Subscriber Count: {sub_count.text}, Channel name: {c_name.text}, Joined: {join_date.text}, Total Channel views: {Total_channel_views.text}, Info: {search_info.group()}')

        time.sleep(wait_in_seconds)
    
    driver.quit()

if __name__ == "__main__":
    main()

  