from pynput.mouse import Listener
import pyautogui
import cv2

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    if not pressed:
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_click=on_click) as listener:
    listener.join()
im=pyautogui.screenshot()
#cv2.imwrite("C:/Users/Shubhangi/Desktop/FINAL_YEAR_PROJECT/UsabilityEvaluation/Real_Time_logging/"+"ss.png",im)

