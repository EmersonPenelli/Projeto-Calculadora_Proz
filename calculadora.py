def calculadora():
    while True:
        print("Selecione uma operação:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        opcao = input("Digite o número para a operação correspondente: ")

        if opcao == '0':
            print("Saindo da calculadora.")
            break
        elif opcao in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Digite o primeiro valor: "))
                num2 = float(input("Digite o segundo valor: "))

                if opcao == '1':
                    resultado = num1 + num2
                    print("Resultado: ", resultado)
                elif opcao == '2':
                    resultado = num1 - num2
                    print("Resultado: ", resultado)
                elif opcao == '3':
                    resultado = num1 * num2
                    print("Resultado: ", resultado)
                elif opcao == '4':
                    if num2 == 0:
                        print("Erro: Divisão por zero.")
                    else:
                        resultado = num1 / num2
                        print("Resultado: ", resultado)
            except ValueError:
                print("Erro: Entrada inválida. Certifique-se de inserir números válidos.")
        else:
            print("Essa opção não existe. Tente novamente.")

if __name__ == "__main__":
    calculadora()
