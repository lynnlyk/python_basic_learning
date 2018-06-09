import py01

# 若果模块名称直接以数字开头，需要借助importlib帮助
# import importlib
# tuling = importlib.import_module("01")

# 导入同时给模块起别名
# import import importlib as ssss

# form module_name import func_name, class_name

stu = py01.Student("xiaojing", 20)

stu.say()

py01.sayHello()