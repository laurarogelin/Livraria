class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True  

    def __str__(self):
        return f"{self.titulo} por {self.autor} {'(Disponível)' if self.disponivel else '(Emprestado)'}"


class Biblioteca:
    def __init__(self):
        self.livros = []

    def add_livro(self, livro):
        for l in self.livros:
            if l.titulo == livro.titulo and l.autor == livro.autor:
                return f"O livro '{livro.titulo}' de {livro.autor} já está na biblioteca."
        self.livros.append(livro)
        return f"Livro '{livro.titulo}' de {livro.autor} adicionado à biblioteca."

    def listar_livros(self):
        if not self.livros:
            return "Não há livros cadastrados na biblioteca."
        return "\n".join(str(livro) for livro in self.livros)

    def emprestar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                if livro.disponivel:
                    livro.disponivel = False
                    return f"Livro '{titulo}' emprestado."
                else:
                    return f"O livro '{titulo}' já está emprestado."
        return f"O livro '{titulo}' não está na biblioteca."

    def devolver_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                if not livro.disponivel:
                    livro.disponivel = True
                    return f"O livro '{titulo}' foi devolvido."
                else:
                    return f"O livro '{titulo}' já está disponível na biblioteca."
        return f"O livro '{titulo}' não pertence à biblioteca."


def menu():
    biblioteca = Biblioteca()
    
    while True:
        print("\nMenu da Biblioteca:")
        print("1. Adicionar Livro")
        print("2. Listar Livros")
        print("3. Emprestar Livro")
        print("4. Devolver Livro")
        print("5. Sair")
        
        opcao = input("Escolha uma opção (1-5): ")

        if opcao == "1":
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            livro = Livro(titulo, autor)
            print(biblioteca.add_livro(livro))

        elif opcao == "2":
            livros = biblioteca.listar_livros()
            print(livros)

        elif opcao == "3":
            titulo = input("Digite o título do livro a ser emprestado: ")
            print(biblioteca.emprestar_livro(titulo))

        elif opcao == "4":
            titulo = input("Digite o título do livro a ser devolvido: ")
            print(biblioteca.devolver_livro(titulo))

        elif opcao == "5":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 5.")



menu()
