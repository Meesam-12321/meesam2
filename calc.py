def calculator(op1,op2,operator):
    if operator=='+':
        print(op1+op2)
    elif operator=='-':
        print(op1-op2)
    elif operator=='*':
        print(op1*op2)
    elif operator=='/':
        print(op1/op2)
    else: 
        print('enter valid input')
while True:
    x=int(input('enter operand1'))
    y=int(input('enter operand2'))
    z=input('enter operator')
    calculator(x,y,z)



