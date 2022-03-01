import random

ans = random.randint(1,100)
num = int(input("請輸入1~100任意一個整數"))
min = 1
max = 100

while ans != num:
    if num < ans:
            min = num
            print("請輸入" + str(min) + " ~ " + str(max) + "任意一個整數")
    elif num > ans:
        max = num
        print("請輸入" + str(min) + " ~ " + str(max) + "任意一個整數")
    else:
        print("請輸入整數!!!")

    num = int(input())

print("恭喜猜對了!!!")
