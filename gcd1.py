from fractions import gcd

def func_gcd(n1,n2):
	if n1==0:
		return n2
	else:
		return(func_gcd(n2%n1,n1))

n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))

print("The gcd is:",func_gcd(n1,n2))
print("The gcd using library function is:",gcd(n1,n2))