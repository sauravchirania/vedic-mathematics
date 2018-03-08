from fractions import gcd
from collections import defaultdict

def func_gcd(n1,n2):
	if n1==1 or n2==1:
		return 1 #corner case
	d1=defaultdict(int)
	d2=defaultdict(int)
	i=2
	while (n1>1):
		while n1%i==0:
			d1[i]+=1
			n1=n1//i
		i+=1
	j=2
	while (n2>1):
		while n2%j==0:
			d2[j]+=1
			n2=n2//j
		j+=1
	ans=1
	for factor in d1:
		if factor in d2:
			ans*=factor*min(d1[factor],d2[factor])
	return ans
		

n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))

print("The gcd is:",func_gcd(n1,n2))
print("The gcd using library function is:",gcd(n1,n2))