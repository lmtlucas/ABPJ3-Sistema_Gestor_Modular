import modulo as md #importando o modulo com funções e apelidando de md

print('  - - - - - - - -\n| GESTOR ESCOLAR |\n  - - - - - - - -\n')

while True:
    print('\n| MENU |\n1 -> Cadastrar\n2 -> Exibir cadastros\n3 -> Verificar situação do aluno(a)\n4 -> Excluir aluno do cadastro\n0 -> Sair\n')
    opcao = (input("> Digite o número da opção desejada: "))
    match opcao:
        case '1':
            md.cadastrar()
        case '2':
            md.exibirCadastro()
        case '3':
            md.exibirSituacao()
        case '4':
            md.excluirCadastro()
        case '0':
            print("FIM")
            break
        case _:
            print("Valor não reconhecido")
