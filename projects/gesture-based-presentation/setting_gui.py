
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


import os
from pathlib import Path
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from gesture_capture import capture_gesture
from settings import *
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/home/calto/build/assets/frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_setting():
    window = Tk()

    window.geometry("1440x1024")
    window.configure(bg = "#3B3B3B")


    canvas = Canvas(
        window,
        bg = "#3B3B3B",
        height = 1024,
        width = 1440,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=os.path.join('assets', 'frame1', "image_1.png"))
    image_1 = canvas.create_image(
        371.0,
        151.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=os.path.join('assets', 'frame1', "image_2.png"))
    image_2 = canvas.create_image(
        371.0,
        581.0,
        image=image_image_2
    )

    canvas.create_text(
        948.0,
        143.0,
        anchor="nw",
        text="Choose Alignment",
        fill="#FFFFFF",
        font=("Inter", 30 * -1)
    )

    image_image_3 = PhotoImage(
        file=os.path.join('assets', 'frame1', "image_3.png"))
    image_3 = canvas.create_image(
        886.0,
        297.0,
        image=image_image_3
    )

    image_image_4 = PhotoImage(
        file=os.path.join('assets', 'frame1', "image_4.png"))
    image_4 = canvas.create_image(
        883.0,
        437.0,
        image=image_image_4
    )

    image_image_5 = PhotoImage(
        file=os.path.join('assets', 'frame1', "image_5.png"))
    image_5 = canvas.create_image(
        884.0,
        725.0,
        image=image_image_5
    )

    image_image_6 = PhotoImage(
        file=os.path.join('assets', 'frame1', "image_6.png"))
    image_6 = canvas.create_image(
        883.0,
        869.0,
        image=image_image_6
    )
    def change_slide_left():
        capture_gesture(SLIDE_CHANGE_GESTURE,capture_right=False)
    button_image_1 = PhotoImage(
        file=os.path.join('assets', 'frame1', "button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=change_slide_left,
        relief="flat"
    )
    button_1.place(
        x=958.0,
        y=556.0,
        width=65.0,
        height=63.0
    )
    def change_erase():
        capture_gesture(ERASE_GESTURE)
    button_image_2 = PhotoImage(
        file=os.path.join('assets', 'frame1', "button_1.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=change_erase,
        relief="flat"
    )
    button_2.place(
        x=958.0,
        y=692.0,
        width=65.0,
        height=63.0
    )
    def change_point_left():
        capture_gesture(POINTER_SIZE_CHANGE_GESTURE,capture_right=False)
    button_image_3 = PhotoImage(
            file=os.path.join('assets', 'frame1', "button_1.png"))

    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=change_point_left,
        relief="flat"
    )
    button_3.place(
        x=958.0,
        y=838.0,
        width=65.0,
        height=63.0
    )
    def change_pointing():
        window.destroy()
        capture_gesture(POINTING_GESTURE)

    button_image_4 = PhotoImage(
            file=os.path.join('assets', 'frame1', "button_1.png"))

    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=change_pointing,
        relief="flat"
    )
    button_4.place(
        x=958.0,
        y=269.0,
        width=65.0,
        height=63.0
    )
    def change_annotating():
        window.destroy()
        capture_gesture(ANNOTATING_GESTURE)
    button_image_5 = PhotoImage(
            file=os.path.join('assets', 'frame1', "button_1.png"))

    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=change_annotating,
        relief="flat"
    )
    button_5.place(
        x=958.0,
        y=410.0,
        width=65.0,
        height=63.0
    )
    def change_slide_right():
        window.destroy()
        capture_gesture(SLIDE_CHANGE_GESTURE,capture_left=False)
    button_image_6 = PhotoImage(
            file=os.path.join('assets', 'frame1', "button_1.png"))

    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=change_slide_right,
        relief="flat"
    )
    button_6.place(
        x=1257.0,
        y=556.0,
        width=65.0,
        height=63.0
    )
    def change_point_right():
        window.destroy()
        capture_gesture(POINTER_SIZE_CHANGE_GESTURE,capture_left=False)
    button_image_7 = PhotoImage(
            file=os.path.join('assets', 'frame1', "button_1.png"))

    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=change_point_right,
        relief="flat"
    )
    button_7.place(
        x=1257.0,
        y=837.0,
        width=65.0,
        height=63.0
    )

    button_image_8 = PhotoImage(
            file=os.path.join('assets', 'frame1', "button_8.png"))
    def open_home_page():
        from gui import open_home
        window.destroy()
        open_home()
    button_8 = Button(
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=open_home_page,
        relief="flat"
    )
    button_8.place(
        x=44.0,
        y=38.0,
        width=77.0,
        height=69.0
    )

    image_image_7 = PhotoImage(
            file=os.path.join('assets', 'frame1', "image_7.png"))

    image_7 = canvas.create_image(
        883.0,
        583.0,
        image=image_image_7
    )

    image_image_8 = PhotoImage(
        file=os.path.join('assets', 'frame1', "image_8.png"))
    image_8 = canvas.create_image(
        1188.0,
        582.0,
        image=image_image_8
    )

    image_image_9 = PhotoImage(
        file=os.path.join('assets', 'frame1', "image_9.png"))
    image_9 = canvas.create_image(
        1191.0,
        865.0,
        image=image_image_9
    )

    canvas.create_text(
        856.0,
        633.0,
        anchor="nw",
        text="Left",
        fill="#FFFFFF",
        font=("Inter", 25 * -1)
    )

    canvas.create_text(
        856.0,
        930.0,
        anchor="nw",
        text="Left",
        fill="#FFFFFF",
        font=("Inter", 25 * -1)
    )

    canvas.create_text(
        1159.0,
        630.0,
        anchor="nw",
        text="Right",
        fill="#FFFFFF",
        font=("Inter", 25 * -1)
    )

    canvas.create_text(
        1160.0,
        924.0,
        anchor="nw",
        text="Right",
        fill="#FFFFFF",
        font=("Inter", 25 * -1)
    )
    window.resizable(True, True)

    window.mainloop()
