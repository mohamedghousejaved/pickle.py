import pickle
f=open('stu.dat','wb')
for i in range(2):
    roll=int(input("roll no="))
    name=input("name=")
    total=int(input("total="))
    L=[roll,name,total]
    pickle.dump(L,f)
f.close()
f=open('stu.dat','rb+')
roll=int(input("rollno to be updated"))
newtotal=int(input("total to be updated"))
try:
    while True:
        position=f.tell()
        l=pickle.load(f)
        if l[0]==roll:
            l[2]=newtotal
            f.seek(position)
            pickle.dump(l,f)
except:
    f.close()

f=open("stu.dat",'rb')
while True:
    try:
        pickle.load(f)
    except:
        f.close()
