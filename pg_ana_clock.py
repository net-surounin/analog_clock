### インポート
import math
import datetime
import pygame
from pygame.locals import *

### 定数
WIDTH    =1024      # 幅
HEIGHT   = 600      # 高さ
RADIUS   = 250      # 半径
NEEDLE_H = 185      # 短針
NEEDLE_M = 210      # 長針
NEEDLE_S = 240      # 秒針
MARK_H   = 225      # 時字
MARK_M   = 270      # 分字
BASE_AGL = 90       # 基準角度
CENTER   = int(WIDTH/2),int(HEIGHT/2)

### モジュール初期化
pygame.init()

### 時間オブジェクト生成
clock = pygame.time.Clock()

### 画面設定
surface = pygame.display.set_mode((WIDTH,HEIGHT), pygame.NOFRAME)

### 無限ループ
while True:

    ### 画面初期化
    surface.fill((0,0,0))

    ### 円表示
    pygame.draw.circle(surface, (128,128,128), (CENTER), RADIUS+5, 3)

    ### 目盛り表示
    for mark in range(0, 360, 6):
        mark_o_x = round(math.cos(math.radians(mark))*RADIUS)           # 外側のX座標
        mark_o_y = round(math.sin(math.radians(mark))*RADIUS)           # 外側のY座標

        ### 正時
        if 0 == mark % 30:
            mark_i_x = round(math.cos(math.radians(mark))*(RADIUS-10))   # 内側のX座標
            mark_i_y = round(math.sin(math.radians(mark))*(RADIUS-10))   # 内側のY座標
            pygame.draw.line(surface, (255,255,255), (CENTER[0]+mark_i_x,CENTER[1]+mark_i_y), (CENTER[0]+mark_o_x,CENTER[1]+mark_o_y), 4)

        ### 正時以外
        else:
            mark_i_x = round(math.cos(math.radians(mark))*(RADIUS-6))   # 内側のX座標
            mark_i_y = round(math.sin(math.radians(mark))*(RADIUS-6))   # 内側のY座標
            pygame.draw.line(surface, (255,255,255), (CENTER[0]+mark_i_x,CENTER[1]+mark_i_y), (CENTER[0]+mark_o_x,CENTER[1]+mark_o_y), 2)

    ### 時字表示
    dic = {"1":300,"2":330,"3":0,"4":30,"5":60,"6":90,"7":120,"8":150,"9":180,"10":210,"11":240,"12":270}
    for mark,angle in dic.items():

        ### 時字作成
        font = pygame.font.SysFont(None, 40)
        text = font.render(mark, True, (128,255,255))

        ### 座標設定
        mark_x = round(math.cos(math.radians(angle))*MARK_H)+CENTER[0]-int(font.size(mark)[0]/2)
        mark_y = round(math.sin(math.radians(angle))*MARK_H)+CENTER[1]-int(font.size(mark)[1]/2)

        ### 時字表示
        surface.blit(text, (mark_x,mark_y))

    ### 分字表示
    dic = {"5":300,"10":330,"15":0,"20":30,"25":60,"30":90,"35":120,"40":150,"45":180,"50":210,"55":240,"0":270}
    for mark,angle in dic.items():

        ### 分字作成
        font = pygame.font.SysFont(None, 30)
        text = font.render(mark, True, (128,255,255))

        ### 座標設定
        mark_x = round(math.cos(math.radians(angle))*MARK_M)+CENTER[0]-int(font.size(mark)[0]/2)
        mark_y = round(math.sin(math.radians(angle))*MARK_M)+CENTER[1]-int(font.size(mark)[1]/2)

        ### 時字表示
        surface.blit(text, (mark_x,mark_y))


    ### 現在時刻取得
    now = datetime.datetime.now()

    ### 角度計算
    angle_h = float(BASE_AGL - 30 * now.hour - 0.5 * now.minute)    # 時
    angle_m = int(BASE_AGL - 6 * now.minute)                        # 分
    angle_s = int(BASE_AGL - 6 * now.second)                        # 秒

    ### 針の終端位置
    pos_hx = round(math.cos(math.radians(angle_h))*NEEDLE_H)    # 時のX座標
    pos_hy = round(math.sin(math.radians(angle_h))*NEEDLE_H)    # 時のY座標
    pos_mx = round(math.cos(math.radians(angle_m))*NEEDLE_M)    # 分のX座標
    pos_my = round(math.sin(math.radians(angle_m))*NEEDLE_M)    # 分のY座標
    pos_sx = round(math.cos(math.radians(angle_s))*NEEDLE_S)    # 秒のX座標
    pos_sy = round(math.sin(math.radians(angle_s))*NEEDLE_S)    # 秒のY座標

    ### 針表示
    pygame.draw.line(surface, (255,255,255), (CENTER), (CENTER[0]+pos_hx,CENTER[1]-pos_hy), 10)
    pygame.draw.circle(surface, (255,255,255), (CENTER[0]+pos_hx,CENTER[1]-pos_hy), 5)
    pygame.draw.line(surface, (255,255,255), (CENTER), (CENTER[0]+pos_mx,CENTER[1]-pos_my), 7)
    pygame.draw.circle(surface, (255,255,255), (CENTER[0]+pos_mx,CENTER[1]-pos_my), 3)
    pygame.draw.line(surface, (255,0,0), (CENTER), (CENTER[0]+pos_sx,CENTER[1]-pos_sy), 2)
    pygame.draw.circle(surface, (255,0,0), (CENTER), 12)

    ### 画面更新
    pygame.display.update()

    ### フレームレート設定
    clock.tick(100)

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