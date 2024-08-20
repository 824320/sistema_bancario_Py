class ContaBancaria:
    def __init__(self, saldo=0, limite=500, limite_saques=3):
        self.saldo = saldo
        self.limite = limite
        self.limite_saques = limite_saques
        self.numero_saques = 0
        self.extrato = ""

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito: R$ {valor:.2f}\n"
            return True
        return False

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo and valor <= self.limite and self.numero_saques < self.limite_saques:
            self.saldo -= valor
            self.extrato += f"Saque: R$ {valor:.2f}\n"
            self.numero_saques += 1
            return True
        return False

    def extrato_conta(self):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("==========================================")

def main():
    conta = ContaBancaria()

    while True:
        print("""
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """)
        opcao = input().lower()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            if conta.depositar(valor):
                print("Depósito realizado com sucesso!")
            else:
                print("Operação falhou! O valor informado é inválido.")

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            if conta.sacar(valor):
                print("Saque realizado com sucesso!")
            else:
                print("Operação falhou! Verifique o saldo, limite de saque ou número de saques.")

        elif opcao == "e":
            conta.extrato_conta()

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()



    """
As alterações foram feitas para:

Melhorar a organização do código com a criação de uma classe ContaBancaria.
Tornar o código mais modular e fácil de manter com a separação dos métodos.
Melhorar a tratativa de erros com o retorno de booleanos nos métodos depositar e sacar.
Tornar o código mais robusto com a conversão da entrada do usuário para minúsculas.
Essas alterações tornam o código mais fácil de ler, manter e expandir.


    """