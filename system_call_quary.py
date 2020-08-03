import os
import prettytable as pt
title1='''

      _________               __                                 .__  .__
     /   _____/__.__. _______/  |_  ____   _____     ____ _____  |  | |  |
     \_____  <   |  |/  ___/\   __\/ __ \ /     \  _/ ___\\__  \ |  | |  |
     /        \___  |\___ \  |  | \  ___/|  Y Y  \ \  \___ / __ \|  |_|  |__
    /_______  / ____/____  > |__|  \___  >__|_|  /  \___  >____  /____/____/
            \/\/         \/            \/      \/       \/     \/
    
'''
print(title1)
result_32=""
result_64=""
call_table = pt.PrettyTable()
call_table.field_names = ["32位", "64位"]

num=int(eval(input("请输入系统调用号:")))
f_32 = open("32")
while True:
    data = f_32.readline()
    if not data:
        result_32="NULL"
        break
    data = data.strip('\n')
    index=data.find('#')
    nums=int(data[index+2:])
    if num==nums:
        result_32=data[:index]
        break
f_32.close()
f_64 = open("64")
while True:
    data = f_64.readline()
    if not data:
        result_64="NULL"
        break
    data = data.strip('\n')
    index=data.find('#')
    nums=int(data[index+2:])
    if num==nums:
        result_64=data[:index]
        break

f_64.close()
call_table.add_row([result_32,result_64])
print("调用号"+str(num)+"的查询结果为:\n")
print(call_table)
        
