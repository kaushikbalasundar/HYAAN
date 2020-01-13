import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import numpy as np
import os


class MyVideoCapture:
    def __init__(self, video_source=0):

        # Open the video source
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

          # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()
        self.window.mainloop()
    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)
class App:
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source

        # open video source
        self.vid = MyVideoCapture(video_source)

        # Create a canvas that can fit the above video source size
        self.canvas = tkinter.Canvas(window, width = self.vid.width, height = self.vid.height)
        self.canvas.pack()
        self.btn_snapshot=tkinter.Button(window, text="Snapshot", width=50, command=self.snapshot)
        self.btn_snapshot.pack(anchor=tkinter.CENTER, expand=True)
        self.delay = 15
        self.update()

        self.window.mainloop()
    def update(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()

        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)
        self.window.after(self.delay, self.update)
    def snapshot(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()
        if ret:
            cv2.imwrite("frame_test.jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
            self.window.destroy()
            self.window = tkinter.Tk()
            self.cv_img = cv2.cvtColor(cv2.imread("frame_test.jpg"), cv2.COLOR_BGR2RGB)
            self.height, self.width, self.no_channels = self.cv_img.shape
            self.canvas = tkinter.Canvas(self.window, width = self.width, height = self.height)
            self.canvas.pack()
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(self.cv_img))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)
            self.delay = 15
            self.window.after(self.delay, self.label)
            self.window.mainloop()

    def label(self):
        self.window.destroy()
        os.system('python -m scripts.label_image --image=frame_test.jpg')
        



App(tkinter.Tk(), "Tkinter and OpenCV")
