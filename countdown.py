import time
from datetime import datetime

# Label(window,text="Enter time in HH:MM:SS",font=('bold')).pack()
# Entry(window,textvariable = hour,width=30).pack()
# Entry(window,textvariable = minus,width=30).pack()
# Entry(window,textvariable = secon,width=30).pack()
 
# Checkbutton(text='Check for Music',onvalue=True,variable=check).pack()#creating checkbox
 
# Button(window,text="Set Countdown",command=countdown,bg='yellow').place(x=260,y=230)#create buttons   

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

print(current_time)

hours = int(input("hours"))
min = int(input("min"))
sec = int(input("sec"))

total_sec = 3600 * hours + min * 60 + sec 

while total_sec > 0:
    mins, secs = divmod(total_sec, 60)
    hrs, mins = divmod(mins, 60)


    timer = f"{hrs:02d}:{mins:02d}:{secs:02d}"

    print(timer, end="\r")
    time.sleep(1)

    total_sec -= 1

print("Times up")