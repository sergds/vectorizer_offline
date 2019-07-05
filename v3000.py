import os
import platform
from random import randint
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb

from PIL import Image

appf = os.path.realpath(__file__)
appdir = os.path.dirname(appf)
bin_path = appdir + '/bin'
global or_image
or_image = ''
root = Tk()


def select_file():
    global or_image
    or_image = fd.askopenfilename(filetypes=(('JPEG Image', '*.jpg'), ('PNG Image', '*.png')))


def chk_file():
    if not or_image == '':
        im = Image.open(or_image)
        h, w = im.size
        if h > 1920 and w > 1080:
            mb.showerror("b0rken", "Max Resolution is 1920x1080(Full HD)!!")
        else:
            vectorize()
    else:
        mb.showerror("b0rken", "No file selected!!")


def vectorize():
    host_os = platform.system()
    jn = randint(1, 10000)
    print('Host os is' + host_os)
    arm_mode = 0
    if host_os == 'Darwin':
        executable = 'primitive_darwin_amd64'
    if host_os == 'Linux':
        executable = 'primitive_linux_amd64'
    if host_os == 'Windows':
        executable = 'primitive_windows_amd64.exe'
    if host_os == 'arm':
        arm_mode = 1
        executable = 'primitive_linux_arm'
    if host_os == 'armv7l':
        arm_mode = 1
        executable = 'primitive_linux_arm'
    if host_os == 'aarch64':
        arm_mode = 1
        executable = 'primitive_linux_arm64'
    if arm_mode == 1:
        clim = '%s/%s -m 1 -v -n 100 -o %s/%s.png -i %s' % (bin_path, executable, appdir, jn, or_image)
    else:
        clim = '%s/%s -m 1 -v -n 145 -o %s/%s.png -i %s' % (bin_path, executable, appdir, jn, or_image)
        os.system(clim)
        mb.showinfo('Success!', 'Done.')


root.title('Vectorizer 3000')
root.geometry('500x150+300+200')
root.resizable(False, False)
logo = Label(text='VECTORIZER 3000', font='papyrus 35')
select_f = Button(text='Select File', command=select_file)
vec_start = Button(text='Start', command=chk_file)
note = Label(text="NOTE: Resulting files will appear in executable's directory")
logo.pack()
select_f.pack()
vec_start.pack()
note.pack()
root.mainloop()
