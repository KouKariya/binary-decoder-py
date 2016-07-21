#decoder.py
#Written by Jesse Gallarzo

binInput=str(input("Enter 4 bit binary number:"))
binValue =1
result=int()

for num in binInput:
	if(num=="1"):
		result+=binValue
		binValue*=2
	elif(num=="0"):
		binValue*=2
print(result)
