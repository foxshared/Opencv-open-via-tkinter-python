# make structure program more good
# without thread learn from online code sugoi
# Feature use start/stop show camera image, configuration port with save file can, 
# Can check a valid port from check image

import tkinter
from tkinter import ttk
import cv2
from PIL import Image, ImageTk
import os


folder_path = os.path.dirname(__file__)
#print(folder_path)
os.chdir(folder_path)

class process_():
    def __init__(self):
        self.status = 0

        self.gui_()
        self.camera_process_()

    def camera_process_(self):

        current_port = int(self.comboBOX.get())
        if current_port != self.last_port:
            self.last_port = current_port
            self.camera_port = cv2.VideoCapture(self.last_port)
            self.save_select_port(self.last_port)

            if self.camera_port.isOpened() is True:
                print("Image Valid")
                pass

            elif self.camera_port.isOpened() is False:
                no_image = ImageTk.PhotoImage(image=Image.open("test_img.png"))
                self.canvas.itemconfig(self.create, image=no_image)
                self.canvas.image = no_image

        if self.status == 1:
            buff, frame = self.camera_port.read()
            if buff:
                image_camera = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                image_camera2 = ImageTk.PhotoImage(
                    image=Image.fromarray(image_camera))

                self.canvas.itemconfig(self.create, image=image_camera2)
                self.canvas.image = image_camera2

        elif self.status == 0:
            no_image = ImageTk.PhotoImage(image=Image.open("test_img.png"))
            self.canvas.itemconfig(self.create, image=no_image)
            self.canvas.image = no_image

        self.window.after(10, self.camera_process_)

    def gui_(self):
        self.window = tkinter.Tk()

        self.canvas = tkinter.Canvas(self.window, width=600, height=500)
        self.canvas.pack()
        self.create = self.canvas.create_image(0, 0, anchor=tkinter.NW)

        self.button1 = tkinter.Button(
            self.window, text="Start/Stop", command=self.start_stop)
        self.button1.pack(side=tkinter.LEFT, anchor=tkinter.SW, padx=5, pady=5)

        self.label1 = tkinter.Label(self.window, text="Select Port:")
        self.label1.pack(side=tkinter.LEFT, anchor=tkinter.SW, padx=5, pady=5)

        self.n = tkinter.StringVar()
        self.comboBOX = ttk.Combobox(
            self.window, width=27, textvariable=self.n)

        val_port = self.valid_port()
        self.comboBOX["value"] = val_port
        self.comboBOX.pack(side=tkinter.LEFT,
                           anchor=tkinter.SW, padx=5, pady=5)

        port = self.get_save_port()
        self.last_port = port
        self.camera_port = cv2.VideoCapture(port)
        self.comboBOX.current(port)

        self.label_wlc = tkinter.Label(self.window, text="Hi Welcome")
        self.label_wlc.pack(side=tkinter.RIGHT,
                            anchor=tkinter.SE, padx=5, pady=5)

    def valid_port(self):
        print("Check valid port")
        list_ = []
        for i in range(5):
            c = cv2.VideoCapture(i)
            valid,_=c.read()
            if valid:
                list_.append(str(i))
        tuple_ = tuple(list_)
        return tuple_

    def start_stop(self):
        if self.status == 0:
            self.status = 1
        elif self.status == 1:
            self.status = 0

    def save_select_port(self, port_):
        if isinstance(port_, int):
            print("save port")
            c = open("temp_txt.txt").read()
            change_ = c.format(num_port=port_)
            w = open("port_save.txt", "w")
            w.write(change_)

    def get_save_port(self):
        try:
            g = open("port_save.txt","r")
            g = int(g.readline())
        except:
            n = open("port_save.txt","w+")
            n.write("0")
            n.close()
        return g


def main():
    cam = process_()
    cam.window.mainloop()


if __name__ == "__main__":
    main()
