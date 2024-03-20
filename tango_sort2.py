tango = input('英単語をスペース区切りで入力してください→')

tango_list = tango.split(' ')

tango_list.sort

for val in tango_list:
    print(val)
    print('-'*10)