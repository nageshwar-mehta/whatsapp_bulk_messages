import pywhatkit as pwk
from datetime import datetime, timedelta

def send_instant_messages(contact_list, message):
    # Get the current time
    now = datetime.now()
    hour = now.hour
    minute = now.minute + 1  # Schedule for 1 minute from now to allow WhatsApp Web to open

    for number in contact_list:
        try:
            # Send message with pywhatkit
            pwk.sendwhatmsg(number, message, hour, minute)
            print(f"Message sent to {number}")
            # Wait for a brief moment to avoid overlap
            minute += 2
            if minute >= 60:
                minute = 0
                hour = (hour + 1) % 24  # Wrap around hour if it reaches 24
        except Exception as e:
            print(f"Failed to send message to {number}: {e}")

# List of contacts in WhatsApp format (with country code, e.g., "+1234567890")
contacts = ["+917319705065"]

# Customize your message
message = "Hello! This is an instant message sent using an automated script."

# Call the function
send_instant_messages(contacts, message)
