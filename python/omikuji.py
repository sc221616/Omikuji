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
        "中吉": {
            "運勢": "安定した運勢。計画を立てて行動することで成功をつかめます。",
            "恋愛運": [
                "穏やかな恋愛運。焦らず時間をかけて関係を深めましょう。",
                "小さな勇気が恋愛に進展をもたらします。",
                "恋愛面では、お互いの気持ちを大切にすることが重要です。"
            ],
            "金運": [
                "金運は堅実。無駄遣いを避けて貯蓄に励むと吉。",
                "お金に関するトラブルを避けるため計画的に動きましょう。",
                "小さな成功が積み重なる兆しです。"
            ]
        },
        "吉": {
            "運勢": "まずまずの運勢。積極的に動けば良い結果が得られるでしょう。",
            "恋愛運": [
                "恋愛運は安定。急がず焦らず自然体で。",
                "新たな出会いが期待できますが、慎重に。",
                "進展がゆっくりと訪れる予感。焦らないことが大切です。"
            ],
            "金運": [
                "金運は平均的。堅実な運用が鍵。",
                "欲を出さずに地道な努力を続けることが重要です。",
                "節約が実を結びそうな運勢です。"
            ]
        },
        "凶": {
            "運勢": "注意が必要な運勢。冷静な判断が求められます。",
            "恋愛運": [
                "恋愛面では相手を思いやることが大切です。",
                "恋愛運が低迷。自己改善に時間を使いましょう。",
                "無理に進展を求めるより、現状を維持するのが吉。"
            ],
            "金運": [
                "お金に関するミスに注意。大きな買い物は控えましょう。",
                "計画外の出費がありそう。節約を心がけて。",
                "予期せぬ出費に備えてお金を蓄えておくと安心です。"
            ]
        }
    }

    # ランダムにおみくじの結果を選ぶ
    result = random.choice(list(results.keys()))

    # Tkinterウィンドウを作成
    root = tk.Tk()
    root.title("おみくじ")
    root.geometry("1450x700")  # ウィンドウサイズを指定

    # 背景色をクリーム色に変更
    root.config(bg="#f9fcae")

    # おみくじのアニメーションを実行
    omikuji_animation(root, result)

    # スクリプトが存在するディレクトリを基準に画像フォルダを指定
    base_dir = os.path.dirname(__file__)
    images_dir = os.path.join(base_dir, "images")  # "images" フォルダ
    icon_path_1 = os.path.join(images_dir, "もみじ②.png")  # もみじの画像
    icon_path_2 = os.path.join(images_dir, "syougatsu2_omijikuji2.png")  # おみくじの画像

    try:
        # 最初のイラスト（もみじ）
        icon_1 = Image.open(icon_path_1)
        icon_1 = icon_1.resize((100, 100))  # 画像サイズを調整
        icon_image_1 = ImageTk.PhotoImage(icon_1)

        # 2つ目のイラスト（おみくじ）
        icon_2 = Image.open(icon_path_2)
        icon_2 = icon_2.resize((100, 100))  # 画像サイズを調整
        icon_image_2 = ImageTk.PhotoImage(icon_2)

        # 結果と画像を配置するためのFrameを使用
        frame = tk.Frame(root, bg="#f9fcae")
        frame.pack(pady=30)

        # 結果のテキストを表示するLabel
        result_text = f"運勢: {results[result]['運勢']}\n\n恋愛運: {random.choice(results[result]['恋愛運'])}\n\n金運: {random.choice(results[result]['金運'])}"
        result_label = tk.Label(frame, text=result_text, font=("Arial", 20, "bold"), fg="black", bg="#f9fcae", justify="left")
        result_label.pack(side="left", padx=10)

        # 最初のアイコン画像（もみじ）を表示するLabel
        image_label_1 = tk.Label(frame, image=icon_image_1, bg="#f9fcae")
        image_label_1.pack(side="right")

        # 2つ目のアイコン画像（門松）を画面の左上に配置
        image_label_2 = tk.Label(root, image=icon_image_2, bg="#f9fcae")
        image_label_2.place(x=300, y=25)

        # 画像参照を保持
        result_label.image = icon_image_1
        image_label_1.image = icon_image_1
        image_label_2.image = icon_image_2

    except Exception as e:
        print(f"画像の読み込みに失敗しました: {e}")

    root.mainloop()

# おみくじを引く
omikuji()
