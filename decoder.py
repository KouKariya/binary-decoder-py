#decoder.py
#Written by Jesse Gallarzo

binInput=raw_input("Enter 4 bit binary number: ")
binValue =1
result=0

for num in binInput:
	if(num=="1"):
		result+=binValue
		binValue*=2
	else(num=="0"):
		binValue*=2
print(result)
