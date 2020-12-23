#[hangman]

#以下はモジュールのインポートを行う
import getpass,time


#以下は関数の定義を行う

#隠された単語を変更する関数
def change_answer():
    answer=getpass.getpass("英単語を入力してね\n入力してもここには単語は表示されないよ：")
    with open("answer.txt","w",encoding="utf-8")as f:
        f.write(answer)
        f.close()


#隠された単語を取得する関数
def get_answer():
    with open("answer.txt", mode="r",encoding="utf-8") as f:
        answer=f.read()
        str(answer)
        return(answer)


#ハングマンを動かす関数
def hangman(answer):
    wrong=0
    draw=["",
          "________________",
          "|               ",
          "|        |      ",
          "|        0      ",
          "|       /|-     ",
          "|       / )     ",
          "|               "]
    letters_left=list(answer)
    board=["_"]*len(answer)
    win=False
    print("隠された単語を一文字ずつ予想しよう\n間違えるたびに、吊られた人（ハングマン）の絵が少しずつ完成していくよ\n絵が完成する前に正解にたどり着こう")
    while wrong<len(draw):
        print("\n今わかっている文字は以下の通り")
        print(board)
        gues=input("隠された単語の一文字を予想しよう：")
        if gues in letters_left:
            board[letters_left.index(gues)]=gues
            letters_left[letters_left.index(gues)]="$"
            print("\n正解だよっ!")
            if "_" in board:
                continue
            else:
                win=True
                break
        else:
            wrong=wrong+1
            print("\nその文字は含まれていないよ～")
            if wrong==len(draw):
                win=False
                break
            for i in range(0,wrong+1):
                print(draw[i])
    if win==False:
        print("\n吊られた人（ハングマン）の絵が完成しちゃったから、君の負けだよん")
    if win==True:
        print("\n君の勝ちだよ!!おめでとう!!")



#以下に全体の挙動を記述する
print("\nハングマンへようこそ!!\n")
while True:
    mode=input("モードを選んでね\n隠された単語を変更する場合は1を、ハングマンを遊ぶ場合は2を、終了する場合は3を入力するよ\nゲームを始めると、1ゲームが終わるまで終了できないから注意してね：")
    if mode=="1":
        print("\n隠された単語を変更するよ")
        change_answer()
        print("\n隠された英単語を変更したよ\n")
        continue
    if mode=="2":
        print("\nハングマンを始めるよ\n")
        hangman(get_answer())
        print("\nゲームを終了してモード選択に戻るよ\n")
        continue
    if mode=="3":
        print("\n3秒後に終了するよ\n遊んでくれてどうもありがとう!!\n")
        time.sleep(3)
        break
    else:
        print("\nそのキーに割り当てられたモードは無いよ～\n")
        continue
