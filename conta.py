
class ContaBancaria:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo o objeto... {}".format(self))
        self.numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def deposito(self, valor):
        self.__saldo = self.__saldo + valor

    # metodo privado para uso dentro da classe apenas
    def __autoriza_saque(self, valor_saque):
        valor_disponivel = self.__saldo + self.__limite
        return valor_saque <= valor_disponivel

    def saque(self, valor):
        if self.__autoriza_saque(valor):
            self.__saldo -= valor
            print(f"Saque de R$ {valor} realizado com sucesso!")
        else:
            print("Saldo insuficiente")

    def transferencia(self, valor, destino):
        self.saque(valor)
        destino.deposito(valor)
        print(f"Transferencia de R$ {valor} realizado com sucesso")

    def set_limite(self, novo_limite):
        self.__limite = novo_limite

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return float(self.__limite)

    @staticmethod
    def codigo_banco():
        return '001'

    @staticmethod
    def codigos_bancos():
        return {
            'BB':'001',
            'Bradesci':'237',
            'Caixa':'104'
        }

    @property
    def extrato(self):
        return (
            f"Titular: {self.__titular} | "
            f"Saldo: R$ {float(self.__saldo):.2f}"
        )