
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo o objeto... {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato (self):
        print("O saldo é igual a {} do titular {} ".format(self.saldo, self.titular))

    def deposito(self, valor):
        self.saldo = self.saldo + valor
        print("Deposito de R${} realizado com sucesso".format(valor))

    def saque(self, valor):
        self.saldo = self.saldo - valor
        print("Saque de R${} realizado com sucesso".format(valor))




