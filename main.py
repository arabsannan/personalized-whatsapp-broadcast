from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pandas as pd
from dotenv import load_dotenv
import os

# load environment variables
load_dotenv()
CHROME_PROFILE_PATH = os.environ['CHROME_PROFILE_PATH']   # path//to//AppData/Local/Google/Chrome/User Data/Default
CHROME_DRIVER = os.environ['CHROME_DRIVER']   # path//to//chromedriver

# Stay logged in after first successful login
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"user-data-dir={CHROME_PROFILE_PATH}")

# Initialize Chrome
browser = webdriver.Chrome(options=chrome_options, executable_path=CHROME_DRIVER)
wait = WebDriverWait(browser, 60)
print("Chrome opened successfully!")

# Open Whatsapp
whatsapp_web = 'https://web.whatsapp.com/'
browser.get(whatsapp_web)
print("Accessing Whatsapp web")

# Convert excel columns to lists
df = pd.read_excel("whatsapp_contacts.xlsx")  # Excel file containing contact details
Number = df['Number'].tolist()
Name = df['Name'].tolist()
# Variable = df['Something variable'].tolist()


# For loop to get contacts
for i, j in zip(Number, Name):
    # find Search box
    Search = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='_13NKt copyable-text selectable-text']")))
    time.sleep(2)

    Search.send_keys(i)
    time.sleep(1)
    Search.send_keys(Keys.ENTER)
    time.sleep(3)

    # find Message(Chat) box
    Message = browser.find_element_by_xpath("//div[@class='fd365im1 to2l77zo bbv8nyr4 mwp4sxku gfz4du6o ag5g9lrv']")
    time.sleep(2)

    Message.send_keys('Hello ' + str(j) + ',')
    time.sleep(1)

    Message.send_keys(Keys.SHIFT, Keys.ENTER)   # enter a newline
    Message.send_keys(Keys.SHIFT, Keys.ENTER)

    Message.send_keys("This is just a python bot I'm testing. Kindly ignore")
    time.sleep(1)
    Message.send_keys(Keys.ENTER)   # send message in the chatbox

    print('Sent to ' + str(j))

browser.quit()
