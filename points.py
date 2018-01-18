from tkinter import *

teams = [
		"Team 1",
		"Team 2",
		"Team 3",
		"Team 4",
		"Team 5",
		"Team 6"
]

scores = [0,0,0,0,0,0]

class Window(Frame):


    def __init__(self, master=None):
        Frame.__init__(self, master)                 
        self.master = master
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("Royal_Scoreboard //kdas")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a button instance
        up = Button(self, text="UP")
        down = Button(self, text = "DOWN")

        t1 = Label(self, text = teams[0],font=("Helvetica", 28))
        t2 = Label(self, text = teams[1],font=("Helvetica", 28))
        t3 = Label(self, text = teams[2],font=("Helvetica", 28))
        t4 = Label(self, text = teams[3],font=("Helvetica", 28))
        t5 = Label(self, text = teams[4],font=("Helvetica", 28))
        t6 = Label(self, text = teams[5],font=("Helvetica", 28))

        def get(event):
        	scores[0] = int(e1.get()) + scores[0]
        	e1.delete(0,END)
        	e1.insert(0,0)
        	s1.config(text = scores[0])
        	scores[1] = int(e2.get()) + scores[1]
        	e2.delete(0,END)
        	e2.insert(0,0)
        	s2.config(text = scores[1])
        	scores[2] = int(e3.get()) + scores[2]
        	e3.delete(0,END)
        	e3.insert(0,0)
        	s3.config(text = scores[2])
        	scores[3] = int(e4.get()) + scores[3]
        	e4.delete(0,END)
        	e4.insert(0,0)
        	s4.config(text = scores[3])
        	scores[4] = int(e5.get()) + scores[4]
        	e5.delete(0,END)
        	e5.insert(0,0)
        	s5.config(text = scores[4])
        	scores[5] = int(e6.get()) + scores[5]
        	e6.delete(0,END)
        	e6.insert(0,0)
        	s6.config(text = scores[5])

        e1 = Entry(self, font = ("Helvetica", 18))
        e1.insert(0,0)
        e1.bind('<Return>', get)
        e2 = Entry(self, font = ("Helvetica", 18))
        e2.insert(0,0)
        e2.bind('<Return>', get)
        e3 = Entry(self, font = ("Helvetica", 18))
        e3.insert(0,0)
        e3.bind('<Return>', get)
        e4 = Entry(self, font = ("Helvetica", 18))
        e4.insert(0,0)
        e4.bind('<Return>', get)
        e5 = Entry(self, font = ("Helvetica", 18))
        e5.insert(0,0)
        e5.bind('<Return>', get)
        e6 = Entry(self, font = ("Helvetica", 18))
        e6.insert(0,0)
        e6.bind('<Return>', get)

        s1 = Label(self, text = 0,font=("Helvetica", 28))
        s2 = Label(self, text = 0,font=("Helvetica", 28))
        s3 = Label(self, text = 0,font=("Helvetica", 28))
        s4 = Label(self, text = 0,font=("Helvetica", 28))
        s5 = Label(self, text = 0,font=("Helvetica", 28))
        s6 = Label(self, text = 0,font=("Helvetica", 28))

        sc = Label(self, text = "SCORE", font = ("Helvetica", 30))
        sc.grid(row = 0, column = 2, padx = 50)

        # placing the button on my window
        # up.grid(row = 0, column = 0)
        # down.grid(row = 0, column = 1)
        t1.grid(row = 1, column = 0, padx = 20, pady = 40)
        t2.grid(row = 2, column = 0, padx = 20, pady = 40)
        t3.grid(row = 3, column = 0, padx = 20, pady = 40)
        t4.grid(row = 4, column = 0, padx = 20, pady = 40)
        t5.grid(row = 5, column = 0, padx = 20, pady = 40)
        t6.grid(row = 6, column = 0, padx = 20, pady = 40)

        e1.grid(row = 1, column = 1, padx = 50)
        e2.grid(row = 2, column = 1, padx = 50)
        e3.grid(row = 3, column = 1, padx = 50)
        e4.grid(row = 4, column = 1, padx = 50)
        e5.grid(row = 5, column = 1, padx = 50)
        e6.grid(row = 6, column = 1, padx = 50)

        s1.grid(row = 1, column = 2, padx = 50)
        s2.grid(row = 2, column = 2, padx = 50)
        s3.grid(row = 3, column = 2, padx = 50)
        s4.grid(row = 4, column = 2, padx = 50)
        s5.grid(row = 5, column = 2, padx = 50)
        s6.grid(row = 6, column = 2, padx = 50)

root = Tk()


app = Window(root)
root.mainloop()