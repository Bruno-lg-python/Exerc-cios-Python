# **Jokenpô - Pedra, Papel, Tesoura**

Este projeto é uma implementação do jogo clássico Jokenpô (Pedra, Papel e Tesoura) em Python, onde o usuário joga contra o computador. O jogo continua até que um dos jogadores (usuário ou computador) vença 5 partidas, e ao final, o placar é exibido.

## Índice

1. [Descrição](#descrição)
2. [Requisitos](#requisitos)
3. [Instalação](#instalação)
4. [Uso](#uso)
5. [Regras do Jogo](#regras-do-jogo)
6. [Funcionalidades](#funcionalidades)
7. [Exemplo de Execução](#exemplo-de-execução)
8. [Contribuições](#contribuições)
9. [Licença](#licença)
10. [Contato](#contato)

---

## Descrição

O jogo permite que o usuário escolha entre "Pedra", "Papel" ou "Tesoura" e jogue contra o computador, que faz uma escolha aleatória. O resultado de cada rodada é mostrado, e o jogo continua até que um dos jogadores alcance 5 vitórias. A cada rodada, o terminal é limpo e o placar atualizado é mostrado.

## Requisitos

- Python 3.x
- Biblioteca `time` para pausas entre as mensagens (integrada ao Python).
- Biblioteca `random` para gerar a escolha do computador (integrada ao Python).

---

## Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/Bruno-lg-python/Exerc-cios-Python/Jô_Ken_Pô.git


## Uso

2. Execute o script Python para iniciar o jogo:

   ```bash
   python Jô_Ken_Pô.py

2. O jogo perguntará ao usuário para escolher entre:

  - [1] Pedra
  - [2] Papel
  - [3] Tesoura

3. O jogo exibirá o placar após cada rodada e perguntará se o usuário deseja continuar. O jogo será reiniciado até que o usuário escolha sair.


## Regras do Jogo
As regras seguem o padrão do jogo Jokenpô:

  - Pedra ganha de Tesoura, mas perde para Papel.
  - Papel ganha de Pedra, mas perde para Tesoura.
  - Tesoura ganha de Papel, mas perde para Pedra.

## Funcionalidades
  - Jogar contra o computador.
  - Exibir o placar atualizado após cada rodada.
  - Animação de contagem (Jô-Kên-Pô) entre cada rodada.
  - Placar acumulado até que um jogador (usuário ou computador) atinja 5 vitórias.
  - Limpeza automática do terminal após cada rodada para facilitar a visualização.

## Exemplo de Execução

    ESCOLHA ENTRE:
        [1] PEDRA
        [2] PAPEL
        [3] TESOURA
    QUAL OPÇÃO VOCÊ ESCOLHE: 1

        JÔ
        KÊN
        PÔ
    O USUÁRIO ESCOLHEU PEDRA
    E O COMPUTADOR ESCOLHEU TESOURA
    O RESULTADO: VOCÊ GANHOU

    Placar Atual:
    Você: 1
    Computador: 0

    DESEJA CONTINUAR? [S/N]: s


## Contribuições
Se você quiser contribuir para melhorar o jogo, siga estes passos:

  1. Faça um fork do repositório.
  2. Crie uma nova branch com a sua feature ou correção: git checkout -b minha-feature.
  3. Faça commit das suas alterações: git commit -m 'Adiciona minha feature'.
  4. Envie para a branch principal: git push origin minha-feature.
  5. Abra um Pull Request.

## Contato
BRUNO GUSTAVO - GitHub - bgustavo1910@gmail.com
