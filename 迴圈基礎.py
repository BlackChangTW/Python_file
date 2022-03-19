# while 迴圈基本語法

# while 布林值:
#    若布林值為True 執行命令 
#    回到上方 做下一次迴圈判斷

n = 1
while n <= 5 :
    print("n的值是 : " ,n)
    n += 1

 #while True 無窮迴圈
  
#for 迴圈基本語法
#for 變數名稱 in 列表或字串:
#   將列表中的項目或字串中的字
#   元 逐一取出 逐一處理

for i in [4,1,2] :
    print("逐一取得列表中資料 : " ,i)
for i in "Hello" :
    print("逐一取得字串中的字元" ,i)
#在for迴圈中使用range()
#for 變數名稱 in range(結束值): (從0開始 不包括結束值)
#for 變數名稱 in range(起始值,結束值): (印出結果包括起始值 不包括結束值)