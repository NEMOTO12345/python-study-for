# • ファイル名:tango_sort3.py
# • 英単語をスペース区切りで入力させる
# • 昇順に並び替え
# (ただし大文字小文字の区別なくABC順にする)
# • 画面に出力する際は先頭大文字あとは小文字にする
# • その際に区切りにハイフン10個を入れる


tango = input('英単語をスペース区切りで入力してください→')
tango.upper()
tango.capitalize()

tango_list = tango.split(' ')

tango_list.sort()

for val in tango_list:
    print(val)
    print('-'*10)
