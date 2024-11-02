from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from urllib.parse import quote
import time

# Read and URL-encode the message from 'message.txt'
try:
    with open('message.txt', 'r') as file: 
        msg = file.read()
except FileNotFoundError:
    print("Error: 'message.txt' not found.")
    msg = ""

# URL-encode the message
msg = quote(msg)

# Read phone numbers from 'numbers.txt'
numbers = []
try:
    with open('numbers.txt', 'r') as file:
        for num in file:
            numbers.append(num.strip())  # Use strip() to remove newline and whitespace
except FileNotFoundError:
    print("Error: 'numbers.txt' not found.")

# Optional: Print the numbers for verification (commented out)
# print(numbers)

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

link = 'https://web.whatsapp.com'
driver.get(link)

# Optional: Use WebDriverWait for better handling instead of sleep
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# Example of waiting for the QR code element (you might need to adapt this)
# WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//div[@class="_1C6Z2"]')))

# Optional: Sleep for a short duration to allow user to scan QR code
time.sleep(30)


for i in range(len(numbers)):

# Construct the link for sending the message
    if numbers:  # Check if the numbers list is not empty
        link2 = f'https://web.whatsapp.com/send/?phone=91{numbers[i]}&text={msg}'
        driver.get(link2)
    else:
        print("No phone numbers available to send a message.")

# Optional: Sleep for a short duration to allow the message to be sent
    time.sleep(5)  # Adjust time as needed for your interaction
    action = ActionChains(driver)
    action.send_keys(Keys.ENTER)
    action.perform()
    time.sleep(5)
# Make sure to quit the driver when done
# driver.quit()  # Uncomment this line to close the browser when done
