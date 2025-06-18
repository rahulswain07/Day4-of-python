#string function in python
s="Hello Python World"
print(s.lower())#1.lower function
#2.upper Function
name="rahul swain"
print(name.upper())
#3.Strip Function
sentence='       Rahul is a goodboy         '#remove start space and end space
print(sentence.strip())
print(sentence.lstrip())#remove left space
print(sentence.rstrip())#remove right space
#4.replace function
word='amazon'
print(word.replace('on','ing'))
#5.split function
_name='Rahul kumar Swain'
print(_name.split())
print(_name.split('kumar'))
#6.find function
Animal='Lion'
print(Animal.find('n'))#output 3
#7.start function
animal2='tiger'
print(animal2.startswith('t'))
print(animal2.endswith('er'))#8.end function
#9.length Function
Car='Audi'
print(len('Audi'))
#10.count function
counts="Rahul Is a Good boy But not a bad boy"
print(counts.count('a'))
# 11. alphabet check function
watch='rolex'
print(watch.isalpha())
#12.digit check function
num=12346799
print('1234'.isdigit())
#13.title function
bike='Raider'
print(bike.title())