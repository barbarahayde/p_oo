
class ContaBancaria:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo o objeto... {}".format(self))
        self.numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato (self):
        print("Titular: {}\nSaldo: R$ {:.2f}".format(self.titular, float(self.__saldo)))

    def deposito(self, valor):
        self.__saldo = self.__saldo + valor

    def saque(self, valor):
        self.__saldo = self.__saldo - valor

    def transferencia(self, valor, destino):
        self.saque(valor)
        destino.deposito(valor)
        print("Transferencia de R${} realizado com sucesso".format(valor))

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return float(self.__limite)

    @limite.setter
    def limite(self, limite):
        self.__limite = limite