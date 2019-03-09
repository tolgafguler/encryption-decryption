import sys

hurap_file=open(sys.argv[1],"r")
#hurap_file = open("hurap.txt", "r")

schuckscii_file = open(sys.argv[2], "r")
#schuckscii_file=open("schuckscii.txt","r")

virus_codes_file = open(sys.argv[3], "r")
#virus_codes_file = open("virus_codes.txt", "r")


print(10*'*')
print("Mission 00")
print(10*'*')

print("----hex of encrypted code----","\n-----------------------------")

list=[]
list1=[]
list2=[]
list3=[]
for lines in hurap_file.readlines():                        #dosyadaki her satırı bir listeye attık

    lines=lines.rstrip("\n")
    list.append(lines)

for i in list:                                              #key satırını listeden attık
    for j in i:
         if j!='1' and j!='0' :
            key=list.pop(list.index(i))
            break
result=0
count=0
hexa=0
sayac=0
sum=0
for x in  list:                                             #tersten gelerek binary to hexa
    for i in x[::-1]:
        list2.append(int(i)*(2**count))
        count=count+1
        if(count==4):
            count=0
    list2.append("256")
for i in list2:
    if(i=='256'):
        list3.append("/n")
    else:
        result=result+int(i)
        sayac=sayac+1
        if(sayac==4):
            sayac=0
            list3.append(result)
            result=0
list4=[]
list5=[]
#print(list3)
for i in list3:
    if(i=='/n'):
        list4=list4[::-1]
        list5.extend(list4)
        list5.append('/n')
        list4=[]
    else:
        list4.append(i)
#print(list5)
list6=[]
result2=''
for i in list5:
    if(i=='/n'):
        list6.append(result2)
        result2=''
    else:
        if(i==10):
            i='A'
        elif(i==11):
            i='B'
        elif(i==12):
            i='C'
        elif(i==13):
            i='D'
        elif(i==14):
            i='E'
        elif(i==15):
            i='F'
        result2=str(result2)+str(i)
#print(list6)
for i in list6:
    print(i)

counter=0
list7=[]
for i in list6:
    for j in i:
        if counter==1:
            b=str(j)
            c=a+b
            list7.append(c)
            counter=0
        elif counter==0:
            a=str(j)
            counter+=1

    list7.append("\n")
#print(list7)

list8=[]
for lines in schuckscii_file.readlines():
    lines=lines.strip("\n")
    lines=str(lines).split("\t")
    list8.append(lines)



for i in list7:
    for j in list8:
        if i==j[1]:
            a=list7.index(i)
            b=list8.index(j)
            list7[a]=list8[b][0]
#print(list7)

print("------------encypted code---------","\n----------------------------------")

for i in list7:
    print(i,end="")

schuckscii_file.close()
key1=[]
shift_amount=0
if key[1]=='0':
        for i in key:
            key1.append(i)

        for i in key1:
            if i!='0' and i!='1':
                key1.remove(i)
        key1.reverse()

        total1=0
        for i in range(len(key1)):
            total1+=int(key1[i])*2**i
        shift_amount=total1

elif key[1]=='1':
        for i in key:
            if i=='0':
                i=1
            elif i=='1':
                i=0
            key1.append(i)
        for i in key1:
            if i!=0 and i!=1:
                key1.remove(i)
        key1.reverse()
#print(key1)
        total=0
        for i in range(len(key1)):
            total+=int(key1[i])*2**i
        shift_amount=-(total+1)
#print(shift_amount)


schuckscii_file=open(sys.argv[2],"r")
listschuc=[]
for i in schuckscii_file.readlines():
    i=i.strip("\n")
    i=str(i).split("\t")
    listschuc.append(i)
#print(listschuc)
alphabet=[]
for i in listschuc:
    alphabet.append(i[0])
#print(alphabet)

original_char=len(listschuc)
#print(original_char)

encrypted_char=(original_char+shift_amount)%original_char
#print(encrypted_char)

#print(list7)
#print(alphabet)
list10=[]
for i in list7:
    if i=="\n":
            list10.append(i)
    for j in alphabet:

        if i==j:
            a=alphabet.index(j)
            b=a-encrypted_char
            b=b%len(alphabet)
            list10.append(alphabet[b])
#schuckscii_file.close()
#print(list10)
print("\n""--- decrypted code ---","\n----------------------")
for i in list10:
    if i=="\n":
        print()
    else:
        print(i,end="")



print("********************")
print("\t","Mission 01")
print("********************")


h=[]
s=""
c=s.join(list10)
h.append(c)
#print(h)
k=[]
for i in h:
    i=str(i).split("\n")
    k.append(i)



listvirus=[]

for i in virus_codes_file.readlines():
    i=i.strip("\n")
    i=i.split(":")
    listvirus.append(i)

m=[]
for i in k:
    for j in i:
        m.append(j)
#print(m)

for i in listvirus:
    for j in range(len(m)):
        m[j]=str(m[j]).replace(i[0],i[1])




for i in m:
    print(i)

print("*********************")
print("\t","Mission 10")
print("*********************")

print("--- encrypted code ---")
print("----------------------")
#schuckscii_file=open("schuckscii.txt","r")
listschuc2=[]
for i in schuckscii_file.readlines():
    i=i.strip("\n")
    i=str(i).split("\t")
    listschuc2.append(i)

alphabet2=[]
for i in listschuc:
    alphabet2.append(i[0])
#print(listschuc)
#print(alphabet)
#print(m)

l=[]
for i in m:
    for j in i:
        if j=="":
            continue
        else:
            l.append(j)
    l.append("\n")
#print(l)

p=[]
for i in l:
     if i=="\n":
        p.append("\n")
     for j in alphabet2:

        if j==i:
            a=alphabet2.index(i)
            b=encrypted_char+a
            b=b%len(alphabet2)
            p.append(alphabet2[b])

for i in p:
    if i=="\n":
        print()
    else:
        print(i,end="")

print("--- hex of encrypted code ---")
print("-----------------------------")

#print(listschuc)
#print(p)

o=[]
for i in p:
    if i=="\n":
        o.append(i)
    for j in listschuc:
        if i==j[0]:
            o.append(j[1])
for i in o:
    print(i,end="")
print("--- bin of encrypted code ---")
print("-----------------------------")

t=[]
for i in o:
    if i =="\n":
        t.append(i)
    elif len(i)==2:
        t.append(i[0])
        t.append(i[1])
#print(t)

hexa_dic=dict([('0',"0000"),('1',"0001"),('2',"0010"),('3',"0011"),('4',"0100"),('5',"0101"),('6',"0110"),('7',"0111"),('8',"1000"),('9',"1001"),('A',"1010"),('B',"1011"),('C',"1100"),('D',"1101"),('E',"1110"),('F',"1111")])

w=[]
for i in t:
    if i=="\n":
        w.append(i)
    else:
        w.append(hexa_dic[i])
#print(w)
for i in w:
    print(i,end="")

hurap_file.close()
schuckscii_file.close()
virus_codes_file.close()
