historico = []

while True:
    print("====CALCULADORA====")
    print("1- somar")
    print("2- subtrair")
    print("3- multiplicar")
    print("4- dividir")
    print("5- sair")
    print("6- histórico")
    print("===================")

    opcao = input("escolha: ")
    if opcao == "1":
        n1 = float(input("primeiro numero: "))
        n2 = float(input("segundo numero: "))
        resultado = n1 + n2
        print(n1, "+", n2, "=", resultado)
        historico.append(f"{n1} + {n2} = {resultado}")

        print("Resultado da soma: ", resultado)

    elif opcao == "2":
        n1 = float(input("primeiro numero: "))
        n2 = float(input("segundo numero: "))
        resultado = n1 - n2
        print(n1, "-", n2, "=", resultado)
        historico.append(f"{n1} - {n2} = {resultado}")

        print("Resultado da subtração: ", resultado)

    elif opcao == "3":
        n1 = float(input("primeiro numero: "))
        n2 = float(input("segundo numero: "))
        resultado = n1 * n2
        print(n1, "*", n2, "=", resultado)
        historico.append(f"{n1} * {n2} = {resultado}")

        print("Resultado da multiplicação: ", resultado)

    elif opcao == "4":
        n1 = float(input("primeiro numero: "))
        n2 = float(input("segundo numero: "))
        resultado = n1 / n2
        print(n1, "/", n2, "=", resultado)
        historico.append(f"{n1} / {n2} = {resultado}")

        print("Resultado da divisão: ", resultado)

    elif opcao == "6":
        print("histórico: ")
        for conta in historico:
            print(conta)

    elif opcao == "5":
        print("saindo.")
        break
