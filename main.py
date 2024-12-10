from pynput.mouse import Controller as MouseController, Button
from pynput.keyboard import Controller as KeyboardController, Key
import time

# Initialize mouse and keyboard controllers
mouse = MouseController()
keyboard = KeyboardController()

# Define the screen coordinates for the clicks
click_points = [
      # First point
    (1800, 244),  # Second point
    (473, 91),  # Third point
    (685, 364),  # Fourth point
    (483, 423)   # Fifth point
]

def automate_clicks():
    while True:
        for index, point in enumerate(click_points):
            # Move the mouse to the specified point
            mouse.position = point
            time.sleep(0.1)  # Short delay to ensure positioning
            # Perform a click
            mouse.click(Button.left, 1)
            print(f"Clicked at {point}")
            
            # After the second click, perform Ctrl+V (paste)
            if index == 1:
                keyboard.press(Key.ctrl)
                keyboard.press('v')
                keyboard.release('v')
                keyboard.release(Key.ctrl)
                time.sleep(1)
                keyboard.release(Key.enter)
                print("Performed Ctrl+V")
                time.sleep(5)
            # Wait for 2 seconds before the next action
            else:
                time.sleep(2)
            
            
            

if __name__ == "__main__":
    try:
        automate_clicks()
    except KeyboardInterrupt:
        print("Script stopped by user.")
