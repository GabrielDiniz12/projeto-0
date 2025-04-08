from contato import Contato


class Agenda():
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, nome, telefone):
        self.contatos.append(Contato(nome, telefone))
        print('Contato adicionado!')

    def listar_contatos(self):
        if not self.contatos:
            print('A agenda esta vazia!')
        else:
            for contato in self.contatos:
                print(contato)

    def buscar_contato(self, nome):
        encontrados = [c for c in self.contatos if c.nome.lower() == nome.lower()]
        if encontrados:
            for contato in encontrados:
                print(contato)
        else:
            print('Contato não encontrado!')
    def remover_contato(self, nome):
        self.contatos = [c for c in self.contatos if c.nome.lower() != nome.lower()]
        print('Contato removido!(se existia na agenda)')

    def menu(self):
        agenda = Agenda()
        while True:
            print('\n1.Adicionar Contato')
            print('2.Listar Contatos')
            print('3.Buscar Contatos')
            print('4.Remover Contatos')
            print('5.Sair')

            opcao = input('Escolha uma opção: ')

            if opcao == '1':
                nome = input('Nome: ')
                telefone = input('Telefone: ')
                self.adicionar_contato(nome, telefone)

            elif opcao == '2':
                self.listar_contatos()
            
            elif opcao == '3':
                nome = input('Digite o nome para buscar: ')
                self.buscar_contato(nome)
            elif opcao == '4':
                nome = input('Nome do contato que deseja remover: ')
                self.remover_contato(nome)
            elif opcao == '5':
                break
            else:
                print('Opção inválida! Tente novamente.')
            
if __name__ == "__main__":
    agenda = Agenda()
    agenda.menu()