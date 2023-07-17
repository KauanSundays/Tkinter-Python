import tkinter as tk

# Create a Window for app
window = tk.Tk()


window.title('Window and widgets') #titulo
window.geometry('800x500') #largura do app padrao

#Create the widgets
text = tk.Text(master = window)#textbox
text.pack() #conteudo em variavel

test teste teste de github
# run the app
window.mainloop()