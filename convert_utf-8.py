# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import os

# 每次将该文件放在模型根目录下运行，一般是README.md所在目录，或者说最外层目录

# ###########首先获取当前目录下所有文件路径，包含递归子目录下的文件
path = os.getcwd()  # 获取当前路径(模型根目录)
print "当前文件所在路径为={}".format(path)


# 获取当前目录下的所有内容
# listDir = os.listdir(path)
# for x in listDir:
#     print(x)

def recursion_dir_all_file(path):
    file_list = []
    for dir_path, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(dir_path, file)
            if "\\" in file_path:
                file_path = file_path.replace('\\', '/')
            file_list.append(file_path)
        for dir in dirs:
            file_list.extend(recursion_dir_all_file(os.path.join(dir_path, dir)))
        break  # 注意只需要让外围for循环运行第一次即可，也就是每次获得当前目录下的3元组即可，os.walk也会递归运行
    return file_list


all_files = recursion_dir_all_file(path)

# ################筛选出以.py结尾的文件名
python_files = []

print "the number of files={}".format(len(all_files))
for file in all_files:
    if file.endswith('.py'):
        python_files.append(file)
        print file

print "the number of python files={}".format(len(python_files))


# ##############将这些文件读取，并在第一行插入注释：
# -*- coding: utf-8 -*-\n

def insertFirstSentence(file):
    with open(file, 'r+')as fin:
        old = fin.read()
        fin.seek(0)
        data = "# -*- coding: utf-8 -*-\n"
        fin.write(data)
        fin.write(old)

# 先试试能否改变一个.py文件的首行
# file = 'test.py'
# with open(file, 'r+')as fin:
#     old = fin.read()
#     fin.seek(0)
#     data = "# -*- coding: utf-8 -*-\n"
#     fin.write(data)
#     fin.write(old)

for file in python_files:
    insertFirstSentence(file)
print "Done!"
