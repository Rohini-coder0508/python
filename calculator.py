import tkinter as tk
from tkinter import ttk 

root = tk.Tk()

win_width = 300
win_height = 350

root.geometry(f"{win_width}x{win_height}+200+200")
root.title("Calculator")
root.resizable(False, False)

input_value = tk.StringVar()

def get_frame():
    frame = ttk.Frame(root, width=win_width)
    frame["borderwidth"] = 5
    frame["padding"] = 2
    frame["relief"] = "sunken"

    return frame

def get_input_area():
    input_frame = get_frame()
    
    text_entry = tk.Entry(input_frame, width=win_width, 
    justify=tk.RIGHT, font="CALIBRI 30", bg="black", fg="white",
    highlightthickness=0, bd=0,
     textvariable=input_value, )
    text_entry.focus()
    text_entry.pack(ipadx=5, ipady=5)
    
    return input_frame

def get_button(parent_frame, text, command):
    button = tk.Button(parent_frame, 
    text=text, font="Calibri 18", command=command)
    return button

def button_click(btn_value):
    input_value.set(f"{input_value.get()}{btn_value}")

def get_buttons_frame():
    button_frame = get_frame()

    button_frame.columnconfigure(0, weight=1)
    button_frame.columnconfigure(1, weight=1)
    button_frame.columnconfigure(2, weight=1)
    button_frame.columnconfigure(3, weight=1)
    button_frame.rowconfigure(0, weight=1)
    button_frame.rowconfigure(1, weight=1)
    button_frame.rowconfigure(2, weight=1)
    button_frame.rowconfigure(3, weight=1)
    button_frame.rowconfigure(4, weight=1)


    get_button(button_frame, "Clear", command=lambda: input_value.set("")).grid(
        column=0, row=0, columnspan=3, sticky=tk.NSEW)
    get_button(button_frame, "/", command=lambda: button_click("/")).grid(
        column=3, row=0, sticky=tk.NSEW)
    get_button(button_frame, "7", command=lambda: button_click("7")).grid(
        column=0, row=1, sticky=tk.NSEW)
    get_button(button_frame, "8", command=lambda: button_click("8")).grid(
        column=1, row=1, sticky=tk.NSEW)
    get_button(button_frame, "9", command=lambda: button_click("9")).grid(
        column=2, row=1, sticky=tk.NSEW)
    get_button(button_frame, "*", command=lambda: button_click("*")).grid(
        column=3, row=1, sticky=tk.NSEW)
    get_button(button_frame, "4", command=lambda: button_click("4")).grid(
        column=0, row=2, sticky=tk.NSEW)
    get_button(button_frame, "5", command=lambda: button_click("5")).grid(
        column=1, row=2, sticky=tk.NSEW)
    get_button(button_frame, "6", command=lambda: button_click("6")).grid(
        column=2, row=2, sticky=tk.NSEW)
    get_button(button_frame, "-", command=lambda: button_click("-")).grid(
        column=3, row=2, sticky=tk.NSEW)
    get_button(button_frame, "1", command=lambda: button_click("1")).grid(
        column=0, row=3, sticky=tk.NSEW)
    get_button(button_frame, "2", command=lambda: button_click("2")).grid(
        column=1, row=3, sticky=tk.NSEW)
    get_button(button_frame, "3", command=lambda: button_click("3")).grid(
        column=2, row=3, sticky=tk.NSEW)
    get_button(button_frame, "+", command=lambda: button_click("+")).grid(
        column=3, row=3, sticky=tk.NSEW)
    get_button(button_frame, "0", command=lambda: button_click("0")).grid(
        column=0, row=4, columnspan=3, sticky=tk.NSEW)
    get_button(button_frame, ".", command=lambda: button_click(".")).grid(
        column=2, row=4, sticky=tk.NSEW)
    get_button(button_frame, "=", command=lambda: input_value.set(eval(input_value.get()))).grid(
        column=3, row=4, sticky=tk.NSEW)
    



    return button_frame

def create_calculator():
    input_frame = get_input_area()
    input_frame.pack(padx=5, pady=5)

    button_frame = get_buttons_frame()
    button_frame.pack(padx=5, fill=tk.BOTH, expand=True)


if __name__ == "__main__":
    create_calculator()
    root.mainloop()