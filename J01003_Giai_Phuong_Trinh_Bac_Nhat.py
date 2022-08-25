a,b=map(int,input().split())
if(a==0 and b==0):
    print("VSN")

elif(a==0 and b!=0):
    print("VN")

else:
    print ("{:.2f}".format(-b/a))

