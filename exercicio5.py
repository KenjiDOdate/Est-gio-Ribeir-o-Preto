
palavra_ori = input("escreva\n\n")
palavra_inv = ''

for i in range(len(palavra_ori) - 1, -1, -1):
        palavra_inv += palavra_ori[i]
        
print("String original:", palavra_ori)
print("String invertida:", palavra_inv)