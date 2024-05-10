from tkinter import *

class Tarefa:
    def __init__(self, nome, desc):
        self.nome = nome
        self.desc = desc
        self.completada = False

class TodoList:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, nome, desc):
        tarefa = Tarefa(nome, desc)
        self.tarefas.append(tarefa)

    def exibir_tarefas(self):
        if not self.tarefas:
            print("Não há tarefas registradas.")
        else:
            print("Tarefas: ")
            for indice, tarefa in enumerate(self.tarefas, start=1):
                status = "Concluída" if tarefa.completada else "Pendente"
                print(f"{indice}. {tarefa.nome} - {tarefa.desc} - Status: {status}")
                print("===========================================")

    def marcar_concluida(self, indice):
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice].completada = True
            print("Tarefa marcada como concluída!")
        else:
            print("Número da tarefa inválido!")

    def excluir_tarefa(self, indice):
        if 0 <= indice < len(self.tarefas):
            tarefa_excluida = self.tarefas.pop(indice)
            print("Tarefa removida:", tarefa_excluida.nome)
            print("===========================================")
            return tarefa_excluida
        else:
            print("Não removido! Tarefa inexistente!")
            return None

def adicionar_tarefa_interface(todo_list, nome_entry, desc_entry):
    nome = nome_entry.get()
    desc = desc_entry.get()
    todo_list.adicionar_tarefa(nome, desc)
    nome_entry.delete(0, END)
    desc_entry.delete(0, END)

def criar_interface_grafica(todo_list):
    janela = Tk()
    janela.title("To Do List")

    nome_label = Label(janela, text="Nome da Tarefa:")
    nome_label.grid(row=0, column=0, padx=10, pady=5)
    nome_entry = Entry(janela)
    nome_entry.grid(row=0, column=1, padx=10, pady=5)

    desc_label = Label(janela, text="Descrição da Tarefa:")
    desc_label.grid(row=1, column=0, padx=10, pady=5)
    desc_entry = Entry(janela)
    desc_entry.grid(row=1, column=1, padx=10, pady=5)

    adicionar_button = Button(janela, text="Adicionar Tarefa",
                              command=lambda: adicionar_tarefa_interface(todo_list, nome_entry, desc_entry))
    adicionar_button.grid(row=2, columnspan=2, padx=10, pady=5)

    exibir_button = Button(janela, text="Exibir Tarefas", command=todo_list.exibir_tarefas)
    exibir_button.grid(row=3, columnspan=2, padx=10, pady=5)

    marcar_button = Button(janela, text="Marcar Tarefa como Concluída", command=lambda: todo_list.marcar_concluida(0))
    marcar_button.grid(row=4, columnspan=2, padx=10, pady=5)

    excluir_button = Button(janela, text="Excluir Tarefa", command=lambda: todo_list.excluir_tarefa(0))
    excluir_button.grid(row=5, columnspan=2, padx=10, pady=5)

    sair_button = Button(janela, text="Sair", command=janela.quit)
    sair_button.grid(row=6, columnspan=2, padx=10, pady=5)

    janela.mainloop()

def main():
    todo_list = TodoList()
    criar_interface_grafica(todo_list)

if __name__ == "__main__":
    main()
