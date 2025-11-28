import subprocess
import time
import datetime
import sys

# 每天要執行的時段
time_slots = [
    (datetime.time(13, 0), datetime.time(14, 0)),
    (datetime.time(15, 0), datetime.time(16, 0)),
    (datetime.time(18, 0), datetime.time(19, 0)),
    (datetime.time(21, 0), datetime.time(22, 0)),
]

# 紀錄每天哪些時段已經執行過
executed_today = set()
last_checked_date = datetime.date.today()

def get_current_slot():
    """根據現在時間回傳目前屬於哪個時段（若無則回傳 None）"""
    now = datetime.datetime.now().time()
    for idx, (start, end) in enumerate(time_slots):
        if start <= now < end:
            return idx
    return None

def run_script(script_path):
    print(f"[開始執行] {script_path} 時間：{datetime.datetime.now()}")
    try:
        subprocess.run([sys.executable, script_path], check=True)
        print(f"[執行完成] 時間：{datetime.datetime.now()}")
    except subprocess.CalledProcessError as e:
        print(f"[錯誤] 執行失敗：{e}")

def run_script_by_schedule():
    global executed_today, last_checked_date
    script_path = "./爬蟲程式.py"

    while True:
        now = datetime.datetime.now()
        today = now.date()

        # 若跨天則重置已執行記錄
        if today != last_checked_date:
            executed_today.clear()
            last_checked_date = today
            print(f"[跨天] 清除已執行記錄 - 日期：{today}")

        current_slot = get_current_slot()

        if current_slot is not None and current_slot not in executed_today:
            run_script(script_path)
            executed_today.add(current_slot)
        else:
            print(f"[等待中] 現在時間：{now}，未進入執行時段或已執行。\n")

        time.sleep(60)  # 每分鐘檢查一次

if __name__ == "__main__":
    run_script_by_schedule()

