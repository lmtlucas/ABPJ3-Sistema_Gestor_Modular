print('  - - - - - - - -\n| GESTOR ESCOLAR |\n  - - - - - - - -\n')

cadastro = {}

def cadastrar():
    aluno = input('Insira o nome do aluno para cadastrar: ')
    notas = []
    for i in range(4):
        nota = int(input('Insira uma nota por bimestre (total 4 notas): '))
        notas.append(nota)
    cadastro.setdefault(aluno, notas)
    print(f'\nAluno "{aluno}" e notas "{notas}" cadastrados')
    return cadastro

def exibirCadastro():
    for nome, nota in cadastro.items():
        print(f'Aluno(a) {nome} tirou as notas: {nota}')

def exibirSituacao():
    aluno = input('Insira o nome do aluno exatamente como cadastrado para exibir a situação: ')
    media = sum(cadastro.get(aluno)) / len(cadastro.get(aluno))
    match media: 
        case media if media > 6:
            situacao = "APROVADO"
        case  media if media < 4:
            situacao = "REPROVADO"
        case _:
            situacao = "RECUPERAÇÃO"
    print(f'\nO(a) Aluno(a) {aluno} tirou a média {media} e sua situação é {situacao}')


while True:
    print('\n| MENU |\n1 -> Cadastrar\n2 -> Exibir cadastros\n3 -> Verificar situação do aluno(a)\n0 -> Sair\n')
    opcao = int(input("Digite o número da opção desejada: "))
    match opcao:
        case 1:
            cadastrar()
        case 2:
            exibirCadastro()
        case 3:
            exibirSituacao()
        case 0:
            print("FIM")
            break
        case _:
            print("Valor não reconhecido")
