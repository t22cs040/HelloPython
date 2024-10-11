import random

def judge_rps(A, B):
    if A == B:
        return "引き分け"
    elif (A + 1) % 3 == B:  # Aの手がBに勝つ条件
        return "Aの勝ち"
    else:
        return "Bの勝ち"

dict_choices = {0: "グー", 1: "チョキ", 2: "パー"}

countA = 0
countAB = 0

for i in range(3):
    key1 = random.randint(0, 2)
    key2 = random.randint(0, 2)
    result = judge_rps(key1, key2)
    print(f"Aの手：{dict_choices[key1]} v.s. Bの手：{dict_choices[key2]} -> {result}")
    
    if result == "引き分け":
        countAB += 1
    elif result == "Aの勝ち":
        countA += 1

if countAB == 3 or (countAB == 1 and countA == 1):
    print("最終結果：引き分け")
elif countA >= 2 or (countAB == 2 and countA == 1):
    print("最終結果：Aの勝ち")
else:
    print("最終結果：Bの勝ち")
