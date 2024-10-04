# print - вывод какого либо текста или значения
print("Hello, world!")
print("Hello", "world!", sep=", ")

# Аргумент end используется если мы хотим написать два принта в одну строку
print("first row", end=" ")
print("second row")

# input - приостанавливает исполнение кода чтобы пользователь что-то ввел в терминал
input("Please enter something")
name = input("Enter your name: ")
print(name)

#переменная
name ="Alice"
print(name)

name = "Alice"
age = 25
print(name, age, sep =" is ")

name, age = "Alice", 25
print(name, age, sep= " is ")

# замена значений 
x = 1
y = 2

x, y = y, x
print(x,y)

#функция type. К какому типу относится значение
variable = "Alice"
print(type(variable))

#snake_case - имена перменных, функций, методов модулей; 
#CamelCase - имена классов
#yet-another-package - названия пакетов
#CONSTANT - константы



#Числа(int)
x = 10
y = 2
summary = x + y
z = x * y
h = x / y
print(summary)
print(type(z))
print(type(h))
