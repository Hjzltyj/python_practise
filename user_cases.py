#!/usr/bin/env python

# 存储一个人名，并在其开头和结尾都包含一些空白字符，务必至少使用字符组合"\t"和"\n"各一次

user_name = " \nHuang\t jizong\n  "

print(user_name)
print(user_name.lstrip())
print(user_name.rstrip())
print(user_name.strip())