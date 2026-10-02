# Estrutura inicial do sistema

alunos = []


# Função para adicionar aluno

def adicionar_aluno():
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))

    nota = float(input("Digite a nota do aluno: "))


    # Validação da nota

    while nota < 0 or nota > 10:
        print("Nota inválida! Digite uma nota entre 0 e 10.")
        nota = float(input("Digite a nota do aluno: "))


    # Criando o dicionário do aluno

    aluno = {
        "nome": nome,
        "idade": idade,
        "nota": nota
    }


    # Adicionando o aluno à lista

    alunos.append(aluno)

    print("Aluno cadastrado com sucesso!")


# Função para listar alunos

def listar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        for aluno in alunos:
            print("Nome:", aluno["nome"])
            print("Idade:", aluno["idade"])
            print("Nota:", aluno["nota"])


# Função para buscar aluno

def buscar_aluno():
    nome_busca = input("Digite o nome do aluno que deseja buscar: ")

    encontrado = False

    for aluno in alunos:
        if aluno["nome"] == nome_busca:
            print("Aluno encontrado!")
            print("Nome:", aluno["nome"])
            print("Idade:", aluno["idade"])
            print("Nota:", aluno["nota"])

            encontrado = True

    if not encontrado:
        print("Aluno não encontrado.")


# Função para remover aluno

def remover_aluno():
    nome_remover = input("Digite o nome do aluno que deseja remover: ")

    encontrado = False

    for aluno in alunos:
        if aluno["nome"] == nome_remover:
            alunos.remove(aluno)
            print("Aluno removido com sucesso!")

            encontrado = True
            break

    if not encontrado:
        print("Aluno não encontrado.")


# Função para calcular a média geral

def calcular_media():
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    soma = 0

    for aluno in alunos:
        soma += aluno["nota"]

    media = soma / len(alunos)

    print("Média geral das notas:", media)


# Menu principal

while True:
    print("\n===== SISTEMA DE CADASTRO DE ALUNOS =====")
    print("1 - Adicionar aluno")
    print("2 - Listar todos os alunos")
    print("3 - Buscar aluno pelo nome")
    print("4 - Remover aluno")
    print("5 - Mostrar média geral das notas")
    print("6 - Sair")

    opcao = int(input("Digite uma opção: "))

    if opcao == 1:
        adicionar_aluno()

    elif opcao == 2:
        listar_alunos()

    elif opcao == 3:
        buscar_aluno()

    elif opcao == 4:
        remover_aluno()

    elif opcao == 5:
        calcular_media()

    elif opcao == 6:
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida! Digite uma opção de 1 a 6.")