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
                print("===========================================")

    def marcar_concluida(self, indice):        
        if indice >= 0 and indice < len(self.tarefa):

            self.tarefa[indice].completada = True
            print("Tarefa marcada como concluída!")

        else:
            print("Numero da tarefa inválido!")

    def excluir_tarefa(self, indice):
        if indice >= 0 and indice < len(self.tarefa):
            tarefa_exlcuida = self.tarefa.pop(indice)
            print("Tarefa Removida: ", tarefa_exlcuida.nome)
            print("===========================================")
            return tarefa_exlcuida
        else:
            print("Não removido! Tarefa Inexistente!")
            return None #para indicar que nenhuma tarefa foi excluida

def main():
    todo_list = TodoList()
    while True:

        print("---------------------------")
        print("1. Adicionar Tarefa")
        print("2. Exibir Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Excluir Tarefa")
        print("5. Sair")
        print("---------------------------")

        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":

            nome = input("Nome da tarefa: ")
            desc = input("Descrição da tarefa: ")

            todo_list.adicionar_tarefa(nome, desc)

        elif escolha == "2":
            todo_list.exibir_tarefa()

        elif escolha == "3":
            todo_list.exibir_tarefa()

            indice = int(input("Digite o número da Tarefa a ser concluída: "))
            todo_list.marcar_concluida(indice - 1)
        
        elif escolha == "4":
            todo_list.exibir_tarefa()

            indice = int(input("Digite o número da Tarefa a ser excluída: "))
            todo_list.excluir_tarefa(indice - 1)

        elif escolha == "5":
            break

if __name__ == "__main__":
    main()
