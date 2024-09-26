import time
import datetime
import pygame
import os

def set_alarm(alarm_time):
    print(f"Your set time is {alarm_time}:")
    pygame.mixer.init()
    sound_file = "for.mp3"
    
    # Check if the sound file exists
    if not os.path.exists(sound_file):
        print(f"Sound file {sound_file} does not exist.")
        return

    is_running = True
    
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        
        if current_time == alarm_time:
            print("WAKE UP!")
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            is_running = False
            
        time.sleep(1)

if __name__ == "__main__":
    while True:
        try:
            alarm_time = input("Enter time in format HH:MM:SS: ")
            # Validate the input time format
            datetime.datetime.strptime(alarm_time, "%H:%M:%S")
            break  # Exit the loop if the input is valid
        except ValueError:
            print("Incorrect format. Please enter time in HH:MM:SS format.")
    
    set_alarm(alarm_time)
