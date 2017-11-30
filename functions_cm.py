def entrada():
    classe = input("Digite a classe da entrada: ")
    nome = input("Digite o nome da entrada: ")
    nome = nome.upper()
    valor = float(input("Digite o valor da entrada: R$ "))
    subtotal_entrada = [classe,{nome:valor}]
    subtotal_entrada global

def saida():
    classe = input("Digite a classe da saída: ")
    nome = input("Digite o nome da saída: ")
    nome = nome.upper()
    valor = float(input("Digite o valor da saída: R$ "))
    subtotal_saida = [classe,{nome:valor}]
    subtotal_saida global
