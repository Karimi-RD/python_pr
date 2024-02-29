# 4 Activity we worked on in the class
import colorama as col

#1
My_list = ["apple", "orange", "apple", "banana", "apple"]
def add_item(a):
    My_list.append(a)
def del_item(a):
    My_list.append(a)


for x in My_list:
    print(col.Fore.MAGENTA,x,end='\t')

print()
add_item('***')
print(col.Fore.MAGENTA,My_list)
del_item('orange')
print(col.Fore.MAGENTA,My_list)
print("______________________________")
#2
My_list = ["apple", "orange", "apple", "banana", "apple"]
class PL:
    def pirint_l(self,My_list):
        for x in My_list:
            print(col.Fore.YELLOW,x)


object_c = PL()
object_c.pirint_l(My_list)
print("______________________________")
#3
class User:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
x = User("sara", "D")

class Costumer(User):
    def __int__(self, fname, lname):
        super().__init__(fname, lname)
        self.phon = "00000000000"


x2 = Costumer("sara", "D")
print(col.Fore.CYAN,"customer = ", x2.lastname)
print("______________________________")
# 4
My_list = ["apple", "orange", "apple", "banana", "apple"]
class Fruts:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return My_list[x]

myclass = Fruts()
myiter = iter(myclass)

print(col.Fore.GREEN, next(myiter))
print(col.Fore.GREEN, next(myiter))
print(col.Fore.GREEN, next(myiter))
print("______________________________")
print("______________________________")
