class Tarefa:
    def __init__(self, nome, desc):
        self.nome = nome
        self.desc = desc
        self.completada = False

class TodoList:
    def __init__(self):
        self.tarefa = []

    def adicionar_tarefa(self, nome, desc):
        tarefa = Tarefa(nome, desc)
        self.tarefa.append(tarefa)

    def exibir_tarefa(self):
        if not self.tarefa:
            print("Não tem tarefas registradas.")
        else:
            print("Tarefas: ")
            for indice, tarefa in enumerate(self.tarefa, start=1):
                status = "Concluida" if tarefa.completada else "Pendente"
                print(f"{indice}. {tarefa.nome} - {tarefa.desc} - Status {status}")

    def marcar_concluida(self):
        if not self.tarefa:
            print("Sem tarefas para concluir!")
        else: 
            print("Escolha sua tarefa para concluir: ")
            # percorre no indice e enumera o indince comecando de 1
            for indice, tarefa in enumerate(self.tarefa, start=1):
                #marca o status como concluida na variavel tarefa.completada, caso contrario marca como 'pendente'
                status = "Concluida" if tarefa.completada else "Pendente"
                #mostra o indice, nome e status
                print(f"{indice}. {tarefa.nome} - {status}")
            opcao = input("Digite o numero da tarefa: ")
            try:
                opcao = int(opcao)
                # percorrer caso a opção 1 que garante que as tarefas tenham pelo menos uma tarefa pendente
                if 1 <= opcao <= len(self.tarefas):
                    #busca a tarefa inserida para marcar como completada (=true)
                    self.tarefas[opcao - 1].completada = True
                    print("Tarefa marcada como concluída!")
                else:
                    print("Numero da tarefa errado!")
            # esse except é obrigatorio
            except ValueError:
                print("Erro: Insira um numero válido!")

def main():
    todo_list = TodoList()
    while True:

        print("1. Adicionar Tarefa")
        print("2. Exibir Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Excluir Tarefa")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":

            nome = input("Nome da tarefa: ")
            desc = input("Descrição da tarefa: ")

            todo_list.adicionar_tarefa(nome, desc)

        elif escolha == "2":
            todo_list.exibir_tarefa()

        elif escolha == "5":
            break

if __name__ == "__main__":
    main()
