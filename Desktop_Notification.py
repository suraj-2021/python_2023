# Desktop Notifier in Python

# Importing the required modules
from plyer import notification
import time

# Main function
if __name__ == '__main__':
    # Infinite loop to show notifications repeatedly
    while True:
        # Showing notification using the plyer module
        notification.notify(
            title="Take Rest", 
            message="Rest is essential for health, we should take a rest after certain time.", 
            timeout=5
        )
        # Sleep for 1 hour before showing the next notification
        time.sleep(60 * 60)

# To run the notifier in the background even after closing the command prompt, use "pythonw filename.py" in the command prompt.
