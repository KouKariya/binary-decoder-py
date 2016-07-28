#decoder.py
#Written by Jesse Gallarzo
#add commented code to implement this script in Python 3

binInput=raw_input("Enter 4 bit binary number: ")
#reverse string to account for right-to-left from binary values
binValue =1
result=0

for num in binInput:
	if(num=="1"):
		result+=binValue
		binValue*=2
	else(num=="0"):
		binValue*=2
print(result)
