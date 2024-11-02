from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# Specify the path to chromedriver
chrome_service = Service("C:\\Users\\nages\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_service)

# Open WhatsApp Web
driver.get("https://web.whatsapp.com")

# Pause to allow manual QR code scan
input("Press Enter after scanning QR code in WhatsApp Web...")

# Define your contacts as mobile numbers (in international format with country code) and message
contacts = ["+917319705065"]  # Replace with actual mobile numbers
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
        message_box.send_keys(message + Keys.ENTER)
        sleep(1)  # Small delay to ensure message is sent
        print(f"Message sent to {contact} successfully.")
    except Exception as e:
        print(f"Could not send message to {contact}. Error: {e}")

# Send messages to each contact
for contact in contacts:
    send_message(driver, contact, message)

print("All messages processed.")
# Uncomment the next line to automatically close the browser after sending messages
# driver.quit()
