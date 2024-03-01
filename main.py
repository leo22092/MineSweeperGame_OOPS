from tkinter import *
from cell import Cell
import settings
import utils

root=Tk()
# Over riding window settings

root.configure(bg="black")#giving background colour
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')#widthxheight
root.title("Mine Sweeper")
root.resizable(False,False)#for width and height to disable resizing

top_frame=Frame(
    root,
    bg='red',
    width=settings.WIDTH,
    height=utils.height_percnt(25)
)
top_frame.place(x=0,y=0)#where to plavce the frame created

left_frame=Frame(
    root,
    bg='blue',
    width=utils.width_percnt(25),
    height=utils.height_percnt(75)
)
left_frame.place(x=0,y=utils.height_percnt(25))

centre_frame=Frame(
    root,
    bg="green",
    width=utils.width_percnt(75),
    height=utils.height_percnt(75)

)
centre_frame.place(x=utils.width_percnt(25),y=utils.height_percnt(25))

# btn1=Button(
#     centre_frame,
#     bg='blue',
#     text='Button1'
# )
# btn1.place(x=0,y=0)

c1=Cell()
c1.create_button_object(centre_frame)
c1.cell_btn_object.grid(column=0,row=0)
c1.create_button_object(centre_frame)
c1.cell_btn_object.grid(column=0,row=1)
for x in range(5):
    for y in range(5):
        c=Cell()
        c.create_button_object(centre_frame)
        c.cell_btn_object.grid(column=x,row=y)

root.mainloop()

if __name__ == '__main__':
    print('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
