# Quelle: https://stackoverflow.com/a/33771196
from tkinter import Button, Tk, HORIZONTAL, Label, W, E

# from tkinter.ttk import Progressbar
import tkinter.ttk as ttk
import time
import threading


class MonApp(Tk):
    def __init__(self):
        super().__init__()

        # MonApp.title(" | MUC | Tool - ")
        # Titel erstellen
        self.label_title = Label(text="===  Eingaben zum Tool",
                                 bg="#6B6351", fg="white")
        # Wigdets platzieren - Titel
        self.label_title.grid(row=0, column=1, columnspan=5, sticky=W + E)
        self.label_title.config(font=("Arial", 12))
        self.btn = Button(self, text='Traitement', command=self.traitement)
        self.btn.grid(row=10, column=0)
        pb_style = ttk.Style()
        pb_style.theme_use('winnative')
        pb_style.configure("Brown.Horizontal.TProgressbar", foreground="#6B6351", background="#6B6351")
        self.progress = ttk.Progressbar(self, orient=HORIZONTAL, style="Brown.Horizontal.TProgressbar",  mode='indeterminate')
        # self.progress.grid(row=25, column=2, columnspan=3, sticky=W + E)


    def traitement(self):
        def real_traitement():
            # self.progress.grid(row=12, column=0)
            self.progress.grid(row=25, column=2, columnspan=3, sticky=W + E)
            self.progress.start()
            # # Just like you have many, many code lines...
            time.sleep(3)
            for num_iter in range(0, int(3E5)):
                print(num_iter)
            self.progress.stop()
            self.progress.grid_forget()

            self.btn['state'] = 'normal'

        self.btn['state'] = 'disabled'
        threading.Thread(target=real_traitement).start()

if __name__ == '__main__':

    app = MonApp()
    app.mainloop()
