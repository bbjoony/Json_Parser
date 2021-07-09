import tkinter
import tkinter.filedialog as fd

window=tkinter.Tk()

window.title("Json Converter")
window.geometry("640x440+100+100")
window.resizable(True, True)

label=tkinter.Label(window,text="Json 파일을 CSV 파일로 변경합니다")
label.pack()

button = tkinter.Button(window, overrelief="solid", width=10, text="파일 열기")
button.pack()


def browsefunc():
    filename = fd.askopenfilename()
    pathlabel.config(text=filename)

browsebutton = button(window, text="파일 열기", command=browsefunc())
browsebutton.pack()

printlabel = Label(window)
pathlabel.pack()

window.mainloop()
