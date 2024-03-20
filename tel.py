# 問題:辞書の作成

# 1 佐藤さんの内線番号が9968に変更になりました。辞書に反映させ
# ましょう。
# 2 山本さんが入社しました。内線番号は3651です。辞書に反映させ
# ましょう。
# 3 高橋さんが退職しました。辞書から削除しましょう。
# 4 辞書を表示してみましょう。

tel = {'佐藤':1485,'高橋':2268,'木村':8978,'山田':4121,'斉藤':8774,'鈴木':9912}

tel['佐藤'] = 9968
tel['山本'] = 3651
tel.pop('高橋')
print(tel)

# 辞書のキー・値をリスト化する
tel_key = list(tel.keys())
print(tel_key)
tel_values = list(tel.values())
print(tel_values)
# 辞書のキー・値でソートする
tel_key = sorted(tel.keys())
print(tel_key)
tel_values = sorted(tel.values())
print(tel_values)