import tkinter as tk
from tkinter import ttk

# Create a Window for app
window = tk.Tk()


window.title('Window and widgets') #titulo
window.geometry('800x500') #largura do app padrao

#label, title
label = ttk.Label(master = window, text= 'This is a test')
label.pack()

#Create the widgets
text = tk.Text(master = window)#textbox
text.pack() #conteudo em variavel


# run the app
window.mainloop()