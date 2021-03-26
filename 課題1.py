import pandas as pd
#検索するための関数の定義
def search():
    df_csv = pd.read_csv("list.csv")
    Source=list(df_csv)
    
    while True:
        word = input('鬼滅の刃登場人物名を入力して下さい>>>')
        if word in Source:
            print('{}が見つかりました'.format(word))
        else:
            print('{}は見つかりませんでした'.format(word))
            #リストになかった場合に、キャラクターを(source)追加出来るようにする
            add = input('キャラクターを新規に登録しますか？　登録する→0　登録しない→1>>>')
            if add == '0':
                Source.append(word)
                print('キャラクターを追加しました')
                #CSVへの書き込みコード入力]
            else:
                print('追加しませんでした')

        df_csv=pd.DataFrame(Source,columns=["name"])
        df_csv.to_csv("list.csv",encoding = 'UTF-8-sig')
        print(Source)

if __name__ == "__main__":
    search()