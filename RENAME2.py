#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import xml.etree.ElementTree as xmlTree
import pypinyin


# 读取文件名并记录
# noinspection PyGlobalUndefined
def read_files():
    # 获取当前目录
    path = os.getcwd()
    # 把当前文件夹下所有文件名存入一个list
    file_list = os.listdir(path)
    # 遍历输出每一个文件的名字和类型
    for file_name in file_list:
        """
        过滤出来需要的文件类型，XML 和 PNG 
        找出文件夹里面xml文件名并记录；
        png 同理，并仅筛选包含中文字符的文件名
        """
        # 输出指定后缀类型的文件
        if file_name.endswith('.xml'):
            if file_name.startswith('appfilter_'):
                xml_list.update({"appfilter": file_name})
            if file_name.startswith('appmap_'):
                xml_list.update({"appmap": file_name})
            if file_name.startswith('theme_resources'):
                xml_list.update({"theme_res": file_name})
        # 输出指定后缀类型的文件
        if file_name.endswith('.png'):
            # 不要扩展名
            f_name = os.path.splitext(file_name)[0]
            # 判断是否包含中文字符
            if bool(is_chinese(f_name)):
                # 转换成Pinyin
                py = get_pinyin(f_name)
                # 存入一个字典（同时保留原文件名）{"中文"： "zhongwen"}
                chinese_list.update({f_name: py})
    print(str(len(chinese_list)) + " files")


# 转换为Pinyin的方法
def get_pinyin(string):
    pinyin = pypinyin.slug(string, separator="")
    return pinyin


# 修改文件名方法（弃用）
def re_file(string):
    for f in string:
        os.renames(f + '.png', string[f] + '.png')
    print("Renamed")


# 修改xml
def re_xml(string):
    # 从保存的字典中读取所需要的xml树
    app_filter = string.get("appfilter")
    # 小bug修复 当没有修改或替换对象时 Pass
    if app_filter is None:
        pass
    else:
        app_filter_tree = xmlTree.parse(app_filter)
        app_filter_root = app_filter_tree.getroot()
        count = 0
        # 遍历所需要替换的元素属性值
        for item in app_filter_root.findall("item"):
            v = item.get("drawable")
            if bool(is_chinese(v)):
                # 这里改了思路 直接转换了 不需要依照字典的记录替换
                py = get_pinyin(v)
                item.set("drawable", py)
                count = count + 1
        print(str(count) + " changes from appfilter ")
        app_filter_tree.write(app_filter, encoding="utf-8", xml_declaration=True)

    app_map = string.get("appmap")
    if app_map is None:
        pass
    else:
        app_map_tree = xmlTree.parse(app_map)
        app_map_root = app_map_tree.getroot()
        count = 0
        for item in app_map_root.findall("item"):
            v = item.get("name")
            if bool(is_chinese(v)):
                py = get_pinyin(v)
                item.set("name", py)
                count = + 1
        print(str(count) + " changes from appmap ")
        app_map_tree.write(app_map, encoding="utf-8", xml_declaration=True)

    theme_res = string.get("theme_res")
    if theme_res is None:
        pass
    else:
        theme_res_tree = xmlTree.parse(theme_res)
        theme_res_root = theme_res_tree.getroot()
        count = 0
        for item in theme_res_root.findall("AppIcon"):
            v = item.get("image")
            if bool(is_chinese(v)):
                py = get_pinyin(v)
                item.set("image", py)
                count = count + 1
        print(str(count) + " changes from theme_res ")
        theme_res_tree.write(theme_res, encoding="utf-8", xml_declaration=True)
        # print("XML file has been Changed!")


# 判断是否包含中文
def is_chinese(string):
    check_str = string
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False


# 把文件名记录输出到txt 以供检查对照
def output_txt(dict_temp):
    if chinese_list is None:
        # print(chinese_list)
        file = open('Changed.txt', 'w', encoding='utf-8')
        # 遍历字典的元素，将每项元素的key和value分拆组成字符串，注意添加分隔符和换行符
        for k, v in dict_temp.items():
            file.write(str(k) + ' ' + str(v) + '\n')
        file.close()
        print("TXT File Exported")


# 创建空字典用来存储文件名
chinese_list = {}
# 创建空字典用来获取xml的文件名
xml_list = {}

# 读取目录
read_files()
if len(chinese_list) != 0:
    # 重命名xml
    re_xml(xml_list)
    # 输出 txt
    output_txt(chinese_list)
else:
    print("No File Changed")

input("Press Enter Key EXIT")
