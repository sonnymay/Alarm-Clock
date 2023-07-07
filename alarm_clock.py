import time
import winsound
import datetime

def input_time():
    try:
        alarm_hour = int(input("Enter the hour (24-hour format) you want to wake up at: "))
        alarm_minute = int(input("Enter the minute you want to wake up at: "))
        return alarm_hour, alarm_minute
    except ValueError:
        print("Please enter a valid time.")
        return input_time()

def alarm(alarm_hour, alarm_minute):
    while True:
        current_time = datetime.datetime.now()
        current_hour = current_time.hour
        current_minute = current_time.minute

        if current_hour == alarm_hour and current_minute == alarm_minute:
            print("Wake up!")
            # Beep for Windows - Frequency: 2500 Hz, Duration: 1 second.
            # You may need to use a different function for different OS
            for i in range(5):
                winsound.Beep(2500, 1000)
                time.sleep(1)
            return

        time.sleep(1)

if __name__ == "__main__":
    alarm_hour, alarm_minute = input_time()
    alarm(alarm_hour, alarm_minute)
