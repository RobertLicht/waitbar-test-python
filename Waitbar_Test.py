# -*- coding: utf-8 -*-
"""
Created on 11.02.2021

:author: Robert-Vincent Lichterfeld

# Quelle: https://itsphbytes.wordpress.com/2017/03/15/progress-bar-in-python/
# Quelle: https://stackoverflow.com/a/24330806
"""

# =========================================================================
#   Importieren von Modulen
# =========================================================================
import time
import threading

# Module aus der Tkinter - Klasse importieren
import tkinter.ttk as ttk
from tkinter import Tk, Toplevel, IntVar, Frame, Menu, filedialog, Message, messagebox, Entry, Button, Radiobutton, BOTTOM, TOP, CENTER, Label, N, S, E, W, Checkbutton, END, SUNKEN, X, BOTH, YES  # Python 3.X



# =========================================================================
#   Klasse - Waitbar mit Bearbeitungsanimation
# =========================================================================
class Waitbar(Toplevel):
    """
    Bearbeitungsanimation um dem Nutzer eine Rueckmeldung zur Aktivitaet zu geben
    """
    #  Initialisierung des UI   #97931A
    def __init__(self, parent, str_textlabeltitle="Default_Text", width=0.25, height=0.125, usefactor=True):
        Toplevel.__init__(self, parent, bg="#3b4d61")
        self.title("Waitbar")

        # get screen width and height
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        w = (usefactor and ws * width) or width
        h = (usefactor and ws * height) or height
        # calculate position x, y
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.overrideredirect(True)
        self.lift()

        #  Statischer Eintrag   #97931A
        str_textfirstlabel = "\n\n\n\n " + str_textlabeltitle
        first_label = Label(self, text=str_textfirstlabel, bg="#3b4d61", fg="black", font=("Arial", 14, "bold"))
        first_label.pack()

        # Fortschrittsanzeige bzw. Ladeanimation definieren
        pb_style = ttk.Style()
        pb_style.theme_use('winnative')
        pb_style.configure("Brown.Horizontal.TProgressbar", foreground="#6B6351", background="#6B6351")
        self.obj_progressbar = ttk.Progressbar(self,
                                          style="Brown.Horizontal.TProgressbar",
                                          orient='horizontal',
                                          length=300, mode='indeterminate')  # mode='indeterminate' # mode='determinate'
        # Place the bar at the centre of the window
        self.obj_progressbar.place(relx=0.5, rely=0.66, anchor=CENTER)

        # Ladeanimation anzeigen
        #   Prozentualer Fortschritt mit Wartezeit in Sekunden
        # self.progress_bar(5, obj_progressbar)

        #   Text und animierter Balken
        # self.progress_bar_text(obj_progressbar, ['Bib_1 laden', 'Bib_2 laden', 'Umgebung vorbereiten'])

        #   Animierter Balken
        # obj_progressbar.start()

        # time.sleep(0.125)

        # # required to make window show before the program gets to the mainloop
        self.update()

    def progress_bar_start(self):
        self.obj_progressbar.start()

    def progress_bar_stop(self):
        self.obj_progressbar.stop()

    def progress_bar(self, seconds, obj_progressbar):
        for num_progress in range(0, seconds + 1):
            num_percent = (num_progress * 100) // seconds
            # Text zum label generieren
            str_textloadinglabel = str(num_percent) + "%"
            # Label definieren
            load_label = Label(self, text=str_textloadinglabel, bg="#6B6351", fg="black", font=("Arial", 12, "bold"))
            # Fortschrittsanzeige mit aktuellem Wert beschreiben
            obj_progressbar['value'] = num_percent
            # alternativ: # obj_progressbar.start(10)
            # Label anzeigen und platzieren
            load_label.place(relx=0.5, rely=0.80, anchor=CENTER)
            self.update()
            time.sleep(1)

    def progress_bar_text(self, obj_progressbar, list_textelem=['Bib_1 laden', 'Umgebung vorbereiten']):
        obj_progressbar.start(30)
        for str_textelem in list_textelem:
            # Text zum label generieren
            str_textloadinglabel = str(str_textelem)
            # Label definieren
            load_label = Label(self, text=str_textloadinglabel, bg="#6B6351", fg="black", font=("Arial", 12, "bold"))
            load_label.place(relx=0.5, rely=0.80, anchor=CENTER)
            self.update()
            time.sleep(1)

# Konstruktor fuer das UI initialisieren
rootFigure = Tk()

# Ausführung des UI
def real_traitement():
    Waitbar(rootFigure, str_textlabeltitle="Bitte Warten", width=0.25, height=0.125, usefactor=True).progress_bar_start()
    for num_iter in range(0, int(2E5)):
        print(num_iter)
    Waitbar(rootFigure, str_textlabeltitle="Bitte Warten", width=0.25, height=0.125, usefactor=True).progress_bar_stop()


# Execute progressbar in an thread
threading.Thread(target=real_traitement).start()


# Schleife zur dauerhaften Ausfuehrung des Konstruktors
rootFigure.mainloop()

"""
#   Beispiel zur Verwendung
# Splash Screen ausfuehren
self.__obj_Master.withdraw()
splash = Splash(parent=self.__obj_Master, str_textlabeltitle="Bitte Warten", width=0.25,
                height=0.125, useFactor=True)

# Hauptprogram laden

# finished loading so destroy splash
splash.destroy()

# show window again
self.__obj_Master.deiconify()
"""