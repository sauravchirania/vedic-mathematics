n1=input("Enter the first number: ").strip()
n2=input("Enter the second number: ").strip()

lookup=[[0,0,0,0,0,0,0,0,0,0],[0,1,2,3,4,5,6,7,8,9],[0,2,4,6,8,10,12,14,16,18],
[0,3,6,9,12,15,18,21,24,27],[0,4,8,12,16,20,24,28,32,36],[0,5,10,15,20,25,30,35,40,45],
[0,6,12,18,24,30,36,42,48,54],[0,7,14,21,28,35,42,49,56,63],[0,8,16,24,32,40,48,56,64,72],
[0,9,18,27,36,45,54,63,72,81]]

if len(n1)>len(n2):
	n2=(len(n1)-len(n2))*'0' + n2
elif len(n2)>len(n1):
	n1=(len(n2)-len(n1))*'0' + n1

n=len(n1)
ans=[]
carry=0

for i in range(1,n+1):
	s=0
	for j in range(1,i+1):
		s+=lookup[int(n2[-i+j-1])][int(n1[-j])]
	s+=carry
	ans.append(str(s%10))
	carry=s//10

for i in range(1,n):
	s=0
	for j in range(1,n-i+1):
		s+=lookup[int(n2[j-1])][int(n1[n-i-j])]
	s+=carry
	ans.append(str(s%10))
	carry=s//10
ans=ans[::-1]
ans="".join(ans)
ans=int(ans)
ans2=int(n1)*int(n2)
print("The calculated product of given numbers is : ", ans)
print("The product using library function is: ",ans2)
print("They are equal" if ans==ans2 else "They are unequal")