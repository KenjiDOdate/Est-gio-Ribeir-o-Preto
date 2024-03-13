
a = 0
b = 1
t = 0
n = int(input(" Insira um numero\n"))
print("\n")
if n == 1 or n == 0:
        print("Esse numero pertence a sequencia de Fibonacci")
        t += 1
  
while n > b:
    c = a + b
    a = b
    b = c
    
    
    if n == a or n == b:
        print("Esse numero pertence a sequencia de Fibonacci")
        t += 1
        break
  
if  t == 0:
    print("Esse numero nao pertence a sequencia de Fibonacci")
 