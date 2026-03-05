cadastro = {}
def cadastrar():
    aluno = input('\n> Insira o nome do aluno para cadastrar: ').upper()
    notas = []
    for i in range(4): # pede 4 x para o usuario inserir a nota
        nota = int(input('> Insira uma nota por bimestre (total 4 notas): '))
        notas.append(nota) # inseri a nota na lista notas
    cadastro.setdefault(aluno, notas) # inseri aluno(chave) e a lista notas(valor) no dicionario (cadastro)
    print(f'\nAluno "{aluno}" e notas "{notas}" cadastrados')
    return cadastro

def exibirCadastro():
    for nome, nota in cadastro.items(): # percorrer todas as chaves(nome) e valor(nota) dentro do dicionario (cadastro)
        print(f'\n- Aluno(a): {nome} | Notas: {nota}')

def exibirSituacao():
    while True: # loop para verificar se o usuario está digitando o cadastro correto e pedir para ele digitar novamente ou sair da função
        aluno = input('\n> Insira o nome do aluno exatamente como cadastrado para exibir a situação ou "0" para voltar ao menu: ').upper()
        if aluno == '0':
            break
        elif aluno in cadastro.keys(): # procura aluno dentro das chaves na lista, para validar a existencia do item
            media = sum(cadastro.get(aluno)) / len(cadastro.get(aluno)) # calcula a media usando a função sum para somar os valores puxados com .get / len para contar quantidade de valores puxados com .get
            match media: # comparando para verificar a condição
                case media if media > 6:
                    situacao = "APROVADO"
                case  media if media < 4:
                    situacao = "REPROVADO"
                case _:
                    situacao = "RECUPERAÇÃO"
            print(f'\nO(a) Aluno(a) {aluno} tirou a média {media} e sua situação é {situacao}')
            break   
        else:
            print('Cadastro não encontrado')

def excluirCadastro():
    while True:
        exclua = input('\n> Insira o nome do aluno para apagar do cadastro ou "0" para voltar: ').upper()
        if exclua == '0':
            break
        elif exclua in cadastro.keys():
            del cadastro[exclua]
            print(f'\nAluno "{exclua}" apagado do cadastro')
            break
        else:
            print('Cadastro não encontrado')
    return cadastro
