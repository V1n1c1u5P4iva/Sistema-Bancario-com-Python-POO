from Transacao import Transacao

class Saque(Transacao):
    
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        transacao = conta.sacar_dinheiro(self._valor)
        
        if transacao:
            conta.retorna_historico.adicionar_transacao(self)
