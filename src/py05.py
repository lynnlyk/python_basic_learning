import sys

'''
    sys.path 属性可以获取搜索路径列表
    添加搜索路径
    sys.path.append(dir)
    
    模块的加载顺序
        1. 搜索内存中已经加载好的模块
        2. 搜索python的内置模块
        3. 搜索sys.path路径
        
    包
        包是一种组织管理代码的方式，包里面存放的是模块
        用于将模块包含在一起的文件夹就是包
        自定义包的结构
        
            /--- 包
            /---/--- __init__.py
            /---/--- 模块1
            /---/--- 模块2
            /---/--- 子包（子文件夹）
            /---/---/--- __init__.py
            /---/---/--- 子模块1
            /---/---/--- 子模块2
            
    包的导入操作
        - import package_name
            - 直接导入一个包，可以使用__init__.py中的内容
            - 使用方式
            
                package_name.func_name
                package_name.class_name.func_name()
                
'''

print(type(sys.path))
print(sys.path)

for p in sys.path:
    print(p)



