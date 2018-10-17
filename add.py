print("This program adds two positive numbers!")

lookup = [[0,1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9,10], [2,3,4,5,6,7,8,9,10,11],
[3,4,5,6,7,8,9,10,11,12], [4,5,6,7,8,9,10,11,12,13], [5,6,7,8,9,10,11,12,13,14],
[6,7,8,9,10,11,12,13,14,15], [7,8,9,10,11,12,13,14,15,16], [8,9,10,11,12,13,14,15,16,17],
[9,10,11,12,13,14,15,16,17,18]]

n1=input("Enter the first number: ").strip()
n2=input("Enter the second number: ").strip()


#pad zeros to make the strings of equal length
if len(n1)>len(n2):
	n2=(len(n1)-len(n2))*'0' + n2
elif len(n2)>len(n1):
	n1=(len(n2)-len(n1))*'0' + n1

n = len(n1)
ans = []
carry = 0

for i in range(n-1,-1,-1):
	carry+= lookup[int(n1[i])][int(n2[i])]
	ans.append(str(carry%10))
	carry //=10

while carry>0:
	ans.append(str(carry%10))
	carry=carry//10

ans=ans[::-1]
ans="".join(ans)
ans=int(ans)
ans2=int(n1)+int(n2)
print("The calculated sum of given numbers is :", ans)
print("The sum using library function is:", ans2)
print("They are equal" if ans==ans2 else "They are unequal")