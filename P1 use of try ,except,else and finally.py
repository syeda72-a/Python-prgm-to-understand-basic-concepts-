print("praticing for try block")
try:
    numerator=50
    denominator=int(input("enter the denominator: "))
    quotient=(numerator/denominator)
    print("division performed successfully")
except ZeroDivisionError:
    print("denominator in the zero not allowed")
except ValueError:
    print("only integers should be entered")
else:
    print("quotient is: ",quotient)
finally:
    print("over and out")