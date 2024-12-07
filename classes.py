class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def __str__(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}"


class Aluno(Pessoa):
    def __init__(self, nome, cpf, matricula):
        super().__init__(nome, cpf)
        self.matricula = matricula

    def __str__(self):
        return f"{super().__str__()}, Matrícula: {self.matricula}"


class Professor(Pessoa):
    def __init__(self, nome, cpf, disciplina):
        super().__init__(nome, cpf)
        self.disciplina = disciplina

    def __str__(self):
        return f"{super().__str__()}, Disciplina: {self.disciplina}"


class Curso:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = set()  # Conjunto para armazenar alunos
        self.professores = set()  # Conjunto para armazenar professores

    def adicionar_aluno(self, aluno):
        self.alunos.add(aluno)

    def remover_aluno(self, aluno):
        self.alunos.discard(aluno)

    def adicionar_professor(self, professor):
        self.professores.add(professor)

    def remover_professor(self, professor):
        self.professores.discard(professor)

    def exibir_info(self):
        print(f"Curso: {self.nome}")
        print("Alunos:")
        for aluno in self.alunos:
            print(f"  - {aluno}")
        print("Professores:")
        for professor in self.professores:
            print(f"  - {professor}")


# Sistema de Testes

# Cadastro de Alunos
aluno1 = Aluno("João Silva", "12345678901", "A001")
aluno2 = Aluno("Maria Oliveira", "98765432100", "A002")

# Cadastro de Professores
professor1 = Professor("Carlos Mendes", "11122233344", "Matemática")
professor2 = Professor("Ana Lima", "55566677788", "História")

# Criação de Cursos
curso1 = Curso("Engenharia")
curso2 = Curso("Letras")

# Adicionando Alunos e Professores aos Cursos
curso1.adicionar_aluno(aluno1)
curso1.adicionar_aluno(aluno2)
curso1.adicionar_professor(professor1)

curso2.adicionar_aluno(aluno1)
curso2.adicionar_professor(professor2)

# Exibindo Informações dos Cursos
curso1.exibir_info()
print()
curso2.exibir_info()
