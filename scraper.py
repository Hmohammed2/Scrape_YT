import undetected_chromedriver as uc
from selenium.webdriver import ActionChains
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
import time 
import re
import pandas as pd

# channel_name = []
# subscriber_count = []
# joined_date = []
# Total_channel_views_column = []
# email_address_column = []
# contact_info = []

# urls = ["https://www.youtube.com/@oxlee/about",
# "https://www.youtube.com/@officialjulseyhiphop/about",
# "https://www.youtube.com/@DarrenLevy/about",
# "https://www.youtube.com/@EoinRBLX/about",
# "https://www.youtube.com/@ShammiLTD/about",
# "https://www.youtube.com/@DeanLewis/about",
# "https://www.youtube.com/@ge3t3eshorts/about",
# "https://www.youtube.com/@Mikaylah/about",
# "https://www.youtube.com/@babiesofyoutube/about",
# "https://www.youtube.com/@Sam.Fricker/about",
# "https://www.youtube.com/@RyanWilliamsofficial/about",
# "https://www.youtube.com/@DebbieDooKidsTV/about",
# "https://www.youtube.com/@sunnykidssongs3422/about",
# "https://www.youtube.com/@YummyYummyToys/about",
# "https://www.youtube.com/@BreeLenehan/about",
# "https://www.youtube.com/@lilbootzes1/about",
# "https://www.youtube.com/@howridiculous/about",
# "https://www.youtube.com/@lachlan/about",
# "https://www.youtube.com/@waywayofficial/about",
# "https://www.youtube.com/@gdaydk/about",
# "https://www.youtube.com/@RamZaes/about",
# "https://www.youtube.com/@neonchang/about",
# "https://www.youtube.com/@kawaiikunicorn/about",
# "https://www.youtube.com/@LyannaKea/about",
# ]

urls = ["https://www.youtube.com/@DebbieDooKidsTV/about"]
# bulk_list = pd.read_excel('YTData.xlsx', sheet_name=0) # can also index sheet by name or fetch all sheets
# mylist = bulk_list['URLs'].tolist()

def login_gmail(driver, email, passw):
    try:

        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='buttons']/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div"))).click()
        except:
            driver.quit()
        #Type the email address 
        
        emailid = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "identifierId")))
        emailid.send_keys(email)

        #Click on the next button 

        nextButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "identifierNext")))

        ActionChains(driver).move_to_element(nextButton).click().perform()

        #Type the password 

        try:

            passwordid = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "Passwd")))

            passwordid.send_keys(passw)

        except:

            passwordid = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "password")))

            passwordid.send_keys(passw)


        #Click on the signin button 

        time.sleep(10)

        signinButton = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "passwordNext")))

        ActionChains(driver).move_to_element(signinButton).click().perform()

        time.sleep(30)

        return True

    except:

        return False

def options(url_id, headless):
    options = ChromeOptions()
    ua = UserAgent()
    user_agent = ua.random
    print(user_agent)

    if headless == "yes":
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        options.add_argument(f'user-agent={user_agent}')
    else:
        options.add_argument("--start-maximized")
        options.add_argument(f'user-agent={user_agent}')

    driver = uc.Chrome(options=options)
    driver.get(url_id)
    
    return driver

def main():

    url = "https://www.youtube.com/"
        
    driver = options(url, "no")
    wait_in_seconds = 5
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, 
        "//*[@id='yDmH0d']/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/form[2]/div/div/button/span"))).click()
    except:
        driver.quit()
    # WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 
        # "td.style-scope:nth-child(3) > ytd-button-renderer:nth-child(1) > yt-button-shape:nth-child(1) > button:nth-child(1) > yt-touch-feedback-shape:nth-child(2) > div:nth-child(1) > div:nth-child(2)"))).click()
    
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='buttons']/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div")))
    except:
        driver.quit()

    try:
        login_gmail(driver, "XXXX.com", "XXXX")
    except Exception:
        # login failed
        driver.quit()

        
    for y_url in urls:

        driver.execute_script(f'window.open{url}')
        time.sleep(10)
        driver.quit()

    #     try:
    #         c_name = driver.find_element(By.XPATH, "//*[@id='text']")
    #         sub_count = driver.find_element(By.XPATH, "//*[@id='subscriber-count']")
    #         join_date = driver.find_element(By.XPATH, "//*[@id='right-column']/yt-formatted-string[2]/span[2]")
    #         Total_channel_views = driver.find_element(By.XPATH, "//*[@id='right-column']/yt-formattedtring[3]")
    #         description = driver.find_element(By.XPATH, '//*[@id="description" and @class="style-scope ytd-channel-about-metadata-renderer"]')
    #         pattern_email = re.compile("[A-z0-9]+(.)[A-z0-9]+@[a-z]+\.[a-z]{2,3}")
    #         search_email = pattern_email.search(description.text)
    #         pattern_info = re.compile("(?:https?:\/\/)?(?:www\.)?(?:twitter|tiktok|facebook|instagram|twitch)?(?:\.com)\/([@a-z+A-Z0-9-_])+")
    #         search_info = pattern_info.search(description.text)
    #     except:
    #         driver.quit()

    #     channel_name.append(c_name.text)
    #     Total_channel_views_column.append(Total_channel_views.text)
    #     subscriber_count.append(sub_count.text)
    #     joined_date.append(join_date.text)

    #     if search_email is None:
    #         email_address_column.append("N/A")
    #     else:
    #         email_address_column.append(search_email.group())

    #     if search_info is None:
    #         contact_info.append("N/A")
    #     else:
    #         contact_info.append(search_info.group())
        
    #     print(c_name.text, Total_channel_views.text)

    #     driver.close()

    #     time.sleep(wait_in_seconds)
    
    # driver.quit()

    # df = pd.DataFrame({"Channel Name": channel_name, "Total Channel views": Total_channel_views_column,
    #                                 "Subscriber Count": subscriber_count, "Date joined": joined_date, "Email Address": email_address_column,
    #                                     "Contact Info": contact_info})

    # df.to_excel("Data_saved.xlsx")


if __name__ == "__main__":
    main()
