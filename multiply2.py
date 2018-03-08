
n1=input("Enter the first number: ").strip()
n2=input("Enter the second number: ").strip()

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
		s+=int(n2[-i+j-1])*int(n1[-j])
	s+=carry
	ans.append(str(s%10))
	carry=s//10

for i in range(1,n):
	s=0
	for j in range(1,n-i+1):
		s+=int(n2[j-1])*int(n1[n-i-j])
	s+=carry
	ans.append(str(s%10))
	carry=s//10
while carry>0:
	ans.append(str(carry%10))
	carry=carry//10
ans=ans[::-1]
ans="".join(ans)
ans=int(ans)
ans2=int(n1)*int(n2)
print("The calculated product of given numbers is : ", ans)
print("The product using library function is: ",ans2)
print("They are equal" if ans==ans2 else "They are unequal")
