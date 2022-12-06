from tkinter import *
from tkinter import filedialog, ttk
from tkinter.ttk import *
from PIL import Image, ImageTk



window= Tk()
window.title("Add watermark to your picture")

resized_img= None
# button_photo= Image.open('photo.png')
# photoimage= button_photo.subsample(3,3)

def open_file():
    filename= filedialog.askopenfilename()
    return filename

def load_img():
    global resized_img, window, img
    #open image
    img= Image.open(open_file())
    watermark= Image.open('favicon.ico')

    #resizing watermark
    watermark= watermark.resize((30,20))

    #resizing image
    width= 300
    #change height according to width to maintain aspect ratio
    height = int(width*(img.size[1]/img.size[0]))
    resized_img= img.resize((width,height), Image.ANTIALIAS)

    #add watermatk and using mask to remove black background from png
    resized_img.paste(watermark,(resized_img.size[0]-watermark.size[0],resized_img.size[1]-watermark.size[1]),watermark)
    img= ImageTk.PhotoImage(resized_img)
    window.update()
    img_area= Label(window, image=img)
    img_area.pack(padx=100, pady=10)

def savefile():
    global resized_img
    filename= filedialog.asksaveasfile(mode="w", defaultextension=".jpg")
    img_name= (filename.name.split('/')[-1])

    if not filename:
        return resized_img.save(filename)



window.geometry('700x500')
window.title('Watermark your picture')



my_font= ('Montserrat', 20, 'bold')
main_label= Label( text="Upload image to add a watermark", font=my_font, background="#E6DDC4")

main_label.pack(pady=20, padx=10)

open_img_button= Button( master=window,text="Upload image", width=20,command=lambda: load_img()).pack(pady=20, )
save_button= Button( master=window,text="Save", width=20, command=lambda : savefile()).pack()

window.configure(background="#E6DDC4")
window.mainloop()

