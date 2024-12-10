from pynput.mouse import Controller as MouseController, Button
from pynput.keyboard import Controller as KeyboardController, Key
import time

# Initialize mouse and keyboard controllers
mouse = MouseController()
keyboard = KeyboardController()

def automate_task():
    while True:  # Forever loop
        try:
            # Step 1: Press Ctrl+Shift+N to open a new incognito window
            keyboard.press(Key.ctrl)
            keyboard.press(Key.shift)
            keyboard.press('n')
            keyboard.release('n')
            keyboard.release(Key.shift)
            keyboard.release(Key.ctrl)
            print("Opened a new incognito window")
            time.sleep(2)  # Wait for the incognito window to open
            
            # Step 2: Type the URL "https://app.sli.do/event/1VW5NGfMCLFmCCDUdD22P1"
            url = "https://app.sli.do/event/1VW5NGfMCLFmCCDUdD22P1"
            keyboard.type(url)
            print(f"Typed the URL: {url}")
            
            # Step 3: Press Enter to load the URL
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            print("Pressed Enter to load the URL")
            time.sleep(5)  # Wait for 5 seconds for the page to load
            
            # Step 4: Press Tab 22 times
            for _ in range(22):
                keyboard.press(Key.tab)
                keyboard.release(Key.tab)
                time.sleep(0.1)  # Short delay between tabs
            print("Pressed Tab 22 times")
            
            # Step 5: Press the down arrow key twice
            for _ in range(2):
                keyboard.press(Key.down)
                keyboard.release(Key.down)
                time.sleep(0.1)  # Short delay between presses
            print("Pressed Down Arrow 2 times")
            
            # Step 6: Press Enter
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            print("Pressed Enter to confirm selection")
            
            # Step 7: Close the tab with Ctrl+F4
            time.sleep(2)  # Brief pause before closing
            keyboard.press(Key.ctrl)
            keyboard.press(Key.f4)
            keyboard.release(Key.f4)
            keyboard.release(Key.ctrl)
            print("Closed the tab with Ctrl+F4")
            
            # Small delay before the next loop iteration
            time.sleep(5)  # Adjust as needed
            
        except KeyboardInterrupt:
            print("Script stopped by user.")
            break  # Exit the loop on manual interruption

if __name__ == "__main__":
    automate_task()
