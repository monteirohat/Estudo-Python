from doctest import master
from tkinter import *
from turtle import width

# color schema (material design) - https://material.io/resources/color/#!/?view.left=0&view.right=0&primary.color=424242
primary_color = "#424242"
dark_color = "#1b1b1b"
light_color = "#6d6d6d"
text_color = "#FFFFFF"


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.initUI()

    def initUI(self):
        self.centerWindows()

        # Create Menu
        frame_left_menu = Frame(
            master=self.master, width=210, height=600, bg=dark_color)

        frame_left_menu.columnconfigure(0, weight=1)

        menu = ['Emoticons']
        self.addButtonMenu("Emoticons", frame_left_menu)

        
        frame_left_menu.pack(side=LEFT)
        frame_left_menu.pack_propagate(False)

        


        # button_teste = Button(frame_left_menu,text="teste")
        # button_teste.pack(side=TOP, padx=5, pady=5)

        # button_teste2 = Button(frame_left_menu,text="teste")
        # button_teste2.pack(side=RIGHT, padx=5, pady=5)

        frame_main = Frame(master=self.master, width=100, bg=primary_color)
        frame_main.pack(fill=BOTH, side=RIGHT, expand=True)

       

    def centerWindows(self):
        w = 800
        h = 600

        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()

        x = (sw - w)/2
        y = (sh - h)/2
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def addButtonMenu(self, text_button, parent):
        item = Button(master=parent, text=text_button,
                      bg=light_color, fg=text_color,
                      activebackground=primary_color,
                      activeforeground=text_color)
        
        item.grid(column=0, row=0,padx=0, pady=3)


def main():

    # Properties mainForm
    mainForm = Tk(className="Python Study")
    mainForm.resizable(False, False)
    mainForm.geometry("800x600")

    app = Application(master=mainForm)
    app.mainloop()


if __name__ == '__main__':
    main()
