'''
alarm clock should
    keep track of current time
    if it's on or off
    time it's set to

    have a method to set or change the current time and print it to the console

    when I import it, I want to print the time, call the change time method to change the time, and toggle the alarm off
'''

class Alarm_clock:

    def __init__(self, current_time, status, time_to_ring):
        self.current_time = current_time
        self.status = status
        self.ring = time_to_ring

    def change_current_time(self):
        self.change_time = input("What is the current time?")
        print(self.change_time)


