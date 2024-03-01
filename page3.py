from tkinter import *
import datetime
import time
#from playsound import playsound
from threading import *
from tkinter import messagebox
from PIL import ImageTk, Image

ws = Tk()
ws.geometry('1200x500')
ws.title('timer')
ws['bg']='white'

f = ("Times bold", 14)

Label(ws,text="   Set Timer",
    background='white',
    foreground='dark slate gray',
    font=('Times 50 bold italic')).grid(column=1,row=0,sticky=N)
img = ImageTk.PhotoImage(Image.open("timerr.png"))
label = Label(ws, image = img)
label.grid(column=0,row=1,sticky=W)

frame = Frame(ws,bg='white')
frame.grid(column=1,row=1,sticky='W',padx=200)

hour1=StringVar()
minute1=StringVar()
second1=StringVar()
  
# setting the default value as 0
hour1.set("00")
minute1.set("00")
second1.set("00")

# Use of Entry class to take input from the user
hourEntry= Entry(frame, width=3, font=("Arial",18,""),
                 textvariable=hour1)
hourEntry.grid(column=1,row=1)
 
minuteEntry= Entry(frame, width=3, font=("Arial",18,""),
                   textvariable=minute1)
minuteEntry.grid(column=2,row=1)
  
secondEntry= Entry(frame, width=3, font=("Arial",18,""),
                   textvariable=second1)
secondEntry.grid(column=3,row=1)
  

def submit():
    try:
        # the input provided by the user is
        # stored in here :temp
        temp = int(hour1.get())*3600 + int(minute1.get())*60 + int(second1.get())
    except:
        print("Please input the right value")
    while temp >-1:
         
        # divmod(firstvalue = temp//60, secondvalue = temp%60)
        mins,secs = divmod(temp,60)
  
        # Converting the input entered in mins or secs to hours,
        # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
        # 50min: 0sec)
        hours=0
        if mins >60:
             
            # divmod(firstvalue = temp//60, secondvalue
            # = temp%60)
            hours, mins = divmod(mins, 60)
         
        # using format () method to store the value up to
        # two decimal places
        hour1.set("{0:2d}".format(hours))
        minute1.set("{0:2d}".format(mins))
        second1.set("{0:2d}".format(secs))
  
        # updating the GUI window after decrementing the
        # temp value every time
        ws.update()
        time.sleep(1)
  
        # when temp value = 0; then a messagebox pop's up
        # with a message:"Time's up"
        # if (temp == 0):
        #     playsound('mixkit-fast-rocket-whoosh-1714.wav')
        #     messagebox.showinfo("Time Countdown", "Time's up ")
        #
        # after every one sec the value of temp will be decremented
        # by one
        # temp -= 1
 
# button widget
btn = Button(frame, text='Set Time Countdown', bd='2',
             command= submit,bg="cadet blue",fg="white",font='Times',).grid(column=4,row=1)

def nextPage1():
    ws.destroy()
    import page4

def nextPage():
    ws.destroy()
    import page1

def prevPage():
    ws.destroy()
    import page2



Button(
    ws, 
    text="Alarm",
    font='Times',
    command=prevPage,
    background='cadet blue',
foreground='white'
    ).grid(column=0,row=2)

Button(
    ws, 
    text="Main Page",
    font = 'Times',
    command=nextPage,
    background='cadet blue',
foreground='white'
    ).grid(column=1,row=2)
Button(
    ws, 
    text="Stopwatch",
    font='Times',
    command=nextPage1,
    background='cadet blue',
    foreground='white'
    ).grid(column=2,row=2)

ws.mainloop()