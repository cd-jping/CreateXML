#!/usr/bin/python
# -*- coding: utf-8 -*-
import xml.dom.minidom
import os
import sys

# 创建一个空数组用来存匹配的文件名
png_list = []


def read_files():
    # 获取当前目录

    path = sys.path[0]
    file_list = os.listdir(path)

    # 遍历输出每一个文件的名字和类型
    for file_name in file_list:
        # 输出指定后缀类型的文件
        if file_name.endswith('.jpg'):
            # 不要扩展名
            f_name = os.path.splitext(file_name)[0]
            png_list.append(f_name)
            # print(item)


def create_drawable(file_list):
    files = file_list
    # 创建文档在内存中
    xml_drawable = xml.dom.minidom.Document()
    # 创建元素
    resources = xml_drawable.createElement('resources')
    # 将元素添加的文档中
    xml_drawable.appendChild(resources)
    # fileList = [{'name':'wechat'},
    #             {'name':'qq'},
    #             {'name':'weibo'},
    #             {'name':'bilibili'},
    #             {'name':'alipay'}]
    for i in files:
        item = xml_drawable.createElement('item')
        item.setAttribute('drawable', str(i))
        resources.appendChild(item)

    fp = open('testdrawable.xml', 'w' )
    xml_drawable.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding='utf-8')


def create_icon_pack(file_list):
    files = file_list
    # 创建文档在内存中
    xml_iconpack = xml.dom.minidom.Document()
    # 创建元素
    resources = xml_iconpack.createElement('resources')
    # 将元素添加的文档中
    xml_iconpack.appendChild(resources)
    for i in files:
        item = xml_iconpack.createElement('item')
        item.appendChild(xml_iconpack.createTextNode(str(i)))
        resources.appendChild(item)

    fp = open('testiconpack.xml', 'w')
    xml_iconpack.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding='utf-8')


# 读取文件列表
read_files()
# 生成drawable.xml
create_drawable(png_list)
# 生成icon_pack.xml
create_icon_pack(png_list)
