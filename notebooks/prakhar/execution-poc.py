# Databricks notebook source
def isPalindrome(s):
    return s == s[::-1]

list1 = ['nayan','suraj','malayalam','navin']
for item in list1:
    ans = isPalindrome(item)
    if ans:
        print(f"{item} is palindrome")
    else:
        print(f"{item} is not palindrome")
        
