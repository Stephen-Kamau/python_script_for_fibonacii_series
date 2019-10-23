#fibonacii numbers
#the body will be 
#if number passed is 0 or one it returns 0,1 respectively
#if it is greater,it will keep on calling the function fibonaci until the times
#you have indicated is reached...

def main():
	#convert the number entered into an interger
	n=int(input("Enter a positive number to test its fibonaci: "))
	print("Fibonaci numbers for the range given are:\n")
	#loop througn the fibonaci function to return the number of times
	for y in range(1,n+1):
		print(fibonaci(y))

def fibonaci(n):
	#condition 1
	if n==0:
		return 0
	#condition 2
	elif n==1:
		return 1
	#condition 3
	elif n>1:
		return fibonaci(n - 1) + fibonaci(n - 2)
	else:
		print("Error while doing computation")
main()