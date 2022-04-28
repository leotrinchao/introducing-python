def cubo(n):
    return pow(n, 3)

print("Digite um número que deseja elevar ao cubo:")
num = input()

num_cubo = cubo(int(num))

print(num_cubo)