import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from urllib.parse import quote
import threading
import time


class WhatsAppMessenger:
    def __init__(self, master):
        self.master = master
        master.title("WhatsApp Messenger")

        self.message_label = tk.Label(master, text="Message:")
        self.message_label.pack()

        self.message_entry = tk.Text(master, height=10, width=50)
        self.message_entry.pack()

        self.numbers_label = tk.Label(master, text="Phone Numbers (one per line):")
        self.numbers_label.pack()

        self.numbers_entry = tk.Text(master, height=5, width=50)
        self.numbers_entry.pack()

        self.send_button = tk.Button(master, text="Send Messages", command=self.send_messages)
        self.send_button.pack()

        self.status_label = tk.Label(master, text="")
        self.status_label.pack()

    def send_messages(self):
        message = self.message_entry.get("1.0", tk.END).strip()
        numbers = self.numbers_entry.get("1.0", tk.END).strip().splitlines()
        
        if not message:
            messagebox.showerror("Error", "Please enter a message.")
            return
        if not numbers:
            messagebox.showerror("Error", "Please enter at least one phone number.")
            return

        self.status_label.config(text="Sending messages...")
        threading.Thread(target=self.start_sending, args=(message, numbers)).start()

    def start_sending(self, message, numbers):
        msg = quote(message)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        
        link = 'https://web.whatsapp.com'
        driver.get(link)

        time.sleep(30)  # Allow time for the user to scan the QR code

        # Use a set to track unique numbers
        unique_numbers = set(number.strip() for number in numbers if number.strip())

        # Prepare to send the same message to all numbers
        for number in unique_numbers:
            link2 = f'https://web.whatsapp.com/send/?phone=91{number}&text={msg}&app_absent=0'
            driver.get(link2)
            time.sleep(10)  # Allow time for the page to load
            
            try:
                # Wait for the message input to be ready and send the message
                WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true']")))
                action = ActionChains(driver)
                action.send_keys(Keys.ENTER)
                action.perform()
                time.sleep(10)  # Wait for the message to be sent
            except Exception as e:
                print(f"Failed to send message to {number}: {e}")

        driver.quit()  # Close the browser when done
        self.status_label.config(text="Messages sent!")


if __name__ == "__main__":
    root = tk.Tk()
    app = WhatsAppMessenger(root)
    root.mainloop()
