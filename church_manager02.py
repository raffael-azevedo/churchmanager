from functions_cm import entrada,saida
print("Bem-vindo[a] ao Church Manager 0.2!")
print("Em que posso ajudar?")

user_input = input("Escolha uma opção: [E]ntrada ou [S]aída -> ")
user_input = user_input.upper()
var_exit = True
if user_input == "E":
    print("Opção selecionada: Entrada.")
    entrada()
    print(entrada[1])
