from tkinter import *
from tkinter import messagebox

def bot_click():
    messagebox.showinfo("imformação", "botão clicado!")

janela = Tk()
janela.title('interface grafica')

img_rot = PhotoImage(file='gatinho.png')

img = Label(janela, image=img_rot)
img.pack(pady=10)

bt = Button(janela, width=10, text='click aqui', bg='blue', command=bot_click)
bt.pack(pady=20)
janela.geometry('300x300+100+100')
janela.mainloop()