# Create your own build in class to find the nth power of x
class pow_of_variable:
    variable_x=1 # static variables
    power_n=1 # static variable
    def variable():
        pow_of_variable.variable_x=int(input("Enter the value of x:"))
        pow_of_variable.power_n= int(input("Enter the value of power:"))
    def result():
        output=pow_of_variable.variable_x**pow_of_variable.power_n #output is local variable
        print("The nth power of variable x is given by :",output)
pow_of_variable_obj=pow_of_variable() # object created
pow_of_variable.variable()
pow_of_variable.result()






