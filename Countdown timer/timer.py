import time # usage of time module with sleep function
from playsound import playsound # learned about this amazing module 
# also learned about pyobj which lets python talk with macOS


count = int(input("ENTER TIME ----> "))
print("\n")

while count > 0: # this is not the stopping condition but more professionally its the running condition
    print(f"{count}\n")
    count -=1
    time.sleep(1) 


print("\n\------- TIMER ENDED -------/")
playsound("/Users/enma/Documents/Code/Python mini projects/Countdown timer/alarm.mp3")
playsound("/Users/enma/Documents/Code/Python mini projects/Countdown timer/alarm.mp3")
