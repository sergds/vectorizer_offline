import os
import platform
from random import randint, choice
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import time
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
fmts = {'.svg', '.png', '.jpg'}
err_str = ['b0rken', 'Yo :(', 'Fish ate a cat', 'Space / 0', 'Moment of silence...']

def select_file():
    global or_image
    or_image = fd.askopenfilename(filetypes=(('JPEG Image', '*.jpg'), ('PNG Image', '*.png')))

def UpdateLoadStatus(txt)
	loadingText.set(txt)
    
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
    jn = randint(1, 10000)
    global clim
    clim = '"%s/%s" -m 1 -v -n %s -o "%s/%s%s" -i "%s"' % (
    bin_path, executable, pbox_var.get(), appdir, jn, curr_fmt, or_image)
    os.system(clim)
    mb.showinfo('Success!', 'Done.')


def change_dropdown(*args):
    global curr_fmt
    print('Out format is ' + tkvar.get())
    curr_fmt = tkvar.get()


def init2():
    global tkvar
    tkvar = StringVar(root)
    tkvar.set('.png')
    global pbox_var
    pbox_var = StringVar()
    global curr_fmt
    curr_fmt = '.png'
    global host_os
    host_os = platform.system()
    global host_abi
    host_abi = platform.machine()
    print('Host is ' + host_os)
    if host_os == 'Linux':
        print('Nice choice ;)')
    global iters
    iters = 0
    global executable
    executable = ''
    global arm_mode
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
        iters = 100
    else:
        iters = 145
    pbox_var.set(iters)
    UpdateLoadStatus('Checking Files...')
    for biname in execlist:
        if os.path.exists(bin_path + '/' + biname):
            print(biname + ': OK')
        else:
            mb.showerror(choice(err_str), "Can't find " + biname)
            quit()
    UpdateLoadStatus('Done.')
    time.sleep(1)
    status.destroy()
    canvas.destroy()

    root.title('Vectorizer 3000')
    root.geometry('500x250+300+200')
    root.resizable(False, False)
    sel_fmt = OptionMenu(root, tkvar, *fmts)
    logo = Label(text='VECTORIZER 3000', font='papyrus 35')
    select_f = Button(text='Select File', command=select_file)
    vec_start = Button(text='Start', command=chk_file)
    note1 = Label(text="Choose the output format:")
    note2 = Label(text="Enter primitives count:")
    pbox = Entry(textvariable=pbox_var)
    note = Label(text="NOTE: Resulting files will appear in executable's directory")
    logo.pack()
    select_f.pack()
    note1.pack()
    sel_fmt.pack()
    note2.pack()
    pbox.pack()
    # pbox.insert(0, iters)
    vec_start.pack()
    note.pack()
    tkvar.trace('w', change_dropdown)



root = Tk()
loadingText = Stringvar()
root.resizable(False, False)
root.title('L0aDiNg...')
canvas = Canvas(root, width=373, height=140)
canvas.pack()
img = PhotoImage(file=appdir + '/slogo.png')
canvas.create_image(10, 10, anchor=NW, image=img)
UpdateLoadStatus('Initializing...')
status = Label(text=loadingText)
status.pack()
root.after(500, init2)
root.mainloop()
