def avg(n):
	sum=0
	for i in range (n):
		term=int(input("enter value:"))
		sum=sum+term
	res=sum/n
	return res
n=int(input("enter value of n:"))
result=avg(n)
print("average:",result)