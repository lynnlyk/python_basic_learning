from src import pk01

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
            
        - import package.module
            - 导入包中某个具体的模块
            - 使用方法
                
                package.module.func_name
                package.module.class.func()
                package.module.class.var
                
        - import package.module as pm
        
        - from ... import 导入
            - from package import module1, module2, ...
            - 此种导入方法不执行"__init__"的内容
            
            from pk01 import py01
            py01.sayHello()
            
        - from package import *
            - 导入当前包"__init__.py"文件中所有的函数和类
            - 使用方法
                func_name()
                class_name.func_name()
                class_name.var
                
        - from package.mudule import *
            - 导入包中指定的模块的所有内容
            - 使用方法
                func_name()
                class_name.func_name()
                
        - 在开发环境中经常会使用其他模块，可以在当前包中直接导入其他模块中的内容
            - import 完整包或者模块的路径
            
        "__all__"的用法
            - 在使用from package import * 的时候，* 可以导入的内容
            - "__init__.py" 中如果文件为空，或者没有"__all__"，那么只可以把"__init__"中的内容导入
            - "__init__.py" 中设置了"__all__"的值，那么则按照"__all__"指定的子包或者模块进行加载，如此则不会载入"__inti__"中的内容
            - "__all__=['module1', 'module2', 'package1', ...]
        
        # 命名空间
            - 用于区分不同位置不同功能但相同名称的函数或者变量的一个特定前缀
            - 作用是防止命名冲突
                
                setName()
                Student.setName()
                Dog.setName()         
'''

ini = pk01.inInit()





