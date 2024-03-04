from PIL import ImageTk, Image
import tkinter as tk


#region CONSTS

#endregion


#region FUNCTIONS
def flip_left_right():
    print('Flip Left Right')

def flip_up_down():
    print('Flip Up Down')

def blur():
    print('Blur')

def contour():
    print('Contour')

def relief():
    print('Relief')

def edges():
    print('Edges')

def file_save():
    print('File Save')

def file_open():
    print('File Open')

def reset():
    print('Reset')

def set_blur_radius(value):
    print(f'Set Blur Radius to {value}')
#endregion


#region GUI - MAIN APP
main_window = tk.Tk()
main_window.title('Python Photoshop')
main_window.geometry('600x400')


#region PHOTO LABEL
photo_image = Image.open('algebra_campus.jpg')
photo = ImageTk.PhotoImage(photo_image)
lbl_photo = tk.Label(main_window,
                     text='Prostor za sliku',
                     image=photo)
lbl_photo.grid(row=0, column=0)
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


# BLUR
btn_flip_blur = tk.Button(main_window,
                          text='Blur',
                          command=blur)
btn_flip_blur.grid(row=2, column=1, padx=20)
scl_blur = tk.Scale(main_window,
                    orient='horizontal',
                    length=150,
                    from_= 1,
                    to=20,
                    command=set_blur_radius)
scl_blur.grid(row=3, column=1, padx=20)


# CONTOUR
btn_flip_contour = tk.Button(main_window,
                          text='Contour',
                          command=contour)
btn_flip_contour.grid(row=4, column=1, padx=20)

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
lbl_photo_details_var.set('Pocetna vrijednost')
lbl_photo_details = tk.Label(main_window,
                             textvariable=lbl_photo_details_var)
lbl_photo_details.grid(row=8, column=1, padx=20)
#endregion


main_window.mainloop()
#endregion
