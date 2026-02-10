import time
import os
from datetime import datetime

try:
    while True:
        # 画面をクリアして常に上部に表示（Linux用）
        os.system('clear')
        
        # 現在の日時を取得してフォーマット
        now = datetime.now()
        date_str = now.strftime("%Y/%m/%d (%a)")
        time_str = now.strftime("%H:%M:%S")
        
        print("========================")
        print(f"   {date_str}")
        print(f"      {time_str}")
        print("========================")
        print("\n(Ctrl+C で終了します)")
        
        time.sleep(1)
except KeyboardInterrupt:
    print("\n終了しました。")
