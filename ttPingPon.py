import tkinter as tk

def move_circle():
    global x_speed
    # 円の現在の座標を取得
    pos = canvas.coords(circle)
    
    # 左右の壁に当たったら速度を反転させる
    if pos[2] >= 400 or pos[0] <= 0:
        x_speed = -x_speed
    
    # 円を移動 (dx, dy)
    canvas.move(circle, x_speed, 0)
    
    # 10ミリ秒後に再度この関数を実行
    root.after(100, move_circle)

root = tk.Tk()
root.title("円の左右移動")

canvas = tk.Canvas(root, width=400, height=200, bg="white")
canvas.pack()

# 円を描画 (x1, y1, x2, y2)
circle = canvas.create_oval(175, 75, 225, 125, fill="blue")

x_speed = 3  # 移動速度
move_circle()

root.mainloop()
