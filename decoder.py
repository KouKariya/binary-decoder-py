#decoder.py
#Written by Jesse Gallarzo

binInput=input("Enter 4 bit binary number: ")
bin=1
value = int()

for num in range(len(binInput)):
  if(num==0):
    value+=bin
    bin*= 2
  else():
    bin*=2
    
print(value)
