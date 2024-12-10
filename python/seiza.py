import random
import time
import tkinter as tk
from PIL import Image, ImageTk
import os

def omikuji_animation(window, result):
    # アニメーション部分
    message_label = tk.Label(window, text="おみくじを引いています...", font=("Arial", 30, "bold"), fg="#309419", bg="#f9fcae")
    message_label.pack(pady=50)

    dots = ['.', '..', '...']
    for i in range(5):  # 5回アニメーションを表示
        for dot in dots:
            message_label.config(text=f"おみくじを引いています{dot}")
            window.update()
            time.sleep(0.5)

    # 結果を表示
    message_label.config(text=f"おみくじの結果は: {result}", font=("Arial", 40, "bold"), fg="#309419", bg="#f9fcae")
    window.update()

def display_zodiac_result(zodiac, window):
    # 星座占いの結果を辞書で定義
    zodiac_results = {
        "牡羊座": "今日の運勢は非常に良好！積極的な行動が吉。",
        "牡牛座": "慎重に行動することで成功をつかめる日。",
        "双子座": "コミュニケーションが重要。新しい出会いのチャンス。",
        "蟹座": "家庭や身近な人との関係が運気を左右します。",
        "獅子座": "自信を持って行動すると、運勢が味方してくれる。",
        "乙女座": "計画的に進めることで、大きな成果を得られる日。",
        "天秤座": "バランスを大切に。周囲との調和が重要。",
        "蠍座": "直感が冴える時。思い切って行動してみましょう。",
        "射手座": "冒険心を大切に。新しい経験があなたを成長させる。",
        "山羊座": "実利的な視点で動くと、安定した結果を得られる。",
        "水瓶座": "自由な発想が鍵。創造的なアイデアが浮かびやすい。",
        "魚座": "柔軟に対応することで、運勢が開けていく日。"
    }

    # 結果をウィンドウに表示
    result_text = zodiac_results.get(zodiac, "選ばれた星座の運勢が見つかりません。")
    result_label = tk.Label(window, text=f"{zodiac}の運勢:\n{result_text}", font=("Arial", 20, "bold"), fg="black", bg="#f9fcae")
    result_label.pack(pady=10)

def omikuji():
    # おみくじの結果とそのメッセージを辞書で定義
    results = {
        "大吉": {
            "運勢": "素晴らしい運勢です！今後の一歩が幸運を呼び込みます。",
            "恋愛運": [
                "恋愛運は絶好調です！素敵な出会いが期待できます。",
                "恋愛運は最高です。心を開いて、積極的にコミュニケーションを取ってみましょう。",
                "恋愛面では驚くような幸運が訪れるかもしれません。思い切ってアプローチしてみて！"
            ],
            "金運": [
                "金運も非常に良いです！新しい投資やビジネスが成功する可能性があります。",
                "金運に恵まれ、予想外の収入があるかも！お金に関する決断は慎重に。",
                "金運が大きく開ける兆しです。無駄遣いせず、大切なことに使いましょう。"
            ]
        },
    }

    # ランダムにおみくじの結果を選ぶ
    result = random.choice(list(results.keys()))

    # Tkinterウィンドウを作成
    root = tk.Tk()
    root.title("おみくじと星座占い")
    root.geometry("1450x700")  # ウィンドウサイズを指定
    root.config(bg="#f9fcae")

    # おみくじのアニメーションを実行
    omikuji_animation(root, result)

    # 星座占い機能の追加
    zodiac_label = tk.Label(root, text="自分の星座を選んでください:", font=("Arial", 20, "bold"), bg="#f9fcae")
    zodiac_label.pack(pady=10)

    zodiac_options = ["牡羊座", "牡牛座", "双子座", "蟹座", "獅子座", "乙女座", "天秤座", "蠍座", "射手座", "山羊座", "水瓶座", "魚座"]
    zodiac_var = tk.StringVar()
    zodiac_var.set(zodiac_options[0])  # デフォルト値

    zodiac_dropdown = tk.OptionMenu(root, zodiac_var, *zodiac_options)
    zodiac_dropdown.config(font=("Arial", 15))
    zodiac_dropdown.pack(pady=10)

    zodiac_button = tk.Button(root, text="星座運勢を表示", font=("Arial", 20), 
                              command=lambda: display_zodiac_result(zodiac_var.get(), root))
    zodiac_button.pack(pady=20)

    root.mainloop()

# 実行
omikuji()
