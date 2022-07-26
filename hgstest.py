import tkinter
from tkinter import BOTH, DISABLED, END, LEFT, NORMAL, Button, Entry, Frame, IntVar, Label, LabelFrame, Radiobutton, StringVar, Text, Tk, ttk
from tkinter import messagebox
from tracemalloc import start

def validation(name_str, name_end, entered_text, elm):
    msg = ''
   
    if name_str == 0:
        msg = f'{elm} is required!'
    if name_end == 0:
        msg = f'{elm} is required!'
    if entered_text == '':
        msg = f'{elm} is required!'        
    else:
        try:
            if int(name_str) <= 0:
                msg = 'entered value cannot be 0 or less'
            elif int(name_str) >= int(name_end):
                msg = 'Start cannot be greater than or equal to 0'
            elif int(name_end) <= 0 :
                msg = 'entered value cannot be 0 or less'
            elif len(entered_text) == int(name_end):
                msg = f'entered valid value {elm}'
            elif len(entered_text) > int(name_end):
                msg = 'enter valid value between start and end'           
            else:
                msg=f'Invalid entry {elm}'
        except Exception as ep:
            messagebox.showerror('message', ep)
    messagebox.showinfo('message', msg)
    

def btn_clicked():   
    validation(startt.get(), end.get(), etext.get(), etext.get())

def on_click_startt(event):
    startt.configure(state=NORMAL)
    startt.delete(0, END)
    startt.unbind('<Button-1>', on_click_id1)

def on_click_end(event):
    end.configure(state=NORMAL)
    end.delete(0, END)
    end.unbind('<Button-1>', on_click_id2)

def on_click_ttext(event):
    etext.configure(state=NORMAL)
    etext.delete(0, END)
    etext.unbind('<Button-1>', on_click_id3)

ws = Tk()
ws.title('Text Input')
ws.geometry('600x600')
ws.config(bg='#fff')

startt = [x for x in range(1, 5000)]
end = [x for x in range(1, 5000)]
entertext = StringVar()


Label(
    ws,
    text='_'*85,
    fg='#ccd065',
    bg='#fff',
).grid(row=2, columnspan=2, pady=(0, 20))

startt = Entry(
    ws,
    bg='#fff',
    font=('sans-serif', 15)
)
startt.grid(row=3, column=0, pady=(0, 10))

end = Entry(
    ws,
    bg='#fff',
    font=('sans-serif', 15),
)
end.grid(row=3, column=1, pady=(0, 10))

etext = Entry(
    ws,
    bg='#fff',
    font=('sans-serif', 15),
    width=43
)
etext.grid(row=4, columnspan=2, pady=(0, 10))

# adding placeholders
startt.insert(0, 'start')
startt.configure(state=DISABLED)
end.insert(0, 'end')
end.configure(state=DISABLED)
etext.insert(0, 'Enter Text')
etext.configure(state=DISABLED)

# binding placeholders
startt.bind('<Button-1>', on_click_startt)
end.bind('<Button-1>', on_click_end)
etext.bind('<Button-1>', on_click_ttext)

on_click_id1 = startt.bind('<Button-1>', on_click_startt)
on_click_id2 = end.bind('<Button-1>', on_click_end)
on_click_id3 = etext.bind('<Button-1>', on_click_ttext)

submit_btn = Button(
    ws,
    text='Submit',
    command= btn_clicked,  #ToDo
    font = ('sans-serif', 18),
    padx=40,
    pady=10,
)
submit_btn.grid(row=9, columnspan=2)

ws.mainloop()
