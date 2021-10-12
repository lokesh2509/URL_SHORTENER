from tkinter import *
from ttkthemes import themed_tk as tk
import pyshorteners
import pyperclip

root = tk.ThemedTk()
root.get_themes()
root.set_theme("yaru")
root.resizable(0,0)
root.geometry("600x300")
root.title("URL SHORTENER - Lokesh Vyas")

def urlshort():
    short_url = url_paste.get()
    new_generated_url = pyshorteners.Shortener().tinyurl.short(short_url)
    url_copy.set(new_generated_url)

def copy():
    new_generated_url = url_copy.get()
    pyperclip.copy(new_generated_url)


l1 = Label(root, text="Url Shortener", font="arial 20 bold")
l1.pack()


url_paste = StringVar()
url_copy = StringVar()


url = Entry(root, width=70, textvariable=url_paste)
url.place(x=80, y=50)

btn_generate = Button(root, text="Generate URL", command=urlshort)
btn_generate.place(x=250, y=80)

url_generated = Entry(root, width=70, textvariable=url_copy)
url_generated.place(x=80, y=120)

btn_generate = Button(root, text="Copy URL", command=copy)
btn_generate.place(x=260, y=150)



root.mainloop()