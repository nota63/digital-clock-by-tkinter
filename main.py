from tkinter import *
import datetime
import random

def date_time():
    time = datetime.datetime.now()
    hr = time.strftime('%I')
    mi = time.strftime('%M')
    sec = time.strftime('%S')
    am = time.strftime('%p')
    date = time.strftime("%d")
    month = time.strftime("%m")
    year = time.strftime("%Y")
    day = time.strftime("%A")

    lab_hr.config(text=hr)
    lab_min.config(text=mi)
    lab_sec.config(text=sec)
    lab_am.config(text=am)
    lab_date.config(text=date)
    lab_month.config(text=month)
    lab_year.config(text=year)
    lab_day.config(text=day)

    # Update every 200 milliseconds
    lab_hr.after(200, date_time)

def update_color():
    # Change colors dynamically
    new_color = random.choice(colors)
    clock.config(bg=new_color)
    for widget in clock.winfo_children():
        widget.config(bg=new_color, fg=random.choice(colors))

    # Re-schedule color update
    clock.after(5000, update_color)

def animate_clock():
    global alpha
    clock.update()
    clock.attributes('-alpha', alpha)
    alpha += 0.01
    if alpha < 1:
        clock.after(10, animate_clock)
    else:
        # Start date_time function after animation
        date_time()

clock = Tk()
clock.title("Digital Clock")
clock.geometry('1000x500')
alpha = 0  # Initial transparency

colors = ['red', 'blue', 'green', 'orange', 'purple', 'cyan', 'magenta', 'yellow']

# Call update_color to start color changing
clock.after(0, update_color)

# Create labels for time
time_labels = ['Hour', 'Min.', 'Sec.', 'AM/PM', 'Date', 'Month', 'Year', 'Day']
label_pos = [(20, 50), (250, 50), (480, 50), (710, 50), (20, 220), (250, 220), (480, 220), (710, 220)]

for i, (label_text, (x, y)) in enumerate(zip(time_labels, label_pos)):
    label = Label(clock, text=label_text, font=('Times New Roman', 20, "bold"), bg='white', fg='black')
    label.place(x=x, y=y, height=40, width=200)
    if i < 4:
        label.config(font=('Times New Roman', 20, "bold"), bg='white', fg='black')
    else:
        label.config(font=('Times New Roman', 20, "bold"), bg='white', fg='black')

# Create labels for time values
lab_hr = Label(clock, text="00", font=('Times New Roman', 60, "bold"), bg='white', fg='black')
lab_hr.place(x=20, y=100, height=110, width=200)
lab_min = Label(clock, text="00", font=('Times New Roman', 60, "bold"), bg='white', fg='black')
lab_min.place(x=250, y=100, height=110, width=200)
lab_sec = Label(clock, text="00", font=('Times New Roman', 60, "bold"), bg='white', fg='black')
lab_sec.place(x=480, y=100, height=110, width=200)
lab_am = Label(clock, text="00", font=('Times New Roman', 50, "bold"), bg='white', fg='black')
lab_am.place(x=710, y=100, height=110, width=200)
lab_date = Label(clock, text="00", font=('Times New Roman', 60, "bold"), bg='white', fg='black')
lab_date.place(x=20, y=270, height=110, width=200)
lab_month = Label(clock, text="00", font=('Times New Roman', 60, "bold"), bg='white', fg='black')
lab_month.place(x=250, y=270, height=110, width=200)
lab_year = Label(clock, text="0000", font=('Times New Roman', 60, "bold"), bg='white', fg='black')
lab_year.place(x=480, y=270, height=110, width=200)
lab_day = Label(clock, text="Day", font=('Times New Roman', 30, "bold"), bg='white', fg='black')
lab_day.place(x=710, y=270, height=110, width=200)

# Call animate_clock function to start clock animation
clock.after(1000, animate_clock)

# Run the Tkinter event loop
clock.mainloop()
