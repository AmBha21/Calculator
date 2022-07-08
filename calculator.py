#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: AmBha
Calculator
"""
while True:
    num1=input("Please input your first number: ")
    if num1.isdigit()==True:
        int_num1=int(num1)
        break
    continue
while True:
    num2=input("Please input your second number: ")
    if num2.isdigit()==True:
        int_num2=int(num2)
        break
    continue    

while True:
    operation=input("Please select an operation: * / - +: ")
    if operation not in ["*", "/", "-", "+"]:
        continue
    break

# print (int_num1)
# print(int_num2)
if operation=="*":
    print (int_num1*int_num2)
if operation=="/":
    print (int_num1/int_num2)
if operation=="-":
    print (int_num1-int_num2)
if operation=="+":
    print (int_num1+int_num2)




