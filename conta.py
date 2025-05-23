class Conta:
    def __init__(self,agencia,numero,titular,saldo,senha):
        self.__agencia = agencia
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__senha = senha

    def extrato(self):
        return self.__saldo
      
    def sacar(self,valor):
        if self.__saldo >= valor:
           self.__saldo -= valor
           return true
        else:
            return false