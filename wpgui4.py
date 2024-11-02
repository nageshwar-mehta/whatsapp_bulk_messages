import tkinter as tk
from tkinter import messagebox, filedialog
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
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

        self.numbers_entry = tk.Text(master, height=10, width=50)
        self.numbers_entry.pack()

        self.image_button = tk.Button(master, text="Select Image", command=self.select_image)
        self.image_button.pack()

        self.image_path = None  # Variable to store the selected image path

        self.send_button = tk.Button(master, text="Send Messages", command=self.send_messages)
        self.send_button.pack()

        self.status_label = tk.Label(master, text="")
        self.status_label.pack()

    def select_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.gif")])
        if self.image_path:
            messagebox.showinfo("Selected Image", f"Image selected: {self.image_path}")

    def send_messages(self):
        message = self.message_entry.get("1.0", tk.END).strip()
        numbers = self.numbers_entry.get("1.0", tk.END).strip().splitlines()
        
        if not message and not self.image_path:
            messagebox.showerror("Error", "Please enter a message or select an image.")
            return
        if not numbers:
            messagebox.showerror("Error", "Please enter at least one phone number.")
            return

        self.status_label.config(text="Sending messages...")
        threading.Thread(target=self.start_sending, args=(message, numbers)).start()

    def start_sending(self, message, numbers):
        msg = quote(message) if message else ""
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        
        link = 'https://web.whatsapp.com'
        driver.get(link)

        time.sleep(30)  # Allow time for the user to scan the QR code

        for number in numbers:
            number = number.strip()
            if number:
                link2 = f'https://web.whatsapp.com/send/?phone=91{number}&text={msg}'
                driver.get(link2)
                time.sleep(6)  # Allow time for the page to load

                if self.image_path:
                    # Locate the input element for file upload
                    input_box = driver.find_element("xpath", '//input[@type="file"]')
                    input_box.send_keys(self.image_path)  # Send the path of the image

                    time.sleep(15)  # Wait for the image to upload

                if message:  # Send the text message if provided
                    action = ActionChains(driver)
                    action.send_keys(Keys.ENTER)
                    action.perform()

                time.sleep(10)  # Wait before sending the next message

        driver.quit()  # Close the browser when done
        self.status_label.config(text="Messages sent!")


if __name__ == "__main__":
    root = tk.Tk()
    app = WhatsAppMessenger(root)
    root.mainloop()
