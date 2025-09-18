def simple_calculator():
    print("Bine ai venit la Calculatorul Simplu!")
    print("Poți efectua adunări, scăderi, înmulțiri și împărțiri.")

    #calculatorul te pune sa introduci numere

    num1 = float(input("Introdu primul număr:"))
    op = input ("Introdu un operator (+, -, *, /):")
    num2 = float(input("Introdu al doilea număr:"))

    #rezultatul

    if op == '+':
        print ('Result:', num1 + num2)
    elif op == '-':
        print ('Result:', num1 - num2)
    elif op == '*':
        print ('Result:', num1 * num2)
    elif op == '/':
        if num2 > 0:
            print ('Result:', num1 / num2)
        else:
            print("Eroare: Împărțirea la zero nu este permisă.")



simple_calculator()
