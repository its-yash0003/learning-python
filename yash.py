# n=1
# while True:
#   print(n)
#   n=n+1
#   if n==5:
#     break
#   print("hello")


# for i in "python":
#   print(i)
#   if i =="o":
#     pass
# print("bye")



# l=(True,1,2,3,False)
# print(sum(l))





# f=open("demofile.txt","r")
# print(f.readlines())

# f1=open("input.txt","r")
# f2=open("output.txt","w")
# s=f1.readlines()
# f1.close()
# for i in range(len(s)):
#     if i%2!=0:
#         f2.write(s[i])
# f2.close()        

f=open("s.txt","r")
f.seek(2)
print(f.readlines())
print(f.tell())