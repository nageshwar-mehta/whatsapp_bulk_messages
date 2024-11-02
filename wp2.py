from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep

# Set up Chrome options to use the existing profile
chrome_options = Options()

# REPLACE <YourUsername> with your actual Windows username.
# Ensure the path points to the location where your Chrome user data is stored.
chrome_options.add_argument("user-data-dir=C:\\Users\\Nages\\AppData\\Local\\Google\\Chrome\\User Data")

# REPLACE "Default" with the name of the Chrome profile where WhatsApp Web is logged in
# ("Profile 1", "Profile 2", etc., if you use other profiles). Use "Default" for the main profile.
chrome_options.add_argument("profile-directory=Default")

# Initialize the WebDriver with the existing profile
# REPLACE with the path to your chromedriver executable
chrome_service = Service("C:\\Users\\nages\\Downloads\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Open WhatsApp Web (it should already be logged in with the specified Chrome profile)
driver.get("https://web.whatsapp.com")
sleep(5)  # Wait for WhatsApp Web to load

# Define your contacts as mobile numbers (in international format with country code) and message
# REPLACE the numbers with the actual WhatsApp numbers (include country code, e.g., "+1234567890")
contacts = ["+917319705065"]
# REPLACE with the actual message you want to send
message = "Hello! This is a bulk message sent using an automated script."

def send_message(driver, contact, message):
    # Search for the contact by number
    search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
    search_box.clear()
    search_box.send_keys(contact)
    sleep(2)  # Wait for the search results to update

    # Select the contact from the search results
    try:
        contact_box = driver.find_element(By.XPATH, f'//span[@title="{contact}"]')
        contact_box.click()
        sleep(1)

        # Find the message box and send the message
        message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="1"]')
   
