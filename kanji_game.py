# 難読漢字をキー、読みを値にして辞書を作る。
# 辞書の中からランダムで漢字を出題。（キーをリスト化してランダムモジュールでシャッフル）
# 例「栗鼠は何と読む？」
# 3秒たったら正解を出す
# 例「正解はりす」
# 1秒たったら次の問題へ
# 問題を10回繰り返す
import random
import time
kanji = {'信天翁':'あほうどり','金糸雀':'かなりあ','軽鴨':'かるがも'}
kanji_list = list(kanji.keys())
print(kanji_list)
random.shuffle(kanji_list)


for i in kanji_list:
    print(input(f'{i}は何て読む？'))
    time.sleep(1)
    print(f'正解は{kanji[i]}。')