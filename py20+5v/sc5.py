import datetime
start = datetime.datetime.now()
print('单字全码编码开始')
# 范渣大神好qwq

# 读入映射，记录到my1 my2两个字典，my1是前两码，my2是后三码。
f = open('my1.txt',encoding='utf-8',mode='r')
my1 = {}
for line in f:
    my,aj = line.strip('\r\n').split('\t')
    my1[my] = aj
f.close()
f = open('my2.txt',encoding='utf-8',mode='r')
my2 = {}
for line in f:
    my,aj = line.strip('\r\n').split('\t')
    my2[my] = aj
f.close()

# 进行单字全码的输出
dyzx=[]
f = open('info.txt',encoding='utf-8',mode='r')
fo = open('qm.txt',encoding='utf-8',mode='w')
for line in f:
# c1 c2 c3 c4/g1 g2 g3 g4分别对应首首部，首次部，次首部，次次部的笔画/字根。
    z,fre,s,y,b,h = line.strip('\r\n').split('\t')
    m1 = my1[s]
    m2 = my2[y]
    m3 = my1[b[1]]
    m4 = my1[b[2]]
    if len(b) == 3:
        m5 = my1[b[2]]
    else:
        m5 = my1[b[3]]
# 写入
    s = z+'\t'+fre+'\t'+m1+'\t'+m2+'\t'+m3+'\t'+m4+'\t'+m5+'\n'
    m1=''
    m2=''
    m3=''
    m4=''
    m5=''
# 多音字，但第一个字母相同的不重复进行编码。
    if (z,s,h) not in dyzx:
        fo.write(s)
    dyzx.append((z,s,h))
f.close()
fo.close()
print('单字全码已输出至qm.txt')
end = datetime.datetime.now()
print('全码输出用时：',end-start)

#进行单字简码的输出
start = datetime.datetime.now()
print('单字简码编码开始')
# 赋初值
# 总频数
fa = 0
# 二码字频数
f2 = 0
# 三码字频数
f3 = 0
# 先输出wlm.txt中定义的字。
f = open('wlm.txt',encoding='utf-8',mode='r')
fo = open('jm5.txt',encoding='utf-8',mode='w')
#fi = open('gcm.txt',encoding='utf-8',mode='w')
# 记录已占用的编码，输出简码用
# 为啥绕个圈用dict？快呀。
bm = {}
# 记录已定义的无理码并输出
wlm = {}
for line in f:
    z, m = line.strip('\n\r').split('\t')
    fo.write(z+'\t'+m+'\n')
#    fi.write(z+'\t'+m+'\n')    
    if len(z)==1:
        wlm[z] = m
    bm[m]=1
f.close()
# 输出其它字
f = open('qm.txt',encoding='utf-8',mode='r')
#fu = open('pxu.txt',encoding='utf-8',mode='w')
qm = {}
n22=0
n5=0
n6=0
n7=0
for line in f:
    z,fre,m1,m2,m3,m4,m5 = line.strip('\n\r').split('\t')
    qm[z] = m1+m2+m3+m4+m5
    fa += float(fre)
    if z not in wlm:
# 前两码未被占用，则该字为两码字。
        if qm[z][:2] not in bm:
            fo.write(z+'\t'+qm[z][:2]+'\n')
            #fi.write(z+'\t'+qm[z][:2]+'\n')
            bm[qm[z][:2]] = 1
            #fu.write(z+'\t'+qm[z][:2]+'\t'+fre+'\n')
            f2 += float(fre)
# 前三码未被占用，则该字为三码字。依此类推。
# 注：生成整句码表的时候以下四行要注释掉！！！！
        elif qm[z][:3] not in bm:
            #fi.write(z+'\t'+qm[z][:3]+'\n')
            fo.write(z+'\t'+qm[z][:3]+'\n')
            bm[qm[z][:3]] = 1
            f3 += float(fre)
        elif qm[z][:4] not in bm:
            #fi.write(z+'\t'+qm[z][:3]+'\n')
            fo.write(z+'\t'+qm[z][:4]+'\n')
            bm[qm[z][:4]] = 1
            #fu.write(z+'\t'+qm[z][:4]+'\t'+fre+'\n')
        elif qm[z] not in bm:
            #fi.write(z+'\t'+qm[z][:3]+'\n')
            fo.write(z+'\t'+qm[z]+'\n')
            bm[qm[z]] = 1
            #fu.write(z+'\t'+qm[z]+'\t'+fre+'\n')
            n5+=1
        else:
            #fi.write(z+'\t'+qm[z][:3]+'\n')
            fo.write(z+'\t'+qm[z]+'\n')
            #fu.write(z+'\t'+qm[z]+'\t'+fre+'\n')
            n5+=1
            n6+=1
    else:
        f2 += float(fre)
fo.close()
#fi.close()
#fu.close()
f.close()
print('二码总频：',f2/fa)
print('三码总频：',(f3+f2)/fa)
print('五码字：',n5)
print('六码字：',n6)
end = datetime.datetime.now()
print('简码输出用时：',end-start)
print('简码已输出至jm.txt')

# 编码词。
# start = datetime.datetime.now()
# print('词组编码开始')
# # 记录词的编码，统计重码用
# c = {}
# cm = 0#词重码统计
# cs2 = 0# 二字词数统计
# cs3 = 0# 三字词数统计
# cs4 = 0# 四字词数统计
# cs5 = 0# 多字词数统计
# f = open('wlm.txt',encoding='utf-8',mode='r')
# #读入词表
# fi = open('cb.txt',encoding='utf-8',mode='r')
# #输出码表
# fo = open('cz.txt',encoding='utf-8',mode='w')
# #这里说明一下。因为点儿词库不带拼音，直接引用单字码表生成五码词会有多音字的问题
# #所以迂回一下，改用整句的词库来确定点儿词库中词的音。
# fj = open('zj.txt',encoding='utf-8',mode='r')
# cys={}
# for line in fj:
#     z,m=line.strip('\r\n').split('\t')
#     mm=list(m.split(' '))
#     cys[z]=mm
# fj.close()
# #这里用jm码表决定这个词到底收不收。
# d={}
# fj = open('jm.txt',encoding='utf-8',mode='r')
# for line in fj:
#     z,m=line.strip('\r\n').split('\t')
#     d[z]=m
# fj.close()
# # 记录已定义的简词并输出
# jc = {}
# for line in f:
#     z, m = line.strip('\n\r').split('\t')
#     if len(z) > 1:
#         jc[z] = 1
# f.close()
# for line in fi:
#     w,p = line.strip('\n').split('\t')
#     i = len(w)
#     try:
#         zmc = sum(len(d[z]) for z in w)
#     except KeyError:
#         zmc = 0
#     if zmc > 5:#单字打法能五键出的词就不做了
#         if i == 2:
#             if w in cys:
#                 m = cys[w][0][:2] + '9' + cys[w][1][:2]
#                 fo.write(w+'\t'+m+'\n')
#                 cs2 += 1
#                 if m not in c:
#                     c[m] = 1
#                 else:
#                     cm += 1
#         elif i == 3:
#             if w in cys and zmc>6:# 三字六键也不做
#                 m = cys[w][0][0] + cys[w][1][0] + '3' + cys[w][2][:2]
#                 fo.write(w+'\t'+m+'\n')
#                 cs3 += 1
#                 if m not in c:
#                     c[m] = 1
#                 else:
#                     cm += 1
#         elif i == 4:
#             if w in cys:
#                 m = cys[w][0][0] + cys[w][1][0] + '8' + cys[w][2][0] + cys[w][-1][0]
#                 fo.write(w+'\t'+m+'\n')
#                 cs4 += 1
#                 if m not in c:
#                     c[m] = 1
#                 else:
#                     cm += 1
#         else:
#             if w in cys:
#                 m = cys[w][0][0] + cys[w][1][0] + '8' + cys[w][2][0] + cys[w][-1][0]
#                 fo.write(w+'\t'+m+'\n')
#                 cs5 += 1
#                 if m not in c:
#                     c[m] = 1
#                 else:
#                     cm += 1
# fi.close()
# fo.close()
# print('二字词数：',cs2)
# print('三字词数：',cs3)
# print('四字词数：',cs4)
# print('多字词数：',cs5)
# print('总词数：',cs2+cs3+cs4+cs5)
# print('词库选重数：',cm)
# print('词库选重率：',cm/(cs2+cs3+cs4+cs5))
# end = datetime.datetime.now()
# print('词组输出用时：',end-start)
# print('词组已输出至cz.txt')

# 输出mb
start = datetime.datetime.now()
print('输出挂接在rime平台上的码表')
f = open('jm.txt',encoding='utf-8',mode='r')
fo = open('mb.txt',encoding='utf-8',mode='w')
for line in f:
    z, zm = line.strip('\n\r').split('\t')
    fo.write(z+'\t'+zm+'\n')
f.close()
# 无理提示
for z in wlm:
    if z not in ['，','。']:
# 前四码未被占用，则在四码上提示。
        if qm[z][:4] not in bm:
            fo.write(z+wlm[z]+'\t'+qm[z][:4]+'\n')
            bm[qm[z][:4]] = 1
# 四码被占用，则在五码上提示。
        else:
            fo.write(z+wlm[z]+'\t'+qm[z]+'\n')
#f = open('cz.txt',encoding='utf-8',mode='r')
#for line in f:
#    c, cm = line.strip('\n\r').split('\t')
#    fo.write(c+'\t'+cm+'\n')
#f.close()
fo.close()
end = datetime.datetime.now()
print('码表输出用时：',str(end-start))
print('码表已输出至mb.txt')

