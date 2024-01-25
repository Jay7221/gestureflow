from spire.presentation import Presentation
import os
from tkinter import Tk, Label
from PIL import Image, ImageTk, ImageDraw
from threading import Thread
import time
from settings import *


def save_slides_as_png(input_filename, output_foldername):
    image_paths = []
    # Load the PowerPoint presentation
    presentation = Presentation()
    presentation.LoadFromFile(input_filename)

    for i, slide in enumerate(presentation.Slides):
        # Specify the output file name
        fileName = os.path.join(output_foldername, f"slide{i}.png")
        image_paths.append(fileName)
        # Save each slide as a PNG image
        image = slide.SaveAsImage()
        print(f"Loading slide: {i}")
        image.Save(fileName)
        image.Dispose()

    presentation.Dispose()
    return image_paths


class DisplayManager:
    def __init__(self):
        self.title = ""
        self.slides = []
        self.canvas = []
        self.draws = []
        self.slidePaths = []
        self.slideNumber = 0

        self.root = Tk()
        self.image_label = Label(self.root)
        self.image_label.pack()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def show(self):
        slide = Image.alpha_composite(self.slides[self.slideNumber], self.canvas[self.slideNumber])
        photo = ImageTk.PhotoImage(slide)
        self.image_label.config(image=photo)
        self.image_label.image = photo

    def show_pointer(self, coords):
        x, y = coords
        x *= 2
        y *= 2
        pointer_coords = [(x, y), (x + 10, y + 10)]
        pointer_color = (255, 0, 0, 255)
        blank = (0, 0, 0, 0)
        self.draws[self.slideNumber].rectangle(pointer_coords, fill=pointer_color)
        self.show()
        self.draws[self.slideNumber].rectangle(pointer_coords, fill=blank)

    def annotate(self, coords):
        x, y = coords
        x *= 2
        y *= 2
        pointer_coords = [(x, y), (x + 10, y + 10)]
        pointer_color = (255, 0, 0, 255)
        self.draws[self.slideNumber].rectangle(pointer_coords, fill=pointer_color)
        self.show()

    def erase(self, coords):
        x, y = coords
        x *= 2
        y *= 2
        pointer_coords = [(x, y), (x + 40, y + 40)]
        pointer_color = (0, 255, 0, 255)
        blank = (0, 0, 0, 0)
        self.draws[self.slideNumber].rectangle(pointer_coords, fill=pointer_color)
        self.show()
        self.draws[self.slideNumber].rectangle(pointer_coords, fill=blank)


    def nextSlide(self):
        if self.slideNumber == len(self.slides):
            self.slideNumber = 0
        self.show()
        self.slideNumber += 1

    def prevSlide(self):
        if self.slideNumber == len(self.slides):
            self.slideNumber = 0
        self.show()
        self.slideNumber += 1

    def setSlideNumber(self, slideNumber):
        self.slideNumber = max(0, min(slideNumber, len(self.slides) - 1))
        self.show()


    def load_from_pptx(self, input_filename):

        self.title, _ = os.path.splitext(os.path.basename(input_filename))
        self.root.title(self.title)

        output_foldername = os.path.join(IMAGE_PATH, self.title)
        if not os.path.exists(output_foldername):
            os.makedirs(output_foldername)

        self.slidePaths = save_slides_as_png(input_filename, output_foldername)

        for path in self.slidePaths:
            self.slides.append(Image.open(path))

        self.show()

    def load_folder(self, folderName):
        self.title = folderName
        folderPath = os.path.join(IMAGE_PATH, folderName)
        self.root.title(self.title)
        self.slidePaths = [os.path.join(folderPath, fileName) for fileName in os.listdir(folderPath)]
        for path in self.slidePaths:
            slide = Image.open(path).convert('RGBA')
            canvas = Image.new('RGBA', slide.size, (0, 0, 0, 0))
            self.slides.append(slide)
            self.canvas.append(canvas)
            self.draws.append(ImageDraw.Draw(canvas))

        self.show()

    def on_closing(self):
        self.root.destroy()

    def runLoop(self):
        self.root.mainloop()

def update(displayManager):
    while True:
        displayManager.nextSlide()
        time.sleep(2)


if __name__ == "__main__":
    displayManager = DisplayManager()
    displayManager.load_from_pptx('test.pptx')
    Thread(target=update, args=[displayManager]).start()
    displayManager.root.mainloop()
