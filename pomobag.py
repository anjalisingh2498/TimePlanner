import time
import threading
import tkinter as tk
from tkinter import ttk,PhotoImage
class PomodoroTimer:
      def __init__(self):
          self.root= tk.Tk()
          self.root.geometry("505x421")
          self.root.configure(bg='white')
          self.root.title("pomodoro timer")
          self.root.tk.call('wm','iconphoto',self.root._w, PhotoImage(file="pomodoro.png"))
          self.root['bg'] = 'white'
          # self.photo=PhotoImage(file="pomodoro.png")
          # self.label=ttk.Label(self.screen,image=self.photo)
          # self.label.pack()
          # self.label=ttk.Label(self.root,image=self.photo)
          # self.label.place(x=0,y=0,relwidth=1,relheight=1)




          self.s=ttk.Style()
          self.s.configure("TNotebook.Tab",font=("Ubuntu",16),bg="white")
          self.s.configure("TButton", font=("Ubuntu", 16),bg="white")
          self.tabs=ttk.Notebook(self.root)
          self.tabs.pack(fill="both",pady=10,expand=True)
          self.tab1=tk.Frame(self.tabs,width=100,height=400,bg="white")
          self.tab2 = tk.Frame(self.tabs, width=100, height=400,bg="white")
          self.tab3 = tk.Frame(self.tabs, width=100, height=400,bg="white")
          self.pomodoro_timer_label=ttk.Label(self.tab1,background='white',foreground='cadetblue',text="25:00",font=("Ubuntu",100),padding=20)
          self.pomodoro_timer_label.pack(pady=60)
          self.short_break_timer_label = ttk.Label(self.tab2,background='white',foreground='cadetblue',text="05:00", font=("Ubuntu", 100))
          self.short_break_timer_label.pack(pady=60)
          self.long_break_timer_label = ttk.Label(self.tab3,background='white',foreground='cadetblue', text="15:00", font=("Ubuntu", 100))
          self.long_break_timer_label.pack(pady=60)

          self.tabs.add(self.tab1,text="pomodoro")
          self.tabs.add(self.tab2, text="short break")
          self.tabs.add(self.tab3, text="long break")

          self.frame = tk.Frame(self.root, width=600, height=400,background="white",highlightthickness=2,highlightbackground='white')
          self.frame.pack()
          self.img = PhotoImage(file="pomodoro.png")

          label = tk.Label(self.frame, image=self.img)
          label.pack()

          self.grid_layout=tk.Frame(self.root,highlightbackground="white", highlightthickness=2,background='white')
          self.grid_layout.pack(pady=10)
          self.start_button=tk.Button(self.grid_layout, text="start",command=self.start_timer_thread,background="cadetblue",foreground='white',font=('Helvetica 15 bold'))
          self.start_button.grid(row=0,column=0,ipadx=60,padx=90)


          self.skip_button=tk.Button(self.grid_layout,text="skip",command=self.skip_clock,background='cadetblue',foreground='white',font=('Helvetica 15 bold'))
          self.skip_button.grid(row=0, column=1,ipadx=60,padx=90)


          self.reset_button = tk.Button(self.grid_layout, text="Reset", command=self.reset_clock,background='cadetblue',foreground='white',font=('Helvetica 15 bold'))
          self.reset_button.grid(row=0, column=2,ipadx=60,padx=90)

          self.skip_button = tk.Button(self.grid_layout, text="skip", command=self.skip_clock, background='cadetblue',foreground='white', font=('Helvetica 15 bold'))
          self.skip_button.grid(row=0, column=1, ipadx=60, padx=90)



          self.pomodoro_counter_label=ttk.Label(self.grid_layout,text="Pomodoros:0", font=("Ubuntu",16),background="white")
          self.pomodoro_counter_label.grid(row=1,column=0,columnspan=3,pady=10)

          self.pomodoros = 0
          self.skipped = False
          self.stopped = False
          self.running = False



          self.root.mainloop()

      def start_timer_thread(self):
          if not self.running:

           t=threading.Thread(target=self.start_timer)
           t.start()
           self.running=True
      def start_timer(self):
          self.stopped=False
          self.skipped=False
          timer_id=self.tabs.index(self.tabs.select())+1
          if timer_id==1:
              full_seconds=60*25
              #full_seconds=5

              while full_seconds>0 and not self.stopped:
                minutes,seconds=divmod(full_seconds, 60)
                self.pomodoro_timer_label.configure(text=f"{minutes:02d}:{seconds:02d}")
                self.root.update()
                time.sleep(1)
                full_seconds-=1
              if not self.stopped or self.skipped:
                  self.pomodoros+=1
                  self.pomodoro_counter_label.config(text=f"Pomodoros:{self.pomodoros}")
                  if self.pomodoros %4 ==0:
                      self.tabs.select(2)
                      self.start_timer()
                  else:
                      self.tabs.select(1)
                  self.start_timer()
          elif timer_id==2:
              full_seconds=60*5
              full_seconds=5


              while full_seconds>0 and not self.stopped:
                minutes,seconds=divmod(full_seconds, 60)
                self.short_break_timer_label.configure(text=f"{minutes:02d}:{seconds:02d}")
                self.root.update()
                time.sleep(1)
                full_seconds-=1
              if not self.stopped or self.skipped:
                  self.tabs.select(0)
                  self.start_timer()
          elif timer_id==3:
              full_seconds=60*15

              while full_seconds>0 and not self.stopped:
                minutes,seconds=divmod(full_seconds, 60)
                self.long_break_timer_label.configure(text=f"{minutes:02d}:{seconds:02d}")
                self.root.update()
                time.sleep(1)
                full_seconds-=1
              if not self.stopped or self.skipped:
                  self.tabs.select(0)
                  self.start_timer()
          else:
              print("inavalid id")




      def reset_clock(self):
          self.stopped=True
          self.skipped=False
          self.pomodoros=0
          self.pomodoro_timer_label.config(text="25:00")
          self.short_break_timer_label.config(text="05:00")
          self.long_break_timer_label.config(text="15:00")
          self.pomodoro_counter_label.config(text="Pomodoros:0")
          self.running=False
      def skip_clock(self):
          current_tab=self.tabs.index(self.tabs.select())
          if current_tab==0:
              self.pomodoro_timer_label.config(text="25:00")
          elif current_tab==1:
              self.short_break_timer_label.config(text="05:00")
          elif current_tab==2:
             self.long_break_timer_label.config(text="15:00")
          self.stopped=True
          self.skipped=True


PomodoroTimer()