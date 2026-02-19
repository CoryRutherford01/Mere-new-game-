import pyautogui as pag
import time
import pyperclip
import subprocess

actions = [
    (610, 531, 4), (286, 459, 4), (610, 531, 4), (610, 531, 4),
    (610, 531, 4), (610, 531, 4), (387, 253, 10), (387, 298, 4),
    (564, 598, 4), (610, 531, 4), (849, 746, 10), (522, 388, 4),
    (460, 321, 4), (506, 387, 4), (397, 437, 4), (394, 286, 4),
    (510, 312, 4), (521, 502, 4),
]

time.sleep(10)
password = "JoyZon3Tech"
timeout = "10"
    
for x, y, duration in actions:
    if (x, y, duration) == (387, 253, 10):
        pag.click(x, y, duration=duration)
        pag.typewrite(password)
    elif (x, y, duration) == (387, 298, 4):
        pag.click(x, y, duration=duration)
        pag.typewrite(password)
    elif (x, y, duration) == (460, 321, 4):
        pag.rightClick(x, y, duration=duration)
    elif (x, y, duration) == (610, 531, 4):
        pag.click(x, y, duration=duration)
        cmd = r'"C:\Program Files (x86)\LiteManager Pro - Server\ROMServer.exe" /start'
        subprocess.run(cmd, shell=True)
    elif (x, y, duration) == (510, 312, 4):
        pag.click(x, y, duration=duration)
        pag.press('backspace')
        pag.press('backspace')
        pag.typewrite(timeout)
    else:
        pag.click(x, y, duration=duration)

clipboard_text = pyperclip.paste()
with open('show.bat', 'a') as f:
    f.write(f'\necho LiteManager ID: {clipboard_text}')
    f.write(f'\necho LiteManager Password : {password}')
print("Done")
