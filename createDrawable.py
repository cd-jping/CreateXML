import xml.dom.minidom
 # <resources>
 #    <item drawable="email"/>

# 创建文档在内存中
xmlFile = xml.dom.minidom.Document()
# 创建元素
resources = xmlFile.createElement('resources')

# 将元素添加的文档中
xmlFile.appendChild(resources)
# fileList = [{'name':'wechat'},
#             {'name':'qq'},
#             {'name':'weibo'},
#             {'name':'bilibili'},
#             {'name':'alipay'}]

fileList = ['wechat',
            'qq',
            'weibo',
            'bilibili',
            'alipay']


for i in fileList :
    item = xmlFile.createElement('item')
    item.setAttribute('drawable',str(i))
    resources.appendChild(item)

fp = open('testdrawable.xml','w')
xmlFile.writexml(fp,indent='\t',addindent='\t',newl='\n',encoding='utf-8')

