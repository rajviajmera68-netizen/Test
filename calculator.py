def add(x,y):
	return x+y

def sub(x,y):
	return x-y

def mul(x,y):
	return x*y

def div(x,y):
	if y==0:
		print("invalid denominator")
	else:
		return x/y

def opr():
	print("=====================")
	opr1=flot(input("enter operand 1:"))
	opr2=flot(input("enter operand 2:"))
	print("=====================")
	return opr1,opr2


def calc():
		opt_choice=input("press 1 for addition\npress 2 for substraction\npress 3 for division\npress 4 for multiplica\nEnter a valid choice:")
		if opt_choice == "1":
			opr1, opr2 = opr()
			result=add(opr1,opr2)
			print("=====================")
			print("Answer: {} + {} = {}".format(opr1,opr2,result))
			print("=====================")

		elif opt_choice=="2	":
			opr1,opr2=opr()
			result=sub(opr1,opr2)
			print("=====================")
			print("Answer: {} - {} = {}".format(opr1,opr2,result))
			print("=====================")

		elif opt_choice=="3":
			opr1,opr2=opr()
			result=div(opr1,opr2)
			print("=====================")
			print("Answer: {} / {} = {}".format(opr1,opr2,result))
			print("=====================")

		elif opt_choice=="4":
			opr1,opr2=opr()
			result=mul(opr1,opr2)
			print("=====================")
			print("Answer: {} * {} = {}".format(opr1,opr2,result))
			print("=====================")

		else:
			print("invalid choice")
			calc()

			print("=====================")
			print("welcome to calculator")
			print("=====================")
			cont_choice= True
		while cont_choice:
			calc()
			choice2=input("enter Y to continue or N to stop:")
			if choice2=="Y" or choice2=="y":
				cont_choice=True
			else:
				cont_choice=False

