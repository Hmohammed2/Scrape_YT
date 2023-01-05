from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time 
import re
import pandas as pd

channel_name = []
subscriber_count = []
joined_date = []
Total_channel_views_column = []
email_address_column = []
contact_info = []

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
        
        driver = options(url, "no")
        wait_in_seconds = 5
        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, 
            "//*[@id='yDmH0d']/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/form[2]/div/div/button/span"))).click()
        except:
            driver.quit()
        time.sleep(2)
        try:
            c_name = driver.find_element(By.XPATH, "//*[@id='text']")
            sub_count = driver.find_element(By.XPATH, "//*[@id='subscriber-count']")
            join_date = driver.find_element(By.XPATH, "//*[@id='right-column']/yt-formatted-string[2]/span[2]")
            Total_channel_views = driver.find_element(By.XPATH, "//*[@id='right-column']/yt-formatted-string[3]")
            description = driver.find_element(By.XPATH, '//*[@id="description" and @class="style-scope ytd-channel-about-metadata-renderer"]')
            pattern_email = re.compile("[A-z0-9]+(.)[A-z0-9]+@[a-z]+\.[a-z]{2,3}")
            search_email = pattern_email.search(description.text)
            # pattern_info = re.compile("(?:https?:\/\/)?(?:www\.)?(?:twitter|tiktok|facebook|instagram|twitch)?(?:\.com)\/([@a-z+A-Z0-9-_])+")
            # search_info = pattern_info.search(description.text)
        except:
            driver.quit()

        channel_name.append(c_name.text)
        Total_channel_views_column.append(Total_channel_views.text)
        subscriber_count.append(sub_count)
        joined_date.append(join_date.text)

        if search_email is None:
            email_address_column.append("N/A")
        else:
            email_address_column.append(search_email.group())
        
        print(c_name.text, Total_channel_views.text)

        driver.close()

        time.sleep(wait_in_seconds)

    driver.quit()

    df = pd.DataFrame({"Channel Name": channel_name, "Total Channel views": Total_channel_views_column,
                                    "Subscriber Count": subscriber_count, "Date joined": joined_date, "Email Address": search_email})

    df.to_excel("Data_saved.xlsx")

if __name__ == "__main__":
    main()

  