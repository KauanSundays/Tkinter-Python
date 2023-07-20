import tkinter as tk
from tkinter import ttk

# Create a Window for app
window = tk.Tk()

def button_func():
    print('pressed')

window.title('Window and widgets') #titulo
window.geometry('800x500') #largura do app padrao

#label, title
label = ttk.Label(master = window, text= 'This is a test')
label.pack()

#Create the widgets
text = tk.Text(master = window)#textbox
text.pack() #conteudo em variavel

#ttk entry = input
entry = ttk.Entry(master = window)
entry.pack()

#label, title
exercise_label = ttk.Label(master = window, text= 'My label')
exercise_label.pack()


#ttk button
button = ttk.Button(master = window, text= 'A button', command= button_func)
button.pack()


# run the app
window.mainloop()