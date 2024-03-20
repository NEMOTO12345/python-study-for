# • 英単語をスペース区切りで入力させる
# • 昇順に並び替え
# • 画面に出力する
# • その際に区切りにハイフン10個を入れる




tango = input('英単語をスペース区切りで入力してください→')

tango_list = tango.split(' ')

tango_list.sort

for val in tango_list:
    print(val)
    print('-'*10)