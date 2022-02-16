import os,re
path =r'C:\Users\hahake\Desktop\其它/'#自己文件的路径
file_list = os.listdir(path)
print(file_list)
for i in file_list:
    name_suffix = re.search(r'.*?(\.md)$',i)#取md后缀
    if name_suffix:
        print(i)
        with open(path+i,'r',encoding="utf-8") as f1,open(path+"%s.bak" % i, "w", encoding="utf-8") as f2:
            for line in f1:
                f2.write(re.sub(r'^!\[.*\]','![]',line))
        os.remove(path+i)
        os.rename(path+"%s.bak" % i,path+i)
