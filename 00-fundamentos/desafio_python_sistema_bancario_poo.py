from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime


class Cliente:
    def __init__(self, endereco):
            self.endereco = endereco
            self.contas = []

    def realizar_transacao(self, conta, transacao):
          transacao.registrar(conta)

    def adicionar_conta(self, conta):
          self.contas.append(conta)      

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
          super()._init_(endereco)
          self.nome= nome
          self.data_nascimento= data_nascimento
          self.cpf= cpf

class Conta:
    def __init__(self, numero, cliente):
           self._saldo = 0
           self._numero = numero
           self._agencia ="0001"
           self._cliente = cliente
           self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
          return cls(numero, cliente)   

    @property
    def saldo(self):
          return self._saldo

    @property
    def numero(self):
          return self._numero    
    
    @property
    def agencia(self):
          return self._agencia 

    @property
    def historico(self):
          return self._historico

    def sacar(self, valor):
          saldo = self.saldo
          excedeu_saldo = valor > saldo

          if excedeu_saldo:
                 print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@") 
                
          elif valor > 0:
                 self.saldo -= valor
                 print("\n=== Saque realizado com sucesso! ===")
                 return True
          
          else:
                 print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
                
          return False
          

    def depositar(self, valor): 
          if valor > 0:
                self._saldo += valor
                print("\n=== Deposito realizado com sucesso! ===")

          else:
                 print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
                 return False
          
          return True

class ContaCorrente(Conta):
      def __init__(self, numero, cliente, limite = 500, limite_saques = 3):
            super().__init__(numero, cliente)
            self.limite = limite
            self.limite_saques = limite_saques

      def sacar(self, valor):
            numero_saques = len(
                  [transacao for transacao in self.historico.
                  transacoes if transacao["tipo"] == Saque.__name__])

            
            execeu_limite = valor > self.limite
            execedeu_saques = numero_saques > self.limite_saques

            if execeu_limite:
                  print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

            elif execedeu_saques:
                  print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

            else:
                  return super().sacar(valor)
            
            return False
      
      def __str__(self):
                return f"""\
                Agência:\t{self.agencia}
                C/C:\t\t{self.numero}
                Titular:\t{self._cliente.nome}
                 Saldo:\t\tR${self.saldo:.2f}
              """
            
class Historico:
      def _init_(self):
          self._transacoes = []

      @property
      def transacoes(self):
          return self._transacoes

      def adicionar_transacao(self, transacao):
          self._transacoes.append(
          {
             "Tipo": transacao._class_._name_,
             "Valor": transacao.valor,
             "data": datetime.now().strftime("%d-%n-%Y %H:%H:%s"),
          }
          )

class Transacao(ABC):
      @property
      def valor(self):
       pass
      
      @abstractclassmethod
      def registrar(self, conta):
       pass

class Saque(Transacao):
      def _init_(self,valor):
         self.valor = valor 

      @property
      def valor(self):
          return self._valor

      def registrar(self, conta):
          sucesso_trensacao - conta.sacar(self.valor) # type: ignore

          if sucesso_transacao: # type: ignore
             conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
      def _init_(self,valor):
          self._valor = valor
      
      @property
      def valor(self):
          return self._valor


      def registrar(self, conta):
           sucesso_transacao = conta.depositar(self.valor)

           if sucesso_transacao:
            conta.historico.adicionar_trensacao(self)

import textwrap
def menu():
 menu = """\n
============= MENU ================
[d]\tDepositar
[s]\tSacar
[e]\tExtrato
[nc]\tNova conta
[lc]\tListar contas
[nu]\tNovo usuário
[q]\tSair
=> """
 return input(textwrap.dedent(menu))

def filtrar_cliente(cpf, clientes):
     clientes_filtrados = [cliente for cliente in clientes_filtrados if cliente.cpf == cpf]
     return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
     if not cliente.contas:
          print("\n@@@ Cliente não possui conta! @@@")
          return
       
     #FIXME: não permite cliente escolher a conta 
      

def depositar(clientes):
    cpf = input("Informe o CPF do cliente")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return
    valor = float(input("Informe o valor do depósito:"))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
         return
    cliente.realizar_transacao(conta, transacao)

def sacar(clientes):
     cpf = input("Informe o CPF do cliente: ")
     cliente = filtrar_cliente(cpf, clientes)
     if not cliente:
          print("\n@@@ Cliente não encontrado! @@@")
          return
     valor = float(input("Informe o valor do saque: "))

     transacao = Saque(valor)

     conta = recuperar_conta_cliente(cliente)
     if not conta:
          return
     
     cliente.realizar_transacao(conta, transacao)



def exibir_extrato(clientes):
     cpf = input("Informe o cpf do cliente: ")
     cliente = filtrar_cliente(cpf, clientes)

     if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

     conta = recuperar_conta_cliente(cliente)
     if not conta:
        print("\n================ EXTRATO ================")
        transacoes = conta.historico.transacoes

        extrato = ""
        if not transacoes:
             extrato = "Não foram realizadas movimentações."
        else:
             for transacao in transacoes:
                 extrato += f"\n{transacao['tipo']}:\n\tR${transacao['valor']:.2f}"

        print(extrato)
        print(f"\nSaldo:\n\tR$ {conta.saldo:2f}")
        print("==============================================")
          

def criar_cliente(clientes):
      cpf = input("Informe o CPF(somente número):")
      cliente = filtrar_usuario(cpf, clientes)
       
      if cliente:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return
      
      nome = input("Informe o nome completo: ")
      data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa):")
      endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
 
      cliente = PessoaFisica(nome=nome, data_nascimento= data_nascimento,cpf=cpf, endereco= endereco)
      clientes.append(cliente)

      print("=== Cliente criado com sucesso! ===")

def filtrar_usuario(cfp, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf] # type: ignore
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(numero_conta, clientes, contas):
     cpf = input("Informe o CPF do cliente:")
     cliente = filtrar_usuario(cpf, clientes)

     if not cliente:
         print("\n@@@ Cliente não encontrado, fluxo de crieação de conta encerrado! @@@")
         return
     conta = ContaCorrente.nova_conta(cliente=cliente, numero= numero_conta)
     contas.contas.append(conta)

     print("\n=== Conta criada com sucesso! ===")
       

def lista_contas(contas):
    for conta in contas:
        print('=' * 100)
        print(textwrap.dedent(str(conta)))



         
def main():
   clientes = []
   contas = []
   
   while True:
       opcao = menu()

       if opcao == "d":
          depositar(clientes)
   
       elif opcao == "s":
            sacar(clientes)

       elif opcao == "e":
           exibir_extrato(clientes)
    
       elif opcao == "nu":
         criar_cliente(clientes)
    
       elif opcao == "nc":
          numero_conta = len(contas) + 1
          criar_conta(numero_conta, clientes, contas)

       elif opcao == "lc":
        lista_contas(contas)

       elif opcao == "q":
          break

   else:
        print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada.@@@")

main()