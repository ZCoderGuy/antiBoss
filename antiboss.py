import pyautogui

#Query the user on the destination site
askUser = input("Where would you like to go?")
destination = list(askUser)

#Opening the task manager
pyautogui.keyDown('esc', 'shift')
pyautogui.keyUp('esc', 'shift')

#Finding the iBoss process and closing it
output = pyautogui.locateOnScreen('iboss.png')
location = pyautogui.center(output)
pyautogui.click(location)
pyautogui.typewrite('enter')

#Select the address bar and go to the requested website
pyautogui.keyDown('control', 'l')
pyautogui.keyUp('control', 'l')
pyautogui.typewrite(destination)
pyautogui.typewrite('enter')

