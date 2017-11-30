print("Bem-vindo[a] ao Church Manager 0.1!")
print("Em que posso ajudar?")


user_input = input("Escolha uma opção: [E]ntrada ou [S]aída -> ")
user_input = user_input.upper()
var_exit = True

if user_input == "E":
    print("Opção selecionada: Entrada.")
    entrada = open("report.txt",'w')
    entrada.write("ENTRADAS:\n")
    while var_exit == True:
        entry_class = input("Digite a classe da entrada: ")
        entry_name = input("Digite o nome da entrada: ")
        entry_name = entry_name.upper()
        entry_value = float(input("Digite o valor da entrada: R$ "))
        entrada.write("%s\n" % entry_class)
        entrada.write("%s ...... R$ %5.2f \n" % (entry_name,entry_value))
        exit_value = input("Para sair, digite 'SAIR' ou pressione qualquer tecla para continuar: ")
        exit_value = exit_value.upper()
        if exit_value == 'SAIR':
            var_exit = False
            entry_class = ""
            entrada.close()
elif user_input == "S":
    print("Opção selecionada: Saída.")
    saida = open("report.txt",'w')
    saida.write("SAÍDAS:\n")
    while var_exit == True:
        entry_class = input("Digite a classe da saída: ")
        entry_name = input("Digite o nome da saída: ")
        entry_name = entry_name.upper()
        entry_value = float(input("Digite o valor da saída: R$ "))
        saida.write("%s\n" % entry_class)
        saida.write("%s ...... R$ %5.2f \n" % (entry_name,entry_value))
        exit_value = input("Para sair, digite 'SAIR': ")
        exit_value = exit_value.upper()
        if exit_value == 'SAIR':
            var_exit = False
            saida.close()
else:
    print("Opção inválida! Digite [E]ntrada ou [S]aída.")
