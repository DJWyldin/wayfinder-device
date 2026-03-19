import os
import time

LAST_SPOKEN = ""
LAST_TIME = 0
COOLDOWN = 2

def speak(text):
    global LAST_SPOKEN, LAST_TIME

    now = time.time()

    if text == LAST_SPOKEN and (now - LAST_TIME) < COOLDOWN:
        return

    print(f"[AUDIO]: {text}")
    os.system(f'espeak "{text}"')

    LAST_SPOKEN = text
    LAST_TIME = now