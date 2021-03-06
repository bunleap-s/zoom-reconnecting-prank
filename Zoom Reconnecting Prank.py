# All import modules
import pyautogui as pg
import time

# Functions

def muteZoomAudio() :
    # locate the Mute-Audio Button
    pg.moveTo(x=32, y=711)
    pg.click()

def stopZoomVideo() :
    # locate the Stop-Video Button
    pg.moveTo(x=111, y=712)
    pg.click()

def renameZoomUser() :
    # Move && Press RightClick
    pg.moveTo(x=128, y=279)
    pg.click(button='right')
    # Move to Rename
    pg.moveTo(x=163, y=359)
    pg.click()
    pg.write('Reconnecting ...')
    pg.press('enter')

def alertChat() :
    # Press the Chat Button
    pg.moveTo(x=700, y=708)
    pg.click()
    # Send Message to Chat
    pg.write('Username is Reconnecting! .....')
    pg.press('enter')

# Give You Sometimes to Switch to Zoom -- 10 Sec --
time.sleep(10)
muteZoomAudio()
stopZoomVideo()
renameZoomUser()
alertChat()

# Alert when Complete
pg.alert('The Action is Done! Press Enter or Ok to Continue')
