from tkinter import *


#    Pack;
#    Grid;
#    Place.

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.initUI()

    def initUI(self):
        self.centerWindows()

    def centerWindows(self):
        w = 800
        h = 600

        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()

        x = (sw - w)/2
        y = (sh - h)/2
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))


def main():

    # Properties mainForm
    mainForm = Tk(className="Python Study")
    mainForm.geometry("800x600")

    app = Application(master=mainForm)
    app.mainloop()


if __name__ == '__main__':
    main()
