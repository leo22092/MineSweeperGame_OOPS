from tkinter import Button
class Cell:
    def __init__(self,is_mine=False):
        self.is_mine=is_mine
        self.cell_btn_object=None
    def create_button_object(self,location):
        btn=Button(
            location,
            text="text"
        )
        btn.bind('<Button-1>',self.left_click_Action)
        btn.bind('<Button-3>',self.right_click_Action)

        self.cell_btn_object=btn
    def left_click_Action(self,event):
        print(event)
        print("I am left click")
    def right_click_Action(self,event):
        print(event)
        print("I am riht click")