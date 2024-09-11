from datetime import datetime, timedelta

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[c] Crédito
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
credito = 300
ultimo_saque = None  # Variável para armazenar o horário do último saque

while True:

    opcao = input(menu)

    # Função para verificar se os saques podem ser reiniciados
    def reiniciar_saques():
        global ultimo_saque, numero_saques
        agora = datetime.now()
        if ultimo_saque:
            diferenca = agora - ultimo_saque
            # Verifica se já passou 24 horas
            if diferenca >= timedelta(days=1):
                numero_saques = 0  # Reinicia o contador de saques
        ultimo_saque = agora  # Atualiza o horário do último saque

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        # Verifica se é necessário reiniciar o contador de saques
        reiniciar_saques()

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "c":
        print(f"Vc tem {credito} de crédito")
        if credito > 0:
            valor = float(
                input(" Informe o valor que deseja tomar de crédito: "))
            if valor > credito:
                print("Operação falhou! O valor informado é inválido.")
            else:

                saldo = saldo + valor
                credito = credito - valor
                print("Seu crédito já foi liberado em sua conta.")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
