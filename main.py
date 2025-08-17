import pyautogui
import pyperclip
import time
from openai import OpenAI
import os
import keyboard
 
time.sleep(3)
pyautogui.moveTo(1371, 1170, duration=0.5)
pyautogui.click()

def final(text):
    client = OpenAI(
    base_url="https://models.github.ai/inference",
    api_key="api_key_here",  #enter your api key here
)

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are ei and based on the previous messages you have to act like ei and reply chats.",
            },
            {
                "role": "user",
                "content": text,
            }
        ],
        model="openai/gpt-4o",
        temperature=1,
        max_tokens=4096,
        top_p=1
)
    return response.choices[0].message.content

while True:
    if keyboard.is_pressed("esc"):
        break
    try:
        pyautogui.moveTo(662, 166, duration=0.5)
        pyautogui.dragTo(668, 1043, duration=1.0, button='left')

        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.5)  

        copied_text = pyperclip.paste()
        message=final(copied_text)
        
        pyperclip.copy(message)
        time.sleep(3)
        pyautogui.moveTo(887, 1086, duration=0.5)
        pyautogui.click()
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')

        time.sleep(5)
    except Exception as e:
        print("Error occurred:", e)
        time.sleep(5)
