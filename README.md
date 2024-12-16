This script is a productivity tool. It will show your Google Calendar tasks in full screen when you are not actively using your computer. 
Once you start using your computer again, it will minimize the calendar. This helps ensure you don’t forget important calendar tasks or events while taking a break from your device.

**Features**

Makes the Google Calendar window full screen when not in use.
Shrinks the Google Calendar pop-up when you start using it again.
Idle Monitoring: Monitors system idle time and fires the calendar when the threshold is reached.
Video Playback Detection: Prevents disruptions when playing a YouTube video in Chrome. (currently not working)
Custom Idle Time Threshold: Number of seconds the system should be idle before the calendar is shown. Default: 10 seconds.

**How It Works**

It uses the Windows API to monitor system idle time.
If the idle time is longer than the limit (usually 10 seconds) and no video is playing, then
It checks if Google Calendar is running.
If not, it opens Google Calendar and makes sure it is maximized and in focus.
When you interact with your computer (mouse/keyboard input), the script minimizes the calendar window.

**Use Case**

This script is ideal for those who:
Want a subtle reminder about upcoming tasks or events in between breaks.
Use Google Calendar to organize tasks and schedules.
Looking for a non-intrusive productivity tool to enhance task awareness.

**Requirements**

Google Calendar App:
To use this script, you will need to install Google Calendar as a separate application from a web browser (ideally a browser you don't use very often). For example:
Open Microsoft Edge.
Go to Google Calendar.
Tap the three dots in the top right corner.
Select Apps > Install Google Calendar to create a separate shortcut. Save the shortcut to somewhere like C:\Temp\Google Calendar.lnk. 

**Note**: Using a less used browser, like Microsoft Edge, ensures the script does not interfere with your primary browser activities.

**Installation**

Clone this repository or download the script file.
Ensure you have Python installed on your system.
Install the required Python packages using pip:
  pip install psutil pygetwindow
Update the GOOGLE_CALENDAR_PATH variable in the script to point to your Google Calendar shortcut's location (e.g., C:\Temp\Google Calendar.lnk).

**Configuration**

Idle Time Threshold:
Adjust the IDLE_THRESHOLD variable in the script to set the idle time (in seconds) before the calendar is triggered.
  IDLE_THRESHOLD = 10  # Default: 10 seconds

**Known Limitations**

_Browser Selection:_
The calendar shortcut must be installed from a browser that you don't frequently use (e.g., Microsoft Edge), as this script focuses on managing the application window.
If you use Chrome for the shortcut, the script may interfere with your browsing experience.

_Video Playback Detection:_
The script continues to open Calendar even when watching videos or reading without interacting with the screen.

**Contribution**

Contributions are welcome! If you have ideas for improvements, feel free to fork the repository and submit a pull request.
