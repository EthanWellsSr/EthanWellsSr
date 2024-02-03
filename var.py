"""
data type in python
int 
float
str (string)
bool (boolean) (true false)
"""
"""
block comment
"""
# inline comment 

#x=1 #integer
#y=3.4 #float
#z="ethan" #string
#is_cool= True #bool
#ethan=1200
#print(x,y,z,is_cool)

#calendar=12
#x=calendar/4
#name="ethan"
#e= False
#print()

"""
operators
* multiplication
/ division
+ addition
- subtraction
% mod
// floor operator
== conditonal operator
"""


"""
characters_name = "Christina"
characters_age= "48"
characters_weight= "150"
print("The man named " + characters_name +  " is tall")
print(characters_name + " is a kind man")
print(characters_name + " is " + characters_age + " years old")
print(characters_name + " weighs " + characters_weight + " pounds")
"""

"""
name = input("Enter your first and last name: ")
age = input('Hello ' + name + ' please enter your age: ')
gender = input('Thank you ' + name + ", please indicate whether you are male or female: ")
print(name)
print(age)
print(gender)

"""

"""

Simple calculator

number_one = float(input('Please enter a number: '))
number_two = float(input('Please enter another number: '))
sum = (number_one) - (number_two)
print(sum)

"""


"""

noun = input("Please enter any random noun: ")
plural_noun = input("Please enter any random plural noun: ")
celebrity = input("please enter any random celebrties name: ")

print(noun + " went to the Staples Center to watch the " + plural_noun + " play in concert.")
print("While at the concert they met " + celebrity + '.')
"""
"""

lucky_numbers = [0, 13, 24, 35, 46, 57, 68, 79, 80, 91, 0]
family = ['Krystyna', 'Ethan Jr.', 'Esmeralda', 'Ty', 'Christina', 'Nana', "Pepaw"]
family.append('Diedre')
family.insert(0, 'Ethan Sr.')
family.pop()
family.remove('Ty')
family.sort()
print(lucky_numbers.count(0))
print(family)
print(family.index('Ethan Jr.'))
lucky_numbers.reverse()
lucky_numbers.sort()

family2 = family.copy()

print(family2)
print(lucky_numbers)

"""
"""
def edub():
    print('Hello big boy')

edub()
"""

def main():
    name = input('Please enter your first name: ')
    height = input(name + ', please tell me your height: ')
    print('Hello ' + name + ' you are ' + height + ' and you are very attractive.')

main()
    




