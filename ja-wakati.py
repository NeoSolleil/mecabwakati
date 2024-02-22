import MeCab

# MeCabのインスタンスを作成
wakati = MeCab.Tagger('-Owakati')

# 形態素解析を実行し、結果を取得
result = wakati.parse(PATH/txt)

# 解析結果を表示
print(result)
