# 匹配包含中文png
# 判断匹配xml

# get 中文名（包含
# 转换为拼音 保存
# 替换文件名 和 xml


"""
先获取包含中文字的文件名
保存为 中文list

然后修改为 新的 拼音list

根据 中文list 逐一匹配文件名 重命名为 拼音list中的名

创建 字典
获取中文名文件名称
转换为 pinyin
加入字典集
{"中文名":"zhongwenming"}
然后根据 key 匹配 PNG、xml（里面）
替换为 value

"""
import os
import sys
import xml.etree.ElementTree as XE

from xpinyin import Pinyin


def read_files():
    # 获取当前目录
    #
    path = os.getcwd()
    file_list = os.listdir(path)

    # 遍历输出每一个文件的名字和类型
    for file_name in file_list:
        # 输出指定后缀类型的文件
        if file_name.endswith('.xml'):
            if file_name.startswith('appfilter_'):
                xml_list.update({"appfilter": file_name})
            if file_name.startswith('appmap_'):
                xml_list.update({"appmap": file_name})
            if file_name.startswith('theme_resources'):
                xml_list.update({"theme_res": file_name})

        if file_name.endswith('.png'):
            # 不要扩展名
            f_name = os.path.splitext(file_name)[0]
            # is_chinese(f_name)
            if bool(is_chinese(f_name)):
                # print('true')
                p = Pinyin()
                py = p.get_pinyin(f_name, '')
                chinese_list.update({f_name: py})
    # print(file_list)
    # return file_list

# def convert_pinyin(string):
#
#     piny = string.get_pinyin(string, '')
#     return piny


# 修改文件名
def re_file(string):
    for f in string:
        os.renames(f+'.png', string[f]+'.png')
        # if f.startswith('a_'):
        print(string[f])


def re_xml(string):
    app_filter = string.get("appfilter")
    # print(app_filter)
    app_filter_tree = XE.parse(app_filter)
    app_filter_root = app_filter_tree.getroot()
    # items = root.findall("item")

    for item in app_filter_root.findall("item"):
        v = item.get("drawable")
        if bool(is_chinese(v)):
            p = Pinyin()
            py = p.get_pinyin(v, '')
            item.set("drawable", py)
    app_filter_tree.write(app_filter)

    app_map = string.get("appmap")
    app_map_tree = XE.parse(app_map)
    app_map_root = app_map_tree.getroot()
    for item in app_map_root.findall("item"):
        v = item.get("name")
        if bool(is_chinese(v)):
            p = Pinyin()
            py = p.get_pinyin(v, '')
            item.set("name", py)
    app_map_tree.write(app_map)

    theme_res = string.get("theme_res")
    theme_res_tree = XE.parse(theme_res)
    theme_res_root = theme_res_tree.getroot()
    for item in theme_res_root.findall("AppIcon"):
        v = item.get("image")
        if bool(is_chinese(v)):
            p = Pinyin()
            py = p.get_pinyin(v, '')
            item.set("image", py)
    theme_res_tree.write(theme_res)


# 判断是否包含中文
def is_chinese(string):
    check_str = string
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False


def output_txt(dict_temp):
    file = open('dict.txt', 'w', encoding='utf-8')
    # 遍历字典的元素，将每项元素的key和value分拆组成字符串，注意添加分隔符和换行符
    for k, v in dict_temp.items():
        file.write(str(k) + ' ' + str(v) + '\n')
    file.close()


# 创建空字典用来存储文件名
chinese_list = {}
# 获取xml的文件名
xml_list = {}

# 读取目录
read_files()
# 重命名xml
re_xml(xml_list)
# 输出 txt
output_txt(chinese_list)


