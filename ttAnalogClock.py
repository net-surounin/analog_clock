import tkinter as tk
import time
import math

class AnalogClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Analog Clock")
        
        # キャンバスのサイズ設定
        self.size = 550
        self.center = self.size / 2
        self.radius = self.size * 0.45
        
        self.canvas = tk.Canvas(root, width=self.size, height=self.size, bg='white')
        self.canvas.pack()
        
        # 時計の文字盤を描画
        self.draw_face()
        
        # 針（キャンバスアイテム）の初期化
        self.hour_hand = self.canvas.create_line(0, 0, 0, 0, width=6, fill='black')
        self.min_hand = self.canvas.create_line(0, 0, 0, 0, width=4, fill='blue')
        self.sec_hand = self.canvas.create_line(0, 0, 0, 0, width=2, fill='red')
        
        # 時刻更新の開始
        self.update_clock()

    def draw_face(self):
        # 文字盤の円
        self.canvas.create_oval(self.center - self.radius, self.center - self.radius,
                                self.center + self.radius, self.center + self.radius, width=2)
        # 文字・目盛り（簡易版）
        for i in range(12):
            angle = math.radians(i * 30 - 90)
            x = self.center + (self.radius - 10) * math.cos(angle)
            y = self.center + (self.radius - 10) * math.sin(angle)
            self.canvas.create_text(x, y, text=str(i if i != 0 else 12), font=("Helvetica", 12))

    def update_clock(self):
        # 現在時刻を取得
        now = time.localtime()
        hour = now.tm_hour % 12
        minute = now.tm_min
        second = now.tm_sec
        
        # 各針の角度計算（ラジアン）
        # 秒針
        sec_angle = math.radians(second * 6 - 90)
        # 分針（秒単位のズレも考慮）
        min_angle = math.radians(minute * 6 + second * 0.1 - 90)
        # 時針（分単位のズレも考慮）
        hour_angle = math.radians(hour * 30 + minute * 0.5 - 90)
        
        # 針の終点座標計算
        self.set_hand(self.sec_hand, self.radius * 0.9, sec_angle)
        self.set_hand(self.min_hand, self.radius * 0.7, min_angle)
        self.set_hand(self.hour_hand, self.radius * 0.5, hour_angle)
        
        # 100ms後に再度更新
        self.root.after(100, self.update_clock)

    def set_hand(self, hand, length, angle):
        x = self.center + length * math.cos(angle)
        y = self.center + length * math.sin(angle)
        self.canvas.coords(hand, self.center, self.center, x, y)

# アプリケーション実行
root = tk.Tk()
clock = AnalogClock(root)
root.mainloop()
