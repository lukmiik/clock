from tkinter import *
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
from time import strftime
from playsound import playsound
from threading import *


# Light and dark colors
light = "#fafafa"
dark = "#272727"
dark_sec_clr = "#FAF9F6"
light_sec_clr = "#272727"
hover_color = "#343434"
current_mode = dark
current_sec_clr = dark_sec_clr
root = Tk()
root.title("Clock tool")
root.geometry("300x400")
root.config(bg=dark)
p = PhotoImage(file="images/clock_icon.png")
root.iconphoto(False,p)
menu_fm_height=25

# Create menu
def close_toggle_menu():
    toggle_menu_fm.destroy()
    menu_btn.config(command=toggle_menu)

def switch_color_mode():
    global current_mode, current_sec_clr,color_mode_switch,color_mode_switch 
    global current_img,toggle_menu_fm,toggle_menu_clr,hover_color, time_label, play_pause_btn,reset_btn
    if current_mode == light: 
        current_mode = dark
        current_sec_clr = dark_sec_clr   
        current_img = dark_mode_img
        toggle_menu_clr = "#1a1a1a"
        hover_color = "#343434"
    else:
        current_mode = light
        current_sec_clr = light_sec_clr
        current_img = light_mode_img
        toggle_menu_clr = "#ededed" 
        hover_color = "#ffffff"
        
    color_mode_switch.config(image=current_img,  bg=toggle_menu_clr,activebackground= toggle_menu_clr)
    root.config(bg=current_mode)
    menu_fm.config(bg=current_mode)
    menu_btn.config(bg=current_mode, fg=current_sec_clr, 
        activebackground=current_mode, activeforeground=current_sec_clr)
    toggle_menu_fm.config(bg=toggle_menu_clr)
    clock_btn.config(bg=toggle_menu_clr, fg=current_sec_clr, 
        activebackground=toggle_menu_clr, activeforeground=current_sec_clr)
    alarm_btn.config(bg=toggle_menu_clr, fg=current_sec_clr, 
        activebackground=toggle_menu_clr, activeforeground=current_sec_clr)
    stopwatch_btn.config(bg=toggle_menu_clr, fg=current_sec_clr, 
        activebackground=toggle_menu_clr, activeforeground=current_sec_clr)
    timer_btn.config(bg=toggle_menu_clr, fg=current_sec_clr, 
        activebackground=toggle_menu_clr, activeforeground=current_sec_clr)
    if 'clock_frm' in globals() and clock_frm.winfo_exists():
        clock_frm.config(bg=hover_color)
        clock_label.config(bg=hover_color, fg=current_sec_clr)
    if 'alarm_frm' in globals() and alarm_frm.winfo_exists():
        alarm_frm.config(bg=hover_color)
        alarm_label.config(bg=hover_color, fg=current_sec_clr)
        hrs.config(bg=hover_color, fg=current_sec_clr,activebackground=hover_color, activeforeground=current_sec_clr)
        mins.config(bg=hover_color, fg=current_sec_clr,activebackground=hover_color, activeforeground=current_sec_clr)
        snd.config(bg=hover_color, fg=current_sec_clr,activebackground=hover_color, activeforeground=current_sec_clr)
        msg.config(bg=hover_color, fg=current_sec_clr)
        submit_btn.config(bg=hover_color, fg=current_sec_clr)
        msg_label.config(bg=hover_color, fg=current_sec_clr)
        sound_label.config(bg=hover_color, fg=current_sec_clr)
    if 'stopwatch_frm' in globals() and stopwatch_frm.winfo_exists():
        stopwatch_frm.config(bg=hover_color)
        stopwatch_label.config(bg=hover_color, fg=current_sec_clr)
        time_label.config(bg=hover_color, fg=current_sec_clr)
        play_pause_btn.config(bg=hover_color, activebackground=hover_color)
        reset_btn.config(bg=hover_color, activebackground=hover_color)
    if 'timer_frm' in globals() and timer_frm.winfo_exists():
        timer_frm.config(bg=hover_color)
        timer_time_label.config(bg=hover_color, fg=current_sec_clr)
        timer_label.config(bg=hover_color, fg=current_sec_clr)
        timer_hrs.config(bg=hover_color, fg=current_sec_clr,activebackground=hover_color, activeforeground=current_sec_clr)
        timer_mins.config(bg=hover_color, fg=current_sec_clr,activebackground=hover_color, activeforeground=current_sec_clr)
        timer_sec.config(bg=hover_color, fg=current_sec_clr,activebackground=hover_color, activeforeground=current_sec_clr)
        start_stop_btn.config(bg=hover_color, activebackground=hover_color)
        timer_reset_btn.config(bg=hover_color, activebackground=hover_color)
# Create color switch mode button
a = Image.open("images/dark_mode.png")
resize_img = a.resize((50, 40))
dark_mode_img = ImageTk.PhotoImage(resize_img)
b = Image.open("images/light_mode.png")
resize_img2 = b.resize((50, 40))
light_mode_img = ImageTk.PhotoImage(resize_img2)
current_img = dark_mode_img

def toggle_menu():
    # Color of the toggle menu frame
    global toggle_menu_clr,hover_color,toggle_menu_fm,clock_btn,alarm_btn,stopwatch_btn,timer_btn,color_mode_switch
    if current_mode == dark:
        toggle_menu_clr = "#1a1a1a" 
        hover_color = "#343434"
    elif current_mode == light:
        toggle_menu_clr = "#ededed" 
        hover_color = "#ffffff"

    # Button background when cursor hovering
    def on_enter(e):
        e.widget['background'] = hover_color 
    def on_leave(e):
        e.widget['background'] = toggle_menu_clr
    
    # Create toggle menu frame
    toggle_menu_fm = Frame(root, bg=toggle_menu_clr)
    toggle_menu_fm.grid_columnconfigure(0, weight=1)
    toggle_menu_height = root.winfo_height()-menu_fm_height
    window_width = root.winfo_width()
    if window_width >200:
        toggle_menu_width = 200
    else:
        toggle_menu_width = window_width - 10
    toggle_menu_fm.place(x=0, y=menu_fm_height, height=toggle_menu_height, width=toggle_menu_width)

    clock_btn = Button(toggle_menu_fm, text="Clock", bg=toggle_menu_clr, fg=current_sec_clr, 
        activebackground=toggle_menu_clr, activeforeground=current_sec_clr,bd=0, font=("BOLD",15), command=clock)
    clock_btn.grid(row=0,column=0, sticky="news")
    clock_btn.bind("<Enter>", on_enter)
    clock_btn.bind("<Leave>", on_leave)  

    alarm_btn = Button(toggle_menu_fm, text="Alarm", bg=toggle_menu_clr, fg=current_sec_clr, 
        activebackground=toggle_menu_clr, activeforeground=current_sec_clr,bd=0, font=("BOLD",15), command=alarm)
    alarm_btn.grid(row=1,column=0, sticky="news")
    alarm_btn.bind("<Enter>", on_enter)
    alarm_btn.bind("<Leave>", on_leave) 

    stopwatch_btn = Button(toggle_menu_fm, text="Stopwatch", bg=toggle_menu_clr, fg=current_sec_clr, 
        activebackground=toggle_menu_clr, activeforeground=current_sec_clr,bd=0, font=("BOLD",15), command=stopwatch)
    stopwatch_btn.grid(row=2,column=0, sticky="news")
    stopwatch_btn.bind("<Enter>", on_enter)
    stopwatch_btn.bind("<Leave>", on_leave)  

    timer_btn = Button(toggle_menu_fm, text="Timer", bg=toggle_menu_clr, fg=current_sec_clr, 
        activebackground=toggle_menu_clr, activeforeground=current_sec_clr,bd=0, font=("BOLD",15), command=timer)
    timer_btn.grid(row=3,column=0, sticky="news")
    timer_btn.bind("<Enter>", on_enter)
    timer_btn.bind("<Leave>", on_leave)  

    color_mode_switch = Button(toggle_menu_fm, image=current_img, bd=0, 
        bg=toggle_menu_clr,activebackground= toggle_menu_clr, command=switch_color_mode)
    color_mode_switch.grid(row=4, column=0, sticky="news")
    color_mode_switch.bind("<Enter>", on_enter)
    color_mode_switch.bind("<Leave>", on_leave)  

    menu_btn.config(command=close_toggle_menu)

# Menu frame
menu_fm = Frame(root, bg=current_mode)
menu_fm.pack(side=TOP, fill=X)
menu_fm.propagate(False)
menu_fm.configure(height=menu_fm_height)
menu_btn = Button(menu_fm, text="≡", bg=current_mode, fg=current_sec_clr, 
    activebackground=current_mode, activeforeground=current_sec_clr,bd=0, font=("BOLD",15), command=toggle_menu)
menu_btn.pack(anchor='w')

# Clock
def clock():
    global alarm_frm,clock_frm,clock_label
    if 'clock_frm'in globals() and clock_frm.winfo_exists():
        return
    def update_clock():
        time = strftime('%H:%M:%S %p')
        clock_label.config(text=time)
        clock_label.after(1000, update_clock)

    clock_frm=Frame(root, bg=hover_color)
    clock_frm.pack( padx=25,pady=25, ipadx=10,ipady=10)
    clock_label = Label(clock_frm, bg=hover_color, fg=current_sec_clr, font=("BOLD", 30) )
    clock_label.pack(expand=True)
    if 'toggle_menu_fm'in globals() and toggle_menu_fm.winfo_exists():
        close_toggle_menu()   
    update_clock()
    if 'alarm_frm' in globals() and alarm_frm.winfo_exists():
        alarm_frm.destroy()
    if 'stopwatch_frm' in globals() and stopwatch_frm.winfo_exists():
        stopwatch_frm.destroy()
    if 'timer_frm' in globals() and timer_frm.winfo_exists():
        timer_frm.destroy()

# Alarm
def alarm():
    global alarm_frm,alarm_label,hrs,mins,snd,msg,submit_btn,msg_label,sound_label
    if 'alarm_frm'in globals() and alarm_frm.winfo_exists():
        return
    def threading_submit_alarm():
        Thread(target=submit_alarm).start()
    def submit_alarm():
        alarm_time = f"{hour.get()}:{minute.get()}"
        while True:
            current_time = strftime("%H:%M")
            if current_time == alarm_time:
                sound_file = "ringtones/" +sound.get() + ".mp3"
                Thread(target=playsound, args=(sound_file,)).start()
                messagebox.showinfo("Alarm", msg.get() + "\n"+alarm_time)
                break
    
    alarm_frm = Frame(root,bg=hover_color)
    alarm_frm.pack( padx=25,pady=25, ipadx=200,ipady=150)
    alarm_label = Label(alarm_frm, text="ALARM",bg=hover_color, fg=current_sec_clr, font=("BOLD", 40) )
    alarm_label.place(relx=0.5, anchor=N)
    #entry hours
    hour = StringVar(alarm_frm)
    hours = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24'
        )
    hour.set(hours[0])
    hrs = OptionMenu(alarm_frm, hour, *hours)
    hrs.config(width=5, bg=hover_color, fg=current_sec_clr,activebackground=hover_color, activeforeground=current_sec_clr)
    hrs.place(x =40,y=73)
    #entry min
    minute = StringVar(alarm_frm)
    minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
            '08', '09', '10', '11', '12', '13', '14', '15',
            '16', '17', '18', '19', '20', '21', '22', '23',
            '24', '25', '26', '27', '28', '29', '30', '31',
            '32', '33', '34', '35', '36', '37', '38', '39',
            '40', '41', '42', '43', '44', '45', '46', '47',
            '48', '49', '50', '51', '52', '53', '54', '55',
            '56', '57', '58', '59', '60')
    minute.set(minutes[0]) 
    mins = OptionMenu(alarm_frm, minute, *minutes)
    mins.config(width=5, bg=hover_color, fg=current_sec_clr,activebackground=hover_color, activeforeground=current_sec_clr)
    mins.place(x = 130,y=73)
    #entry message
    msg_label = Label(alarm_frm, text="message",bg=hover_color, fg=current_sec_clr, font=("BOLD", 10) )
    msg_label.place(x = 31,y=124)
    msg = Entry(alarm_frm, width=18,bd=5,bg=hover_color, fg=current_sec_clr)
    msg.place(x = 97,y=123)  
    #entry sound
    sound = StringVar()
    sound_label = Label(alarm_frm, text="sound",bg=hover_color, fg=current_sec_clr, font=("BOLD", 10) )
    sound_label.place(x = 60,y=173)
    sounds = ('sound1', 'sound2', 'sound3')
    snd = OptionMenu(alarm_frm, sound, *sounds)
    snd.config(width=5, bg=hover_color, fg=current_sec_clr,activebackground=hover_color, activeforeground=current_sec_clr)
    snd.place(x=120,y=170)
    #submit button
    submit_btn = Button(alarm_frm, text='Submit',font=("BOLD", 13), width = 15,bg=hover_color, fg=current_sec_clr, command=threading_submit_alarm)
    submit_btn.place(relx=0.5, y =220, anchor=N)
    
    close_toggle_menu()
    if clock_frm.winfo_exists():
        clock_frm.destroy()
    if 'stopwatch_frm' in globals() and stopwatch_frm.winfo_exists():
        stopwatch_frm.destroy()
    if 'timer_frm' in globals() and timer_frm.winfo_exists():
        timer_frm.destroy()

# Stopwatch
play_img = PhotoImage(file = "images/play.png")
pause_img = PhotoImage(file="images/pause.png")
reset_img = PhotoImage(file="images/reset.png")

def stopwatch():
    global stopwatch_frm, stopwatch_label, sec, minu, hrs, start, time_label, play_pause_btn, reset_btn
    start = False
    sec ,minu,hrs= 0,0,0
    if 'stopwatch_frm'in globals() and stopwatch_frm.winfo_exists():
        return
    def play_stopwatch():
        play_pause_btn.config( image=pause_img,  bg=hover_color,activebackground= hover_color, command=pause_stopwatch)
        running()
    def pause_stopwatch():
        play_pause_btn.config( image=play_img, command=play_stopwatch)
        time_label.after_cancel(flag)
    def reset_stopwatch():
        global start
        if start == True:
            time_label.after_cancel(flag)
            global sec,minu,hrs
            sec = 0
            minu=0
            hrs=0          
            time_label.config(text="00:00:00")
            play_pause_btn.config( image=play_img, command=play_stopwatch)
            start = False

    def running():
        global sec, minu, hrs, start, flag
        start = True
        sec +=1
        if sec == 60:
            minu += 1
            sec = 0
        if minu == 60:
            hrs += 1
            minu = 0
        hours = f'{hrs}' if hrs > 9 else f'0{hrs}'
        minutes = f'{minu}' if minu> 9 else f'0{minu}'
        seconds = f'{sec}' if sec > 9 else f'0{sec}'
        time_label.config(text=hours + ':' + minutes+ ':' + seconds)
        flag = time_label.after(1000,running)
        
    stopwatch_frm = Frame(root,bg=hover_color)
    stopwatch_frm.pack( padx=25,pady=25, ipadx=200,ipady=100)
    stopwatch_label = Label(stopwatch_frm, text="STOPWATCH",bg=hover_color, fg=current_sec_clr, font=("BOLD", 25) )
    stopwatch_label.place(relx=0.5, anchor=N)
    time_label = Label(stopwatch_frm, text="00:00:00", bg=hover_color, fg=current_sec_clr, font=("BOLD", 40))
    time_label.place(relx=0.5,y=50, anchor=N)
    play_pause_btn = Button(stopwatch_frm, image=play_img, bd=0, 
        bg=hover_color,activebackground= hover_color, command=play_stopwatch)
    play_pause_btn.place(relx=0.25,y=120)
    reset_btn = Button(stopwatch_frm, image=reset_img, bd=0, 
        bg=hover_color,activebackground= hover_color, command=reset_stopwatch)
    reset_btn.place(relx=0.55,y=120)
    close_toggle_menu()
    if clock_frm.winfo_exists():
        clock_frm.destroy()
    if 'alarm_frm' in globals() and alarm_frm.winfo_exists():
        alarm_frm.destroy()
    if 'timer_frm' in globals() and timer_frm.winfo_exists():
        timer_frm.destroy()
    
# Timer
def timer():
    global timer_frm,timer_time_label,sec, minu, hrs, start, start_stop_btn
    global timer_sec,timer_mins,timer_hrs,timer_reset_btn,timer_label
    start = False
    sec ,minu,hrs= 0,0,0
    if 'timer_frm'in globals() and timer_frm.winfo_exists():
        return
    def start_timer():
        global sec, minu, hrs
        sec = int(second.get())
        minu=int(minute.get())
        hrs=int(hour.get())
        start_stop_btn.config(image=pause_img, command=pause_timer)
        running()
    def pause_timer():
        start_stop_btn.config( image=play_img, command=start_timer)
        timer_time_label.after_cancel(flag)
    def reset_timer():
        global start
        if start == True:
            timer_time_label.after_cancel(flag)
            global sec,minu,hrs
            sec = 0
            minu=0
            hrs=0          
            timer_time_label.config(text="00:00:00")
            start_stop_btn.config( image=play_img, command=start_timer)
            start = False
    def running():
        global sec, minu, hrs, start, flag
        start = True
        change = False
        if sec != 0:
            sec -=1
        if sec == 0:
            if hrs ==0 and minu==0 and sec==0:
                messagebox.showinfo("Timer", "TIMER ENDED")
                reset_timer()
                return            
            if minu>0:
                minu -= 1
                sec = 60
            else:
                hrs -= 1
                minu = 59
                sec=60
                change = True
        if change:
            hours = f'{hrs+1}' if hrs > 8 else f'0{hrs+1}' 
            seconds = '00'
            minutes='00'
        else:
            hours = f'{hrs}' if hrs > 9 else f'0{hrs}'   
            if sec==60:
                seconds = '00'
                minutes= f'{minu+1}' if minu> 8 else f'0{minu+1}'
            elif sec<60 and sec>9:
                seconds =f'{sec}' 
                minutes = f'{minu}' if minu> 9 else f'0{minu}'
            else:
                seconds=  f'0{sec}'
                minutes = f'{minu}' if minu> 9 else f'0{minu}'
        timer_time_label.config(text=hours + ':' + minutes+ ':' + seconds)
        flag = timer_time_label.after(1000,running)
    timer_frm = Frame(root,bg=hover_color)
    timer_frm.pack(padx=25,pady=25, ipadx=200,ipady=125)
    timer_label = Label(timer_frm, text="TIMER",bg=hover_color, fg=current_sec_clr, font=("BOLD", 30) )
    timer_label.place(relx=0.5, anchor=N)
    timer_time_label = Label(timer_frm, text="00:00:00", bg=hover_color, fg=current_sec_clr, font=("BOLD", 40))
    timer_time_label.place(relx=0.5, y=50,anchor=N)
    #hours
    hour = StringVar(timer_frm)
    hours = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24'
        )
    hour.set(hours[0])
    timer_hrs = OptionMenu(timer_frm, hour, *hours)
    timer_hrs.config(width=3, bg=hover_color, fg=current_sec_clr,activebackground=hover_color, activeforeground=current_sec_clr)
    timer_hrs.place(relx=0.1,y=125)
    #min
    minute = StringVar(timer_frm)
    minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
            '08', '09', '10', '11', '12', '13', '14', '15',
            '16', '17', '18', '19', '20', '21', '22', '23',
            '24', '25', '26', '27', '28', '29', '30', '31',
            '32', '33', '34', '35', '36', '37', '38', '39',
            '40', '41', '42', '43', '44', '45', '46', '47',
            '48', '49', '50', '51', '52', '53', '54', '55',
            '56', '57', '58', '59')
    minute.set(minutes[0]) 
    timer_mins = OptionMenu(timer_frm, minute, *minutes)
    timer_mins.config(width=3, bg=hover_color, fg=current_sec_clr,activebackground=hover_color, activeforeground=current_sec_clr)
    timer_mins.place(relx=0.38,y=125)
    #sec
    second = StringVar(timer_frm)
    seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
            '08', '09', '10', '11', '12', '13', '14', '15',
            '16', '17', '18', '19', '20', '21', '22', '23',
            '24', '25', '26', '27', '28', '29', '30', '31',
            '32', '33', '34', '35', '36', '37', '38', '39',
            '40', '41', '42', '43', '44', '45', '46', '47',
            '48', '49', '50', '51', '52', '53', '54', '55',
            '56', '57', '58', '59')
    second.set(seconds[0]) 
    timer_sec = OptionMenu(timer_frm, second, *seconds)
    timer_sec.config(width=3, bg=hover_color, fg=current_sec_clr,activebackground=hover_color, activeforeground=current_sec_clr)
    timer_sec.place(relx=0.66,y=125)
    # start stop reset
    start_stop_btn = Button(timer_frm, image=play_img, bd=0, 
        bg=hover_color,activebackground= hover_color, command=start_timer)
    start_stop_btn.place(relx=0.25,y=175)
    timer_reset_btn = Button(timer_frm, image=reset_img, bd=0, 
        bg=hover_color,activebackground= hover_color, command=reset_timer)
    timer_reset_btn.place(relx=0.55,y=175)
    close_toggle_menu()
    if 'alarm_frm' in globals() and alarm_frm.winfo_exists():
        alarm_frm.destroy()
    if 'stopwatch_frm' in globals() and stopwatch_frm.winfo_exists():
        stopwatch_frm.destroy()
    if clock_frm.winfo_exists():
        clock_frm.destroy()

clock()
root.resizable(False, False)
mainloop()