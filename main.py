from add import add
from subtract import subtract
from multiply import multiplication
import sys

print("Choose Valid Option\n1.Addition\n2.Subtraction\n3.Multiplication")
a = int(sys.argv[3])

if(a>=1 and a<=3):
	b=int(sys.argv[1])
	c=int(sys.argv[2])

	if(a==1):
		add(b,c)
	elif(a==2):
		subtract(b,c)
	else:
		multiplication(b,c)
else:
	print("Choose valid option")
