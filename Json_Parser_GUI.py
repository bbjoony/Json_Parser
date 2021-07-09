import tkinter as tk
import tkinter.filedialog as fd
import json
import pandas as pd

def browsefunc():
    file = fd.askopenfile()
    if file:
        print(file.name) # 파일을 제대로 읽어왔는지 확인
    contents = file.read()
    json_data = json.loads(contents)
    df = pd.json_normalize(json_data["records"])
    df.to_csv('sample+1.csv')

window=tk.Tk()

window.title("Json Converter")
window.geometry("640x440+100+100")
window.resizable(True, True)

label=tk.Label(window,text="Json 파일을 CSV 파일로 변경합니다")
label.pack()

button = tk.Button(window, overrelief="solid", width=10, text="파일 열기", command=browsefunc)
button.pack()

window.mainloop()
