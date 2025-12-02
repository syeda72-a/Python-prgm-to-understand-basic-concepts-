print("use of assert statement")
def negativecheck(number):
    assert(number>=0),"oops…negative number"
    print(number*number)
print(negativecheck(100))#works fine
print(negativecheck(-350))#assertion error