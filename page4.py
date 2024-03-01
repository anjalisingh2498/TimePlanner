import tkinter as Tkinter
from datetime import datetime
from tkinter import *
import time
# from playsound import playsound
from threading import *
from tkinter import messagebox
from PIL import ImageTk, Image

ws = Tk()
ws.geometry('1300x500')
ws.title('Clepsydra-timer')
ws['bg']='white'

f = ("Times bold", 14)
Label(ws,text="Countdown",
    background='white',
    foreground='dark slate gray',
    font=('Times 50 bold italic')).grid(column=1,row=0,sticky=N)

img = ImageTk.PhotoImage(Image.open("timerr.png"))
label = Label(ws, image = img)
label.grid(column=0,row=1,sticky=W,pady=20)

frame = Frame(ws,bg='white')
frame.grid(column=1,row=1,sticky='W',padx=200)

counter = 66600
running = False
def counter_label(label):
    def count():
        if running:
            global counter
   
            # To manage the initial delay.
            if counter==66600:            
                display="Starting..."
            else:
                tt = datetime.fromtimestamp(counter)
                string = tt.strftime("%H:%M:%S")
                display=string
   
            label['text']=display   # Or label.config(text=display)
   
            # label.after(arg1, arg2) delays by 
            # first argument given in milliseconds
            # and then calls the function given as second argument.
            # Generally like here we need to call the 
            # function in which it is present repeatedly.
            # Delays by 1000ms=1 seconds and call count again.
            label.after(1000, count) 
            counter += 1
   
    # Triggering the start of the counter.
    count()     
   
# start function of the stopwatch
def Start(label):
    global running
    running=True
    counter_label(label)
    start['state']='disabled'
    stop['state']='normal'
    reset['state']='normal'
   
# Stop function of the stopwatch
def Stop():
    global running
    start['state']='normal'
    stop['state']='disabled'
    reset['state']='normal'
    running = False
   
# Reset function of the stopwatch
def Reset(label):
    global counter
    counter=66600
   
    # If rest is pressed after pressing stop.
    if running==False:      
        reset['state']='disabled'
        label['text']='Welcome!'
   
    # If reset is pressed while the stopwatch is running.
    else:               
        label['text']='Starting...'
   

   
# Fixing the window size.
label = Tkinter.Label(frame, text="Welcome!", bg="white",fg='cadet blue', font="Times 30 bold")
label.grid(row=0,column=0,padx=20)
start = Tkinter.Button(frame, font='Times',text='Start', width=5,height=2,bg="cadet blue",fg="white", command=lambda:Start(label))
stop = Tkinter.Button(frame,font='Times', text='Stop',width=5,height=2,bg="cadet blue",fg="white",state='disabled', command=Stop)
reset = Tkinter.Button(frame, font='Times',text='Reset',width=5,height=2,bg="cadet blue",fg="white", state='disabled', command=lambda:Reset(label))
frame.grid(row=1,column=1)
start.grid(row=0,column=1)
stop.grid(row=0,column=2)
reset.grid(row=0,column=3)

def nextPage1():
    ws.destroy()
    import page3

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
    foreground='white',
    height=2, width=9
    ).grid(column=0,row=2)

Button(
    ws, 
    text="Clepsydra",
    font = 'Times',
    command=nextPage,
    background='cadet blue',
    foreground='white',
    height=2, width=9
    ).grid(column=1,row=2)
Button(
    ws, 
    text=" Timer",
    font='Times',
    command=nextPage1,
    background='cadet blue',
    foreground='white',
    height=2, width=9
    ).grid(column=2,row=2)

ws.mainloop()