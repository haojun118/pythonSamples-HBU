# -*- coding: utf-8 -*-

#Date: 2017-2-3
#Ver: 1.0
#Author: xshg
#通过输入体重和身高，计算BMI

height = input("请输入身高(m)：")
weight = input("请输入体重(kg)：")
height = float(height)
weight = float(weight)

bmi = weight / height / height
print("你的 BMI 值为：%.0f" % bmi)

if bmi < 18.5:
    print("你体重偏轻。")
elif bmi < 25:
    print("你的体重正常。")
elif bmi < 28:
    print("你的体重超重，请控制饮食并加强运动。")
elif bmi < 32:
    print("你的体重已是肥胖，请注意减肥。")
else:
    print("你已严重肥胖，请就医。")

print('''BMI 参考：
        BMI = 体重/身高/身高
        < 18.5      过轻
        18.5 - 25   正常
        25 - 28     超重
        28 - 32     肥胖
        > 32        严重肥胖''')

