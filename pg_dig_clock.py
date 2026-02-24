### インポート
import os
import datetime
import pygame
from pygame.locals import *

### 定数
WIDTH  = 1024   # 幅
HEIGHT =  600   # 高
FONTS  = "Monospace" # フォントフェース
POINTS =  360   # フォントポイント

os.environ["DISPLAY"] = ":0.0" # メインディスプレイ

### モジュール初期化
pygame.init()

### 時間オブジェクト生成
clock = pygame.time.Clock()

### 画面設定
# surface = pygame.display.set_mode(( WIDTH, HEIGHT))
surface = pygame.display.set_mode(( WIDTH, HEIGHT), pygame.FULLSCREEN)

### 無限ループ
while True:

    ### 画面初期化
    surface.fill(( 0, 0, 0))

    ### 現在時刻取得
    now = datetime.datetime.now()

    ### 時刻フォント設定
    font = pygame.font.SysFont( FONTS, POINTS)
    time = "{:02}:{:02}:{:02}".format( now.hour, now.minute, now.second)
    text = font.render( time, True, ( 255, 255, 255))

    ### 時刻表示
    surface.blit(text, (int((WIDTH-font.size(time)[0])/2), int((HEIGHT-font.size(time)[1])/2)))

    ### 画面更新
    pygame.display.update()

    ### フレームレート設定
    clock.tick(60)

    ### イベント処理
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            break
    else:
        continue

    ### whileループ終了
    break

### 終了処理
pygame.quit()