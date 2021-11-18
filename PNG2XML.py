#!/usr/bin/python
# -*- coding: utf-8 -*-

import xml.dom.minidom
import os


def read_files():
    # 获取当前目录
    path = os.getcwd()
    file_list = os.listdir(path)
    # 遍历输出每一个文件的名字和类型
    for file_name in file_list:
        # 输出指定后缀类型的文件
        if file_name.endswith('.png'):
            # 不要扩展名
            f_name = os.path.splitext(file_name)[0]
            png_list.append(f_name)

    print(str(len(png_list)) + " files")


def create_drawable(string):
    files = string
    # 创建文档在内存中
    xml_drawable = xml.dom.minidom.Document()
    # 创建元素
    resources = xml_drawable.createElement('resources')
    # 将元素添加的文档中
    xml_drawable.appendChild(resources)

    for i in files:
        item = xml_drawable.createElement('item')
        # 把列表中的文件名插入”drawable“属性中
        item.setAttribute('drawable', str(i))
        resources.appendChild(item)

    fp = open('drawable.xml', 'w', encoding='utf-8')
    xml_drawable.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding='utf-8')
    print("Drawable-XML File Exported")


def create_icon_pack(file_list):
    files = file_list
    # 创建文档在内存中
    xml_icon_pack = xml.dom.minidom.Document()
    # 创建元素
    resources = xml_icon_pack.createElement('resources')
    # 将元素添加的文档中
    xml_icon_pack.appendChild(resources)
    for i in files:
        item = xml_icon_pack.createElement('item')
        item.appendChild(xml_icon_pack.createTextNode(str(i)))
        resources.appendChild(item)

    fp = open('icon_pack.xml', 'w', encoding='utf-8')
    xml_icon_pack.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding='utf-8')
    print("ICON_PACK-XML File Exported")


# 创建一个空数组用来存匹配的文件名
png_list = []

# 读取文件列表
read_files()
if len(png_list) != 0:
    # 生成drawable.xml
    create_drawable(png_list)
    # 生成icon_pack.xml
    create_icon_pack(png_list)
else:
    print("No file to be Changed")

input("Press Enter Key EXIT")
