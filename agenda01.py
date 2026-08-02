from time import sleep
import datetime
with open ("logins.txt", "a"):
    pass
def traco (quantidade=40):
    print('-'*quantidade)

print('Seja bem vindo a sua agenda pessoal')
traco()
print('login da sua agenda')
#Login do usuário
login_realizado = False
while True:
    nome = input('Nome de usuário: ').strip().title()
    senha = input('Senha: ').strip()
    sleep(1)
    encontrou_usuario = False
    #Verifica se o usuário existe no arquivo logins.txt
    with open ("logins.txt", "r", encoding='utf-8') as arquivo:
        for linha in arquivo:
            usuario, senha_arquivo = linha.strip().split(';')
            if nome == usuario:
                encontrou_usuario = True
                #Se o usuário existir, verifica se a senha está correta
                if senha == senha_arquivo:
                    print('login realizado com sucesso!')
                    traco()
                    login_realizado = True
                    break
                else:
                    print('Senha incorreta! Tente novamente.')
                break
    #Se o usuário não existir, pergunta se deseja criar um novo usuário
    if not encontrou_usuario:
        print('Usuário não encontrado!')
        while True:
            resp = input('Deseja criar um novo usúario? [S/N]: ').strip().upper()
            if not resp:
                print('Opção inválida! Tente novamente.')
                continue

            resp = resp[0]

            if resp == "N":
                print('Tente novamente')
                break
            #Se o usuário quiser criar um novo usuário, pede o nome e a senha e salva no arquivo logins.txt
            elif resp == "S":
                print('Crie seu novo usuário')
                while True:
                    nome = input('Nome de usuário: ').strip().title()
                    encontrou_usuario = False
                    sleep(1)
                    #Verifica se o usuário já existe no arquivo logins.txt
                    with open ("logins.txt" , "r", encoding='utf-8') as arquivo:
                        for linha in arquivo:
                            usuario = linha.strip().split(';')[0]
                            if nome == usuario:
                                encontrou_usuario = True
                                break
                    if encontrou_usuario:
                        print('O usuário já existe! Tente novamente.')
                    else:
                        break
                while True:
                    senha = input('Senha: ').strip()
                    if senha == '':
                        print('A senha não pode ser vazia! Tente novamente.')
                        continue
                    else:
                        break
                with open ("logins.txt", "a", encoding='utf-8') as arquivo:
                    arquivo.write(f'{nome};{senha}\n')
                    #Após criar o usuário, informa que o usuário foi criado com sucesso e pede para fazer o login novamente
                    print('Usuário criado com sucesso! Faça o login novamente.')
                    break
            elif resp not in ["S", "N"]:
                print('Opção inválida! Tente novamente.')
                continue
    if login_realizado:
        break
#Após o login, mostra as tarefas do usuário
traco()
print(f'Bem vindo {nome}!')
#Loop principal do programa, onde o usuário pode adicionar, finalizar ou sair do programa varias vezes
while True:
    sleep(1)
    traco()
    print('Suas tarefas:')
    with open (f"tarefas_{nome}.txt", "a"):
        pass
    with open (f"tarefas_{nome}.txt", "r", encoding='utf-8') as arquivo:
        linha = arquivo.readlines()
        if not linha:
            print('Você não possui tarefas cadastradas')
        else:
            for i, tarefa in enumerate(linha):
                print(f'{i+1} - {tarefa.strip()}')
    #Menu de opções
    traco()
    print('1 - Adicionar tarefa\n2 - Finalizar tarefa\n3 - Sair')
    while True:
        resposta = input('Escolha uma opção: ').strip()
        #Se o usuário escolher a opção 1, pede para digitar a tarefa e salva no arquivo tarefas_{nome}.txt com a data de criação
        if resposta == '1':
            tarefa = input('Digite a tarefa: ').strip()
            if tarefa == '':
                print('A tarefa não pode ser vazia! Tente novamente.')
                continue
            else:
                with open (f"tarefas_{nome}.txt", "a", encoding='utf-8') as arquivo:
                    arquivo.write(f'{tarefa} | Data de criação: {datetime.datetime.now().strftime("%d/%m/%Y")}\n')
                sleep(1)
                break
        #Se o usuário escolher a opção 2, mostra as tarefas cadastradas e pede para digitar o número da tarefa que deseja finalizar, removendo-a do arquivo tarefas_{nome}.txt
        if resposta == '2':
            with open (f"tarefas_{nome}.txt", "r", encoding='utf-8') as arquivo:
                linha = arquivo.readlines()
                if not linha:
                    print('Você não possui tarefas cadastradas')
                else:
                    print('Suas tarefas:')
                    for i, tarefa in enumerate(linha):
                        print(f'{i+1} - {tarefa.strip()}')
                    try:
                        escolha = int(input('Digite o número da tarefa que deseja finalizar: '))-1
                        if escolha < 0 or escolha >= len(linha):
                            print('Opção inválida! Tente novamente.')
                        else:
                            print(f'Tarefa "{linha[escolha].strip()}" sendo finalizada e removida da lista de tarefas.')
                            linha.pop(escolha)
                            with open (f"tarefas_{nome}.txt", "w", encoding='utf-8') as arquivo:
                                arquivo.writelines(linha)
                            sleep(1)
                            print('Tarefa finalizada com sucesso!')
                    except ValueError:
                        print('Digite apenas números! Tente novamente')
            break
        elif resposta == '3':
            print('Saindo...')
            sleep(1)
            print('Até mais')
            exit()
        elif resposta not in ['1', '2', '3']:
            print('Opção inválida! Tente novamente.')
