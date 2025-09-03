'''x=int(input("enter any vaue:"))
fact=1
i=1
while i<=x:
	fact=fact*i
	i=i+1
print("factorial of {}={}".format(x,fact))'''

choice=True
while choice:
	n=int(input("enter any value:"))
	fact=1
	for i in range(1,n+1):
		fact=fact*i
	print("factorial of {}={}".format(n,fact))
	user_choice=input("enter y to continue and n to stop: ")
	if user_choice=="n":
		choice=False
	else:
		choice=True