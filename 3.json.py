#-*-coding:utf-8-*-
# Author:Lu Wei
import json
v=['asd',12,34,5,{'k1':1},True,'asdasd',['asd',12,3]]
v1=json.dumps(v)
print(v1)

v2='["asd", 12, 34, 5, {"k1": 1}, true, "asdasd", ["asd", 12, 3]]'
v3=json.loads(v2)
print(v3)