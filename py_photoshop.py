from PIL import ImageTk, Image, ImageFilter
from tkinter import filedialog as fd
import tkinter as tk


#region CONSTS
photo_path = 'algebra_campus.jpg'
photo_object = Image.open(photo_path)
reduce_scale = 3
photo_h_size = int(photo_object.size[0] / reduce_scale)
photo_v_size = int(photo_object.size[1] / reduce_scale)
photo_object = photo_object.resize((photo_h_size, photo_v_size))
photo_props = f'Photo size: {photo_object.size[0]} x {photo_object.size[1]}\nPhoto mode: {photo_object.mode}'
#endregion


#region FUNCTIONS
def flip_left_right():
    global photo_object, lbl_photo_image
    photo_object = photo_object.transpose(Image.FLIP_LEFT_RIGHT)
    lbl_photo_image = ImageTk.PhotoImage(photo_object)
    lbl_photo['image'] = lbl_photo_image


def flip_up_down():
    global photo_object, lbl_photo_image
    photo_object = photo_object.transpose(Image.FLIP_TOP_BOTTOM)
    lbl_photo_image = ImageTk.PhotoImage(photo_object)
    lbl_photo['image'] = lbl_photo_image


def bw():
    global photo_object, lbl_photo_image
    photo_object = photo_object.convert(mode='L')
    lbl_photo_image = ImageTk.PhotoImage(photo_object)
    lbl_photo['image'] = lbl_photo_image


def blur(radius):
    global photo_object, lbl_photo_image
    photo_object = Image.open(photo_path)

    if photo_object.size[0] > 1500:
        reduce_scale = 3
        photo_h_size = int(photo_object.size[0] / reduce_scale)
        photo_v_size = int(photo_object.size[1] / reduce_scale)
        photo_object = photo_object.resize((photo_h_size, photo_v_size))

    photo_object = photo_object.filter(ImageFilter.GaussianBlur(radius=int(radius)))
    
    lbl_photo_image = ImageTk.PhotoImage(photo_object)
    lbl_photo['image'] = lbl_photo_image


def contour():
    global photo_object, lbl_photo_image
    photo_object = photo_object.filter(ImageFilter.CONTOUR)
    
    lbl_photo_image = ImageTk.PhotoImage(photo_object)
    lbl_photo['image'] = lbl_photo_image


def relief():
    global photo_object, lbl_photo_image
    photo_object = photo_object.filter(ImageFilter.EMBOSS)
    
    lbl_photo_image = ImageTk.PhotoImage(photo_object)
    lbl_photo['image'] = lbl_photo_image


def edges():
    global photo_object, lbl_photo_image
    photo_object = photo_object.filter(ImageFilter.FIND_EDGES)
    
    lbl_photo_image = ImageTk.PhotoImage(photo_object)
    lbl_photo['image'] = lbl_photo_image


def file_save():
    global photo_object, lbl_photo_image
    photo_object.save(f'{photo_path}-01.jpg')


def file_open():
    global photo_path, photo_object, lbl_photo_image
    photo_path = fd.askopenfilename(title='Open image')

    photo_object = Image.open(photo_path)
    # reduce_scale = 3
    # photo_h_size = int(photo_object.size[0] / reduce_scale)
    # photo_v_size = int(photo_object.size[1] / reduce_scale)
    # photo_object = photo_object.resize((photo_h_size, photo_v_size))

    lbl_photo_image = ImageTk.PhotoImage(photo_object)
    lbl_photo['image'] = lbl_photo_image


def reset():
    global photo_object, lbl_photo_image
    photo_object = Image.open(photo_path)

    if photo_object.size[0] > 1500:
        reduce_scale = 3
        photo_h_size = int(photo_object.size[0] / reduce_scale)
        photo_v_size = int(photo_object.size[1] / reduce_scale)
        photo_object = photo_object.resize((photo_h_size, photo_v_size))

    lbl_photo_image = ImageTk.PhotoImage(photo_object)
    lbl_photo['image'] = lbl_photo_image
    scl_blur_var.set(1)

#endregion


#region GUI - MAIN APP
main_window = tk.Tk()
main_window.title('Python Photoshop')


#region PHOTO LABEL
lbl_photo_image = ImageTk.PhotoImage(photo_object)
lbl_photo = tk.Label(main_window,
                     text='Prostor za sliku',
                     image=lbl_photo_image)
lbl_photo.grid(row=0, column=0, rowspan=9)
#endregion

#region ACTIONS - BUTTONS
# FLIP
btn_flip_left_right = tk.Button(main_window,
                                text='Flip Left Right',
                                command=flip_left_right)
btn_flip_left_right.grid(row=0, column=1, padx=20)

btn_flip_up_down = tk.Button(main_window,
                             text='Flip Up Down',
                             command=flip_up_down)
btn_flip_up_down.grid(row=1, column=1, padx=20)


btn_bw = tk.Button(main_window,
                          text='Black / White',
                          command=bw)
btn_bw.grid(row=2, column=1, padx=20)


# BLUR
scl_blur_var = tk.IntVar()
scl_blur_var.set(1)
scl_blur = tk.Scale(main_window,
                    orient='horizontal',
                    variable=scl_blur_var,
                    length=150,
                    from_= 1,
                    to=20,
                    command=blur)
scl_blur.grid(row=3, column=1, padx=20)


# CONTOUR
btn_flip_contour = tk.Button(main_window,
                          text='Contour',
                          command=contour)
btn_flip_contour.grid(row=4, column=1, padx=20)


# Relief
btn_flip_relief = tk.Button(main_window,
                          text='Relief',
                          command=relief)
btn_flip_relief.grid(row=5, column=1, padx=20)

btn_flip_edges = tk.Button(main_window,
                          text='Edges',
                          command=edges)
btn_flip_edges.grid(row=6, column=1, padx=20)

btn_flip_save = tk.Button(main_window,
                          text='Save',
                          command=file_save)
btn_flip_save.grid(row=7, column=1, sticky='W', padx=20)

btn_flip_open = tk.Button(main_window,
                          text='Open',
                          command=file_open)
btn_flip_open.grid(row=7, column=1, padx=20)

btn_flip_reset = tk.Button(main_window,
                          text='Reset',
                          command=reset)
btn_flip_reset.grid(row=7, column=1, sticky='E', padx=20)
#endregion

#region PHOTO DETAILS
lbl_photo_details_var = tk.StringVar()
lbl_photo_details_var.set(photo_props)
lbl_photo_details = tk.Label(main_window,
                             textvariable=lbl_photo_details_var)
lbl_photo_details.grid(row=8, column=1, padx=20)
#endregion


main_window.mainloop()
#endregion
