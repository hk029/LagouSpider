#encoding=utf-8
import jieba
import csv

jieba.load_userdict('./word.txt')
file = csv.reader(file('G://1.csv','rb'))
key = {}
print key
for line in file:
    seg_list = jieba.cut(line[2],cut_all=False) #搜索引擎模式
    for k in seg_list:
        k = k.replace(' ','')
        if k in key:
            key[k] +=1
        else :
            key[k] = 1

with open('eggs.csv', 'w') as csvfile:
    #写文件格式是以行为单位写，每行‘[’内字符串以‘，’分隔‘]’ 或者使用算术表达式如下
    #spamwriter = csv.writer(csvfile)
    for i in key:
        print i
        csvfile.writelines()
        #spamwriter.writerow([i,key[i]])
    #或是多行写


