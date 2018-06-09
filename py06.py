import pk01

'''
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
                
        - import package_name as p
            - 此种方法是默认对__init__.py内容的导入
                
'''

ini = pk01.inInit()





