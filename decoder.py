#decoder.py
#Written by Jesse Gallarzo

binInput=input("Enter 4 bit binary number: ")
binValue=1
result=int()

for num in range(len(binInput)):
  if(num==0):
    result+=binValue
    binValue*= 2
  else():
    binValue*=2
    
print(result)
