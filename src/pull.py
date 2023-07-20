import os
from dotenv import load_dotenv
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# Load the environment variables from the .env file
dotenv_path = os.path.join(os.path.dirname(os.getcwd()), 'sunpowered-download', '.env')
load_dotenv(dotenv_path)

# Get the mysunpower.com login credentials from the environment variables
login_email = os.getenv('EMAIL')
login_password = os.getenv('PASSWORD')

# URL of the website
url = 'https://mysunpower.com/'

# Create a headless Chrome browser instance
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)

# Open the URL and enter login credentials
driver.get(url)

time.sleep(5)

email_field = driver.find_element_by_name('email')
password_field = driver.find_element_by_name('password')

email_field.send_keys(login_email)
password_field.send_keys(login_password + Keys.RETURN)

time.sleep(5)

# Find the required element with the specific class and alt attribute
element = driver.find_element_by_xpath('//img[contains(@class, "widget-icon") and contains(@alt, "Download data in Excel format")]')

# Get the src attribute
src = element.get_attribute('src')

# Download the excel file
response = requests.get(src)

with open('downloaded_file.xlsx', 'wb') as f_out:
    f_out.write(response.content)

print('Excel file downloaded as downloaded_file.xlsx')

# Close the browser
driver.quit()