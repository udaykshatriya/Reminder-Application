import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Reminder activities
activities = [
    "Wake up",
    "Go to gym",
    "Breakfast",
    "Meetings",
    "Lunch",
    "Quick nap",
    "Go to library",
    "Dinner",
    "Go to sleep"
]

# Function to play sound
def play_sound():
    pygame.mixer.music.load("sound.wav")
    pygame.mixer.music.play()

# Function to check and remind
def check_reminder():
    # Get current day and time
    current_day = day_var.get()
    current_time = time_var.get()

    # Get current datetime
    now = datetime.now()
    selected_datetime = datetime.strptime(current_time, "%I:%M %p")

    # Adjust datetime to match selected day
    selected_datetime += timedelta(days=(current_day - now.weekday()))

    # Check if it's time for reminder
    if now.hour == selected_datetime.hour and now.minute == selected_datetime.minute:
        activity = activity_var.get()
        play_sound()
        print(f"Time to {activity}!")

# Create main window
root = tk.Tk()
root.title("Reminder Application")

# Day dropdown
day_label = ttk.Label(root, text="Select day:")
day_label.grid(row=0, column=0)
day_var = tk.IntVar()
day_dropdown = ttk.Combobox(root, textvariable=day_var, values=list(range(7)))
day_dropdown.grid(row=0, column=1)
day_dropdown.current(0)

# Time dropdown
time_label = ttk.Label(root, text="Select time:")
time_label.grid(row=1, column=0)
time_var = tk.StringVar()
time_dropdown = ttk.Combobox(root, textvariable=time_var, values=[f"{h:02d}:{m:02d} {a}" for a in ("AM", "PM") for h in range(1, 13) for m in range(0, 60, 15)])
time_dropdown.grid(row=1, column=1)
time_dropdown.current(0)

# Activity dropdown
activity_label = ttk.Label(root, text="Select activity:")
activity_label.grid(row=2, column=0)
activity_var = tk.StringVar()
activity_dropdown = ttk.Combobox(root, textvariable=activity_var, values=activities)
activity_dropdown.grid(row=2, column=1)
activity_dropdown.current(0)

# Button to set reminder
set_button = ttk.Button(root, text="Set Reminder", command=check_reminder)
set_button.grid(row=3, column=0, columnspan=2)

root.mainloop()
