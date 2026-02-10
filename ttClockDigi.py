import tkinter as tk
from time import strftime

def update_time():
    # 日付と時刻のフォーマットを指定
    string = strftime('%m-%d\n%H:%M:%S')
    label.config(text=string)
    # 1000ミリ秒（1秒）ごとに更新
    label.after(1000, update_time)

root = tk.Tk()
root.title("Digital Clock")

# 見た目の調整（背景黒、文字緑でデジタル風に）
label = tk.Label(root, font=('courier', 160, 'bold'), background='black', foreground='green')
label.pack(anchor='center', fill='both', expand=True)

update_time()
root.mainloop()

