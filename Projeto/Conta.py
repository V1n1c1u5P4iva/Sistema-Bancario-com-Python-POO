from Historico import Historico

class Conta:
    
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def criar_nova_conta(cls, cliente, numero):
        return cls(cliente, numero)
    
    @property
    def retorna_numero(self):
        return self._numero
    
    @property
    def retorna_agencia(self):
        return self._agencia
    
    @property
    def retorna_cliente(self):
        return self._cliente
    
    @property
    def retorna_historico(self):
        return self._historico
    
    @property
    def retorna_saldo(self):
        return self._saldo
    
    def sacar_dinheiro(self, valor):
        saldo = self.retorna_saldo
        if valor > saldo:
            print("O valor está ultrapassando o saldo disponível.")
        elif valor > 0:
            self._saldo -= valor
            print("Saque realizado com sucesso.") 
            return True
        else:
            print("Operação não realizada!")
        
        return False
    
    def depositar(self, valor):
        saldo = self.retorna_saldo
        if valor > 0:
            self._saldo += valor
            print("Depósito realizado com sucesso.")
            return True
        else:
            print("Operação não realizada!")
        return False
