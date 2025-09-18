def simple_calculator():
    print ('bun venit la simplul calculator')
    print ('poti efectua impartiri, inmultiri si scaderi')

    num1= float(input('care este primul numar?'))
    oper= input('care este operatorul?')
    num2 = float(input('care este al doilea?'))

    if oper == '+':
         print (num1 + num2)

    elif oper == '-':
        print (num1 - num2)
    
    elif oper == '*':
        print (num1 * num2)

    elif oper == '/':
        if num1 > 0:
            print (num1 / num2)
            
        else:
            print ('numarul este 0 sau mai mic')


simple_calculator()