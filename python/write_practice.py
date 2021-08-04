# 파일 쓰기
파일 = open('a.txt', 'w')
파일.write('hello')
파일.close()

파일 = open('a.txt', 'a')
파일.write('\n반가워')
파일.close()


파일 = open('a.txt', 'r')
print(파일.read())
파일.close()


f=open('data.csv', 'w')
f.write('김,이,박')
f.write('\n김,이,박')
f.close

리스트 = ['삼성전자', '카카오', '네이버', '신풍제약']
f=open('a.txt', 'w')
for i in range(4):
    f.write( 리스트[i] + '\n')
f.close()


for i in range(1,10):
    for a in range(1,10):
        print(str(i) +'*'+ str(a) +'='+ str(i*a))
