# convert_python_files_utf-8
下载别人模型的时候python文件总是ASCII格式的，当自己想中文注释的时候每次都要在文件首行添加# -*- coding: utf-8 -*-  特别麻烦，于是设计这个插件可以一次运行将所有python首行加上# -*- coding: utf-8 -*-

使用方法是将该脚本（也是python文件）放在模型根目录下，也就是README.md所在目录下，然后运行一下即可

警告声明：
若python文件内容过多可能会导致不可预知情况，由于是使用f.read()直接读取原文件内容，所以不确定过长文件是否会导致原有代码缺失，慎用
