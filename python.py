import ctypes
import subprocess
import pygetwindow as gw
import psutil
import time

# Path to Google Calendar shortcut
GOOGLE_CALENDAR_PATH = r"C:\Temp\Google Calendar.lnk"

# Idle time threshold (in seconds)
IDLE_THRESHOLD = 10

# Function to get the system idle time
def get_idle_time():
    """Get the system idle time in seconds."""
    class LASTINPUTINFO(ctypes.Structure):
        _fields_ = [("cbSize", ctypes.c_uint), ("dwTime", ctypes.c_uint)]

    lii = LASTINPUTINFO()
    lii.cbSize = ctypes.sizeof(LASTINPUTINFO)
    ctypes.windll.user32.GetLastInputInfo(ctypes.byref(lii))
    millis = ctypes.windll.kernel32.GetTickCount() - lii.dwTime
    return millis / 1000.0  # Convert to seconds

# Function to open Google Calendar
def open_google_calendar():
    """Open Google Calendar."""
    subprocess.Popen(['explorer', GOOGLE_CALENDAR_PATH])

# Function to check if Google Calendar is running
def is_google_calendar_running():
    """Check if Google Calendar is running."""
    for window in gw.getWindowsWithTitle("Google Calendar"):
        if "Google Calendar" in window.title:
            return True
    return False

# Function to set Google Calendar to fullscreen
def set_google_calendar_fullscreen():
    """Set Google Calendar to fullscreen."""
    for window in gw.getWindowsWithTitle("Google Calendar"):
        if "Google Calendar" in window.title:
            if window.isMinimized:
                window.restore()  # Restore if minimized
            if not window.isMaximized:
                window.maximize()  # Maximize if not already maximized
            return True
    return False

# Function to minimize Google Calendar
def minimize_google_calendar():
    """Minimize Google Calendar."""
    for window in gw.getWindowsWithTitle("Google Calendar"):
        if "Google Calendar" in window.title:
            if not window.isMinimized:
                window.minimize()  # Minimize the window
            return True
    return False

# Function to check if a video is playing in Chrome
def is_video_playing():
    """Check if a video is playing in Chrome."""
    for proc in psutil.process_iter(['name', 'cmdline']):
        try:
            if proc.info['name'] == 'chrome.exe' and 'youtube' in ' '.join(proc.info['cmdline']).lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return False

# Main loop
while True:
    idle_time = get_idle_time()

    if idle_time > IDLE_THRESHOLD:  # System is idle
        if not is_video_playing():  # Check if a video is playing
            print("System is idle, and no video is playing.")
            if not is_google_calendar_running():
                print("Launching Google Calendar...")
                open_google_calendar()
                time.sleep(5)  # Allow time for the app to launch
            print("Ensuring Google Calendar is fullscreen...")
            if not set_google_calendar_fullscreen():
                print("Failed to maximize Google Calendar.")
    else:  # System is active
        if is_google_calendar_running():
            print("System is active. Google Calendar will be minimized...")
            minimize_google_calendar()

    time.sleep(1)  # Check every second
