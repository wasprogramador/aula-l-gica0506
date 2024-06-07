"""
faça um programa de tabuada que o usuário digita um número e venha do 1 ate 10
"""
num = int(input("Digite um número para ver a tabuada: "))

print(f"Tabuada do {num}:")
# print("Tabuada do " + num)
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")