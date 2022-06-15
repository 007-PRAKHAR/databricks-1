# Databricks notebook source
import pandas as pd
from cryptography.fernet import Fernet
lst = ['this', 'is', 'sample', 'code']
key = Fernet.generate_key()
f = Fernet(key)
encryptedlist = []
for item in lst:
    token = f.encrypt(bytes(item,'utf-8'))
    encryptedlist.append(token)
df = pd.DataFrame(encryptedlist)