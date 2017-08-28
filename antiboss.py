import pyautogui

#Opening the task manager
pyautogui.keyDown('esc', 'shift')
pyautogui.keyUp('esc', 'shift')

#Finding the iBoss process and closing it
output = pyautogui.locateOnScreen('iboss.png')
location = pyautogui.center(output)
pyautogui.click(location)
pyautogui.typewrite('enter')


