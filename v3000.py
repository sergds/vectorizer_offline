import os
import platform
from random import randint, choice
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb

from PIL import Image

if getattr(sys, 'frozen', False):
    # frozen
    appdir = os.path.dirname(sys.executable)
else:
    # unfrozen
    appdir = os.path.dirname(os.path.realpath(__file__))
bin_path = appdir + '/bin'
global clim
clim = ''
global or_image
or_image = ''
execlist = ['primitive_darwin_amd64', 'primitive_linux_amd64', 'primitive_windows_amd64.exe', 'primitive_linux_arm',
            'primitive_linux_arm64']

err_str = ['b0rken', 'Yo :(', 'Fish ate a cat', '3000 / 0']

def select_file():
    global or_image
    or_image = fd.askopenfilename(filetypes=(('JPEG Image', '*.jpg'), ('PNG Image', '*.png')))


def chk_file():
    if not or_image == '':
        im = Image.open(or_image)
        h, w = im.size
        if h > 1920 and w > 1080:
            mb.showerror(choice(err_str), "Max Resolution is 1920x1080(Full HD)!!")
        else:
            vectorize()
    else:
        mb.showerror(choice(err_str), "No file selected!!")


def vectorize():
    host_os = platform.system()
    host_abi = platform.machine()
    jn = randint(1, 10000)
    print('Host os is' + host_os)
    arm_mode = 0
    if host_os == 'Darwin':
        executable = 'primitive_darwin_amd64'
    if host_os == 'Linux':
        executable = 'primitive_linux_amd64'
    if host_os == 'Windows':
        executable = 'primitive_windows_amd64.exe'
    if host_abi == 'arm':
        arm_mode = 1
        executable = 'primitive_linux_arm'
    if host_abi == 'armv7l':
        arm_mode = 1
        executable = 'primitive_linux_arm'
    if host_abi == 'aarch64':
        arm_mode = 1
        executable = 'primitive_linux_arm64'
    if arm_mode == 1:
        global clim
        clim = '%s/%s -m 1 -v -n 100 -o %s/%s.png -i %s' % (bin_path, executable, appdir, jn, or_image)
    else:
        clim = '%s/%s -m 1 -v -n 145 -o %s/%s.png -i %s' % (bin_path, executable, appdir, jn, or_image)
        os.system(clim)
        mb.showinfo('Success!', 'Done.')


def init2():
    status['text'] = 'Checking Files...'
    for biname in execlist:
        if os.path.exists(bin_path + '/' + biname):
            print(biname + ': OK')
        else:
            mb.showerror(choice(err_str), "Can't find " + biname)
            quit()
    status['text'] = 'Done.'

    status.destroy()
    canvas.destroy()

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


root = Tk()
root.resizable(False, False)
root.title('L0aDiNg...')
canvas = Canvas(root, width=373, height=140)
canvas.pack()
img = PhotoImage(file=appdir + '/slogo.png')
canvas.create_image(10, 10, anchor=NW, image=img)
status = Label(text='Initializing...')
status.pack()
root.after(500, init2)
root.mainloop()
