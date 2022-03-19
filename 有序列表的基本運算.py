# 有序可變動列表List
grades = [12,60,15,70,90]
print(grades) # 取得列表內所有資料
print(grades[0]) # 取得列表中索引值為0的資料(12)
print(grades[3]) # 取得列表中索引值為3的資料(70)
grades[0] = 55 # 將索引值0的位置換成55
print(grades)
print(grades[1:4]) # 取得索引值1~3 不包含尾數
grades[1:4] = [] # 連續刪除列表中索引1~4 的資料(但不包含4)
print(grades)
grades = grades + [12,33] # 在原本的列表中加入12和33
print(grades)

data = [12,24,55,62,98]
print(len(data)) #取得列標中的長度 len(列表資料)

number = [[12,5,66],[78,33,94]]
print(number[0][1]) # 取得列表第1層 第1個的資料
print(number[0][0:2])  # 取得列表第1層 第1個到第3個資料(不包含尾數)個資料
number[0][0:2] = [2,3] # 將列表第1層 第1個到第3個資料(不包含尾數) 換成[2,3]
print(number)





# 有序不可變動列表Tuple
Tuple_ = (3,4,5)
print(Tuple_[2]) # 取得列表中索引值2的資料
print(Tuple_[0:2]) #取得列表中索引值0到2的資料 但不包含結尾
Tuple_[0] = 5 # 報錯 Tuple的資料不可變動

#除了不可變動外 Tuple其餘地方與List一致