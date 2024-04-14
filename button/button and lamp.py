import tkinter as tk
from PIL import Image, ImageTk

class IndicatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ЛАМПОЧКА")

        self.button_img = Image.open("button_image.png")
        self.button_img = self.button_img.resize((100, 90), Image.BILINEAR)
        self.button_img = ImageTk.PhotoImage(self.button_img)

        self.indicator_on_img = Image.open("indicator_on.png")
        self.indicator_on_img = self.indicator_on_img.resize((300, 280), Image.BILINEAR)
        self.indicator_on_img = ImageTk.PhotoImage(self.indicator_on_img)

        self.indicator_off_img = Image.open("indicator_off.png")
        self.indicator_off_img = self.indicator_off_img.resize((300, 280), Image.BILINEAR)
        self.indicator_off_img = ImageTk.PhotoImage(self.indicator_off_img)

        self.indicator_state = False

        self.button = tk.Button(self.root, image=self.button_img, command=self.toggle_indicator)
        self.indicator_label = tk.Label(self.root, image=self.indicator_off_img)

        self.button.pack(pady=60)
        self.indicator_label.pack(pady=10)

    def toggle_indicator(self):
        self.indicator_state = not self.indicator_state

        if self.indicator_state:
            self.indicator_label.configure(image=self.indicator_on_img)
        else:
            self.indicator_label.configure(image=self.indicator_off_img)

root = tk.Tk()
app = IndicatorApp(root)
root.mainloop()