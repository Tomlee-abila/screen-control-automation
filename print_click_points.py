from pynput.mouse import Listener

def on_click(x, y, button, pressed):
    if pressed:
        print(f"Mouse clicked at ({x}, {y}) with {button}")

# Set up the mouse listener
with Listener(on_click=on_click) as listener:
    print("Click anywhere on the screen to print coordinates. Press Ctrl+C to exit.")
    listener.join()
