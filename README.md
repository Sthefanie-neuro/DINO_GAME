# Dino Game com Pygame

Uma recriação do clássico "Dino Game" com funcionalidades expandidas, desenvolvido inteiramente em Python com a biblioteca Pygame.

Este projeto vai além do básico, oferecendo um menu principal completo, sistema de pontuação por moedas, placar de recordes persistente e múltiplas telas de jogo. O jogador controla um dinossauro que deve pular para desviar de obstáculos e coletar moedas para maximizar sua pontuação, tudo isso enquanto a velocidade aumenta progressivamente.

![Gameplay do Dino Game](Dino_game-ezgif.com-video-to-gif-converter.gif)

## 🚀 Funcionalidades Principais

-   **Menu Principal Completo:** Navegue entre as opções de "Iniciar Jogo", "Instruções", "Recordes" e "Sair".
-   **Sistema de Pontuação Duplo:** O jogo rastreia tanto as **moedas coletadas** (`pontos`) quanto o **tempo sobrevivido** (`tempo`).
-   **Salvamento de Recordes:** As maiores pontuações e tempos são salvos em um arquivo `recordes.txt`, persistindo entre as sessões de jogo.
-   **Telas de Instruções e Recordes:** Telas dedicadas que podem ser acessadas pelo menu para visualizar os controles ou os recordes atuais.
-   **Coleta de Moedas:** Moedas animadas aparecem em locais aleatórios para serem coletadas, adicionando um novo objetivo ao jogo.
-   **Obstáculos Aleatórios:** O jogo alterna aleatoriamente entre cactos no chão e dinossauros voadores.
-   **Aumento Progressivo de Velocidade:** A cada 100 unidades de tempo, a velocidade do jogo aumenta, elevando a dificuldade.
-   **Efeitos Sonoros:** Sons distintos para pulo, coleta de moeda, pontuação por tempo e colisão.
-   **Tela de Game Over Detalhada:** Ao colidir, a tela de "Game Over" exibe a pontuação final e os recordes atuais, com a opção de reiniciar a partida.

## 🕹️ Como Jogar

### Menu Principal
-   **Iniciar Jogo:** Pressione `Enter`.
-   **Ver Instruções:** Pressione a tecla `I`.
-   **Ver Recordes:** Pressione a tecla `R`.
-   **Sair do Jogo:** Pressione a tecla `S`.
-   **Voltar ao Menu:** Nas telas de Instruções ou Recordes, pressione `Esc`.

### Durante o Jogo
-   **Pular:** Pressione a `Barra de Espaço`.
-   **Reiniciar o Jogo:** Após perder (Game Over), pressione a tecla `R`.

## 📂 Estrutura de Arquivos

Para que o jogo funcione corretamente, os arquivos e pastas do projeto devem seguir a seguinte estrutura:

Dino_game/
|
|-- dino_game.py             # Script principal do jogo
|-- README.md                # Este arquivo
|-- recordes.txt             # Arquivo para salvar recordes (será criado automaticamente)
|
|-- images/
|   |-- lattes.png
|   |-- obstaculos.png
|   |-- dino_walk.png
|   |-- coin_new.png
|   |-- Platform.png
|   |-- dino_menu.png
|
-- tracksound/ |-- death_sound.wav |-- jump_sound.wav |-- score_sound.wav -- smw_coin.wav

**Atenção:** Certifique-se de que as pastas `images` e `tracksound` e todos os seus respectivos arquivos estejam presentes na mesma pasta que o script `dino.py`.

## 🛠️ Instalação e Execução

Siga os passos abaixo para executar o projeto em sua máquina local.

**Pré-requisitos:**
-   [Python 3](https://www.python.org/downloads/) instalado.

**Passos:**

1.  **Clone o repositório:**
    ```sh
    git clone [https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git](https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git)
    ```

2.  **Navegue até a pasta do projeto:**
    ```sh
    cd NOME-DA-PASTA
    ```

3.  **(Opcional mas recomendado) Crie e ative um ambiente virtual:**
    ```sh
    # Criar ambiente virtual
    python -m venv venv

    # Ativar no Windows
    .\venv\Scripts\activate

    # Ativar no macOS/Linux
    source venv/bin/activate
    ```

4.  **Instale as dependências (Pygame):**
    ```sh
    pip install pygame
    ```

5.  **Execute o jogo:**
    ```sh
    python dino_game.py
    ```

## 💻 Tecnologias Utilizadas

-   **Python**
-   **Pygame**
 
