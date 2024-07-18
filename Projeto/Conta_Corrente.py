from Conta import Conta
from Saque import Saque

class Conta_Corrente(Conta):
    
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques    
            
    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.retorna_historico.transacao if transacao["tipo"] == Saque.__name__])
        
        if valor > self.limite:
            print("Limite excede o permitido.")
        elif numero_saques >= self.limite_saques:
            print("Limite de saques permitidos já foi atingido.")
        else:
            return super().sacar_dinheiro(valor)
        
        return False
