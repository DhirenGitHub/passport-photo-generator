from rembg import remove
from rembg.bg import remove, new_session

from PIL import ImageTk, Image, ImageOps
import tkinter as tk
from tkinter import filedialog, colorchooser


selectedFile = ""
displayPic = "template.jpg"
BgColor = None

def changeImg():
    global panel
    img = Image.open(displayPic).convert('RGBA')
    img = ImageOps.exif_transpose(img)
    img = img.resize((413, 531))
    img = ImageTk.PhotoImage(img)
    panel.config(image=img)
    panel.image = img

def UploadAction(event=None):
    global selectedFile, displayPic

    filename = filedialog.askopenfilename()
    selectedFile = filename
    print('Selected:', filename)

    displayPic = selectedFile
    changeImg()


def choose_color():
    global BgColor
    color = colorchooser.askcolor(title ="Choose color") 
    print(color)

    BgColor = color


def CreatePhoto():
    global displayPic, BgColor

    input_path =  selectedFile
    input = Image.open(input_path) 
    input = ImageOps.exif_transpose(input)
    background = Image.new('RGB', input.size, BgColor[0])

    #output = remove(input)  

    my_session = new_session("u2net_human_seg")
    output = remove(input, session=my_session)

    
    output = remove(input)

    background.paste(output, (0, 0), output)
    background = background.convert('RGB')
    background.save('passportphoto.jpg')

    displayPic = "passportphoto.jpg"
    changeImg()
    print("complete")


root = tk.Tk()

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

button = tk.Button(root, text='Open', command=UploadAction)
button.grid(row=0, column=0, padx=5, pady=5)
button = tk.Button(root, text='BG color', command=choose_color)
button.grid(row=0, column=1, padx=5, pady=5)
button = tk.Button(root, text='Create', command=CreatePhoto)
button.grid(row=0, column=2, padx=5, pady=5)

img = Image.open(displayPic).convert('RGBA')
img = img.resize((413, 531))
img = ImageTk.PhotoImage(img)
panel = tk.Label(root, image=img)
panel.image = img
panel.grid(row=1, column=0,columnspan=3, sticky="ew")


root.mainloop()