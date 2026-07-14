# 錯誤與例外的處理
try:
    num = int(input("請輸入一組數字"))
    result = 10 / num
except ValueError as e:
    result = f"輸入了無效的數字，{e}"
except ZeroDivisionError as e:
    result = f"被除數不能是零，{e}"
except:
    result = "有錯誤發生"
else:
    print("完全沒錯誤發生才會進入的區間")
finally:
    print("不對對錯都會進入的區間")

print(f"結果是: {result}")