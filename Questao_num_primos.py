def verifica_primo(n): #Função para verificar se é primo
    i = 1; cont = 0 #i -> Termo que vai dividir o número durante o loop; cont -> Contador de divisões bem sucedidas
    while i <= n: #Loop com while
        if(n % i == 0): cont += 1 #Se o número for divisível por i, acrescenta um no contador
        i += 1 #Continuando o loop, passando para a próxima divisão
    if(cont > 2): return False #No fim, o contador diz por quantos valores o número é divisível, logo, se for maior que 2, não é primo
    else: return True #Caso seja divisível por até dois valores (1 e ele mesmo), é um número primo

print("Digite um número inteiro, para verificarmos se ele é um número primo ou não.") #Solicitando ação do usuário
num = input() #Reconhecendo o número digitado
verificacao = verifica_primo(int(num)) #Chamando a função
if(verificacao == True): print(f"{num} é um número primo.") #Caso o valor retornado seja True, execute isso:
else: print(f"{num} não é um número primo") #Caso o valor retornado seja False, execute isso: