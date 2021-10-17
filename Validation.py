from tkinter import*
from tkinter import ttk


def TK():
    pass


class House():
    def __init__(self,root):
        self.root=root
        self.root.title('House page')
        self.root.geometry('1600*790+0+0')



        if __name__ == '__main__' :
            root=TK()
            obj=House(root)
            root.mainloop()

