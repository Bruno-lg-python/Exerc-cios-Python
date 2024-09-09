import os
from random import randint
from time import sleep

# Função para limpar o terminal (compatível com Windows e Unix)
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função que converte a escolha numérica em string
def escolha(opc):
    match opc:
        case 1:
            return 'PEDRA'
        case 2:
            return 'PAPEL'
        case 3:
           return 'TESOURA'
        case _:
            return "Escolha inválida!"
        
# Função para gerar uma escolha aleatória para o computador
def gerar():
    return randint(1, 3)

# Função que verifica quem ganhou a rodada
def verificar(pc, usuario):
    match (pc, usuario):
        case _ if pc == usuario:  # Condição de empate
            return '\033[33mEMPATOU\033[0m'
        case _ if pc < usuario:  # Condições de vitória do computador
            return '\033[31mCOMPUTADOR \033[0m'
        case _:
            return '\033[32mVOCÊ \033[0m'  # Condição de vitória do jogador

# Função principal do jogo
def jogar():
    jogador_vitorias = 0
    computador_vitorias = 0

    while True:
        # Limpa o terminal e exibe o placar atualizado
        limpar_terminal()
        print(f"PLACAR: JOGADOR {jogador_vitorias} x {computador_vitorias} COMPUTADOR")
        print("O jogo termina quando alguém chegar a 5 vitórias.\n")

        # Verifica se há um vencedor (5 vitórias)
        if jogador_vitorias == 5:
            print("VOCÊ É O VENCEDOR FINAL!")
            break
        elif computador_vitorias == 5:
            print("O COMPUTADOR É O VENCEDOR FINAL!")
            break

        # Gerando a escolha do computador
        pc = gerar()

        # Pedindo a escolha do usuário
        while True:
            try:
                usuario = int(input('''ESCOLHA ENTRE:
        [1] PEDRA
        [2] PAPEL
        [3] TESOURA
QUAL OPÇÃO VOCÊ ESCOLHE: '''))
                if usuario in [1, 2, 3]:
                    break  # Sai do loop se a escolha for válida
                else:
                    print("Escolha inválida! Por favor, escolha 1, 2 ou 3.")
            except ValueError:
                print("Entrada inválida! Por favor, insira um número (1, 2 ou 3).")

        # Convertendo os números em strings de opções (PEDRA, PAPEL, TESOURA)
        usuario_escolha = escolha(usuario)
        pc_escolha = escolha(pc)

        # Verificando o resultado da rodada
        resultado = verificar(pc, usuario)

        # Exibindo o resultado com efeito de suspense
        print('''
        JÔ''')
        sleep(1)
        print('''
        KÊN''')
        sleep(1)
        print('''
        PÔ''')
        sleep(1)
        print(f'''O USUÁRIO ESCOLHEU {usuario_escolha}
E O COMPUTADOR ESCOLHEU {pc_escolha}
O GANHADOR DA RODADA: {resultado}''')

        # Atualizando o placar
        if resultado == '\033[32mVOCÊ \033[0m':
            jogador_vitorias += 1
        elif resultado == '\033[31mCOMPUTADOR \033[0m':
            computador_vitorias += 1

        # Perguntar se o usuário deseja continuar
        while True:
            resposta = input("DESEJA CONTINUAR? [S/N]: ").strip().lower()
            if resposta == 's':
                break  # Sai do loop para continuar o jogo
            elif resposta == 'n':
                print("Você escolheu sair. Até a próxima!")
                return  # Encerra o jogo
            else:
                print("Opção inválida! Digite 'S' para sim ou 'N' para não.")

# Iniciar o jogo
jogar()
