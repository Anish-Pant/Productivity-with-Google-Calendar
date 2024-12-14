import time
import psutil
import pygetwindow as gw
import subprocess
from pynput import mouse, keyboard

# Path to Google Calendar shortcut
GOOGLE_CALENDAR_PATH = r"C:\Users\Nix\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Chrome Apps\Google Calendar.lnk"

# Idle time threshold
IDLE_THRESHOLD = 30  # in seconds

# Track last activity time
last_activity_time = time.time()

def on_activity():
    """Update last activity time."""
    global last_activity_time
    last_activity_time = time.time()

def monitor_activity():
    """Monitor mouse and keyboard activity."""
    with mouse.Listener(on_move=on_activity, on_click=on_activity, on_scroll=on_activity) as mouse_listener:
        with keyboard.Listener(on_press=on_activity) as keyboard_listener:
            mouse_listener.join()
            keyboard_listener.join()

def is_video_playing():
    """Check if a video is playing in Chrome."""
    for proc in psutil.process_iter(['name', 'cmdline']):
        try:
            if proc.info['name'] == 'chrome.exe' and 'youtube' in ' '.join(proc.info['cmdline']).lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return False

def open_google_calendar():
    """Open Google Calendar."""
    subprocess.Popen(['explorer', GOOGLE_CALENDAR_PATH])

def is_google_calendar_running():
    """Check if Google Calendar is running."""
    for window in gw.getWindowsWithTitle("Google Calendar"):
        if "Google Calendar" in window.title:
            return True
    return False

def set_google_calendar_fullscreen():
    """Set Google Calendar to fullscreen."""
    for window in gw.getWindowsWithTitle("Google Calendar"):
        if "Google Calendar" in window.title:
            if window.isMinimized:
                window.restore()  # Restore if minimized
            if not window.isMaximized:
                window.maximize()  # Maximize if not already maximized
            print("Google Calendar is now fullscreen.")
            return True
    return False

# Main loop
while True:
    current_time = time.time()
    idle_time = current_time - last_activity_time

    if idle_time > IDLE_THRESHOLD:  # Check idle threshold
        if not is_video_playing():
            print("System is idle, and no video is playing.")
            if not is_google_calendar_running():
                print("Launching Google Calendar...")
                open_google_calendar()
                time.sleep(5)  # Allow time for the app to launch
            print("Ensuring Google Calendar is full screen...")
            if not set_google_calendar_fullscreen():
                print("Failed to maximize Google Calendar.")
    time.sleep(1)  # Check every second
