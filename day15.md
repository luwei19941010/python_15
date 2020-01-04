### day15

#### 今日内容

- 模块知识
- 内置模块
  - time
  - datetime
  - json
  - 其他

#### 内容回顾&补充

- 构造字典和函数对应关系，避免使用过多的if else：
- a=1,b=2 ----> a,b=b,a+b
- 装饰器
- 找文件路径
- 脚本参数
- sys.exit
- range/xrange
- 读大文件



#### 详细内容

##### 1.模块基本知识

- 模块

  - 内置模块

  - ```
    import sys
    sys.argv
    ```

  - 第三方模块，下载/安装

  ```
  pip install XXX
  ```

  

  - 自定义模块

    - xxx.py

    ```
    def f1():
    	print('f1')
    def f2():
    	print('f2')
    ```

    - x1.py

    ```
    import xxx
    xxx.f1()
    xxx.f2()
    ```

  

  

##### 2.os模块

- os.path.jion(a,b) ，文件目录拼接
- os.path.dirname ，上级目录
- os.path.abspath，绝对路径
- os.path.exists，路径是否存在
- os.stat().st_size，文件大小
- os.listdir，当前文件夹下文件及文件夹（单层）
- os.walk，当前文件夹下所有的文件及文件夹（多层）
- os.makedirs，创建多级目录

```
import os
path=r'new_forder/a/b/c'
os.makedirs(path)

应用：
'''
import os
path=r'new_forder/a/b/c/txt.txt'
file=os.path.dirname(path)
if not os.path.exists(file):
    os.makedirs(file)
with open(path,mode='w',encoding='utf-8') as f:
    f.write('asdasdasd')
'''
```

- os.mkdir ,创建一级目录

```
import os
path=r'new_forder'
os.mkdir(path)
```

- os.rename(a,b) ,重命名

```
import os
path=r'new_forder/a/b/c'
os.rename('new_forder','cc')
```

##### 3.sys模块

- sys.argv
- sys.path,默认python 导入模块时，会按照sys.path中的路径去挨个查找

```
sys.path.append(r'D:\\') 
import ACI
```

- sys是解释器相关的数据，递归次数，引用次数

##### 4.json

json是一个特殊的字符串。【长得类似列表/字典/字符串/数字/真假】

json基本:

- 只允许存在 int 、str、list、dict、bool，不存在set（），tuple
- 最外层只能是list 或者dict
- 最外层只能是list 或者dict
- json中如果包含str 必须是双引号“ ”。

```
序列化，将python的值转换为json格式的字符串
import json
v=['asd',12,34,5,{'k1':1},True,'asdasd',['asd',12,3]]
v1=json.dumps(v)
print(v1)

反序列化，将json的值转换为python格式的数据类型
v2='["asd", 12, 34, 5, {"k1": 1}, true, "asdasd", ["asd", 12, 3]]'
v3=json.loads(v2)
print(v3)
```

![image-20200104150821243](C:\Users\davidlu\AppData\Roaming\Typora\typora-user-images\image-20200104150821243.png)

















