import tkinter as tk


def set_timer():
    previous_text = text.get()
    window.after(5000, delete_text, previous_text)


def delete_text(previous_text):
    current_text = text.get()

    if len(previous_text) == len(current_text):
        text.delete(0, tk.END)

    set_timer()


window = tk.Tk()
window.title("Disappearing Text")
window.minsize(width=500, height=200)

label = tk.Label(text="Type here", font=("Arial", 24, "bold"))
label.pack()

text = tk.Entry(width=100)
text.focus()
text.pack()
set_timer()

window.mainloop()
