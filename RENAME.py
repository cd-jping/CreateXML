
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