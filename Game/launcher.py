from tkinter import Tk, StringVar
from tkinter import Label
from tkinter import Button
from tkinter import OptionMenu
import os

res = None


class app(Tk):
    def __init__(self):
        super().__init__()
        self.SupportedResolutions = ['192x272', '384x544']
        self.createWidgets()

        self.title("Launch: Synergi")
        self.geometry("300x30")

    def createWidgets(self):
        self.res = StringVar(self)
        self.res.set(self.SupportedResolutions[0])
        self.resLabel = Label(self, text="Resolution: ")
        self.resLabel.grid(column=0, row=0)
        self.resOpt = OptionMenu(self, self.res, *self.SupportedResolutions)
        self.resOpt.grid(column=1, row=0)
        self.launchbtn = Button(self, command=self.launch, text="Launch")
        self.launchbtn.grid(column=2, row=0)

    def launch(self):
        self.destroy()
        print("Launching")
        os.system("python {} {} {}".format(os.path.join(os.getcwd(), 'Game', 'Scripts', 'Game.py'), self.res.get().split('x')[0], self.res.get().split('x')[1]))


launcher = app()
launcher.mainloop()
