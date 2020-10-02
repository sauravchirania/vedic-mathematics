x=int(input("Enter a number ending with 5: "))
ans=(x//10)*(x//10 +1)*100 +25
print("Square of the given number is:",ans)
print("Square using library function is: ",x**2)
print("They are equal" if ans==x**2 else /n "They are not equal")
