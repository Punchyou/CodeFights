class Employee:
    num_of_emps = 0 #class variable
    raise_amount = 1.04 #class variable
    def __init__(self, first, last, pay):#call the instance self
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps +=1

    def fullName(self): #always call the instance self
        return '{} {}'.format(self.first, self.last)
        
    #I could create a method for an every year raise
    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount) #I have to use Employee to acces the class variable raise_amount

    #call a decorator: class method
    @classmethod #class methods have to have an argument as a class, f.e. cls
    def set_raise_amt(cls, amount):
        cls.raise_amount= amount
    #we can create objects that splits the string where '-' is. We first, last, pay from __init__ class, for all employees through a class method
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-') #create an object that splits the string where '-' is. We first, last, pay from __init__ class!!!
        cls(first, last, pay) #= Employee(first, last, pay)
        return cls(first, last, pay)

emp_1 = Employee('Maria', 'Pantsiou', 5000)#the instance self is in the  automatically. we don't have to pass it in
emp_2 = Employee('Test', 'Name', 40000)

emp_str_1 = 'Maria-Pan-4000'
emp_str_2 = 'Maria-Koura-75000'
emp_str_3 = 'Akis-Kourbetis-80000'
#first, last, pay = emp_str_1.split('-') #create an object that splits the string where '-' is. We first, last, pay from __init__ class!!!
new_emp_1 = Employee.from_string(emp_str_3)



print(emp_1.pay, emp_1.email)

#if I want to prin the full name:
#print('{} {}'.format(emp_1.first, emp_1.last))

print(emp_2.fullName())

#these two do exactly the same thing
print(emp_1.fullName()) #instance emp_1 and call the method fullName. Ia don't have to pass the self argument. it does it automatically.
print(Employee.fullName(emp_1))#we call the the method on the class we have to specify the instance(object).it passes employ_1 as self


print("emp_1 pay amount: ", emp_1.pay)
emp_1.apply_raise()
print("pay after raise: ", emp_1.pay)

print("raise: ", emp_1.raise_amount)
#change the amount of raise
#Employee.raise_amount = 1.05

print("new raise: ", emp_1.raise_amount)
#or change it only for emp_1
emp_1.raise_amount = 1.05
#print(Employee.__dict__)

print('Number of employees: ', Employee.num_of_emps)

#apply raise amount to all employees because of the set_raise_amount class method
Employee.set_raise_amt(1.1) #10%
print('Emplyee raise for set classmethod :', Employee.raise_amount)
print('Employee 1 raise: ', emp_1.raise_amount)
print('Employee 2 raise: ', emp_2.raise_amount)

#employess names with '-' in the middle
print(new_emp_1.email)