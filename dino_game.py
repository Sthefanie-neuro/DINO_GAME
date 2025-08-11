import pygame
from pygame.locals import *
from sys import exit
import os
from random import randrange, choice

pygame.init()
pygame.mixer.init()

diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, 'images')
diretorio_sons = os.path.join(diretorio_principal, 'tracksounds')


largura = 640
altura = 480
branco = (255,255,255)
preto = (0,0,0)
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Dino Game')

screen = pygame.display.set_mode((largura, altura))
background = pygame.image.load(os.path.join(diretorio_imagens,"lattes.png")).convert_alpha()
background = pygame.transform.scale(background, (largura, altura)) 


sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens,"obstaculos.png")).convert_alpha()
sprite_dino = pygame.image.load(os.path.join(diretorio_imagens,"dino_walk.png")).convert_alpha()
sprite_coin = pygame.image.load(os.path.join(diretorio_imagens,"coin_new.png")).convert_alpha()
sprite_floor = pygame.image.load(os.path.join(diretorio_imagens,"Platform.png")).convert_alpha()

som_colisao = pygame.mixer.Sound(os.path.join(diretorio_sons, "death_sound.wav"))
som_colisao.set_volume(1)

som_pontuacao = pygame.mixer.Sound(os.path.join(diretorio_sons, "smw_coin.wav"))
som_pontuacao.set_volume(1)

som_tempo = pygame.mixer.Sound(os.path.join(diretorio_sons, "score_sound.wav"))
som_tempo.set_volume(1)

colidiu = False
pontuou = False

escolha_obstaculo = choice([0, 1])
tempo = 0
pontos = 0
velocidade_jogo = 10

def exibe_mensagem(msg, tamanho, cor):
    fonte = pygame.font.SysFont('Open Sans', tamanho, True, False)
    mensagem = f'{msg}'
    texto_formatado = fonte.render(mensagem, True, cor)
    return texto_formatado

def reiniciar_jogo():
    global tempo, velocidade_jogo, colidiu, escolha_obstaculo, pontos, moeda
    tempo = 0
    pontos = 0
    velocidade_jogo = 10
    colidiu = False
    pontuou = False
    dino.rect.y = altura-64 - 96//2
    dino.pulo = False
    dino_voador.rect.x = largura
    cacto.rect.x = largura
    moeda.rect.x = largura
    escolha_obstaculo = choice([0, 1])

def carregar_recordes():
    try:
        with open('recordes.txt', 'r') as arquivo:
            dados = arquivo.read().splitlines()
            if len(dados) == 2:
                maior_pontuacao = int(dados[0])
                maior_tempo = int(dados[1])
                return maior_pontuacao, maior_tempo
    except FileNotFoundError:
        return 0, 0  # Valores iniciais, caso o arquivo não exista
    return 0, 0

def salvar_recordes(maior_pontuacao, maior_tempo):
    with open('recordes.txt', 'w') as arquivo:
        arquivo.write(f"{maior_pontuacao}\n")
        arquivo.write(f"{maior_tempo}")


# Função de menu
def mostrar_menu():
    while True:
        tela.fill(branco)
        tela.blit(background, (0, 0))

        # Exibe o título
        titulo = exibe_mensagem("Dino Game", 60, preto)
        tela.blit(titulo, (largura // 2 - titulo.get_width() // 2, altura // 4))
        dino_menu = pygame.image.load(os.path.join(diretorio_imagens, "dino_menu.png")).convert_alpha()
        tela.blit(dino_menu, (largura // 2 - dino_menu.get_width() // 2, altura // 4 + titulo.get_height() + 10))  

        # Exibe as opções do menu
        op_iniciar = exibe_mensagem("Iniciar Jogo (enter)", 35, preto)
        tela.blit(op_iniciar, (largura // 2 - op_iniciar.get_width() // 2, altura // 2))

        op_instrucoes = exibe_mensagem("Instruções (I)", 35, preto)
        tela.blit(op_instrucoes, (largura // 2 - op_instrucoes.get_width() // 2, altura // 2 + 50))

        op_records = exibe_mensagem("Recordes (R)", 35, preto)
        tela.blit(op_records, (largura // 2 - op_records.get_width() // 2, altura // 2 + 100))

        op_sair = exibe_mensagem("Sair (S)", 35, preto)
        tela.blit(op_sair, (largura // 2 - op_sair.get_width() // 2, altura // 2 + 150))

        pygame.display.flip()

        # Espera por uma ação do jogador
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    return "iniciar"
                if event.key == K_i:
                    return "instrucoes"
                if event.key == K_r:
                    return "records"
                if event.key == K_s:
                    pygame.quit()
                    exit()

# Função de instruções
def mostrar_instrucoes():
    while True:
        tela.fill(branco)
        tela.blit(background, (0, 0))

        instrucoes = [
            "Instruções:",
            "1. Use a barra de espaço para pular.",
            "2. Colete moedas para pontuar.",
            "3. Evite os obstáculos.",
            "4. Pressione 'R' para reiniciar após o Game Over."
        ]

        for i, texto in enumerate(instrucoes):
            linha = exibe_mensagem(texto, 30, preto)
            tela.blit(linha, (largura // 2 - linha.get_width() // 2, altura // 4 + i * 40))

        voltar = exibe_mensagem("Pressione 'Esc' para voltar", 30, preto)
        tela.blit(voltar, (largura // 2 - voltar.get_width() // 2, altura - 60))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return

# Função para mostrar os records
def mostrar_records():
    maior_pontuacao, maior_tempo = carregar_recordes()

    while True:
        tela.fill(branco)
        tela.blit(background, (0, 0))

        recorde_pontos = exibe_mensagem(f"Maior Pontuação: {maior_pontuacao}", 40, preto)
        tela.blit(recorde_pontos, (largura // 2 - recorde_pontos.get_width() // 2, altura // 3))

        recorde_tempo = exibe_mensagem(f"Maior Tempo: {maior_tempo}s", 40, preto)
        tela.blit(recorde_tempo, (largura // 2 - recorde_tempo.get_width() // 2, altura // 2))

        voltar = exibe_mensagem("Pressione 'Esc' para voltar", 30, preto)
        tela.blit(voltar, (largura // 2 - voltar.get_width() // 2, altura - 60))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return


class Dino(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.som_pulo = pygame.mixer.Sound(os.path.join(diretorio_sons, "jump_sound.wav"))
        self.som_pulo.set_volume(1)
        self.imagens_dinossauro = []
        for i in range(3):
            img = sprite_dino.subsurface((i*34,0), (34,48))
            img = pygame.transform.scale(img, (1.5*34, 1.5*48))
            self.imagens_dinossauro.append(img)
        self.index_lista = 0
        self.image = self.imagens_dinossauro[self.index_lista]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.pos_y_inicial = altura-56 - 96//2
        self.rect.center = (100,self.pos_y_inicial) 
        self.pulo = False

    def pular(self):
        self.pulo = True
        self.som_pulo.play()

    def update(self):
        if self.pulo == True:
            if self.rect.y <=200:
                    self.pulo = False
            self.rect.y -= 20
        else:
            if self.rect.y < self.pos_y_inicial:
                self.rect.y += 20
            else:
                self.rect.y = self.pos_y_inicial
        
        if self.index_lista > 2:
            self.index_lista = 0
        self.index_lista += 0.25
        self.image = self.imagens_dinossauro[int(self.index_lista)]


class Nuvens(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((32 * 3, 0), (32, 32))
        self.image = pygame.transform.scale(self.image, (3 * 32, 3 * 32))
        self.rect = self.image.get_rect()
        self.rect.y = randrange(50, 200, 50)
        self.rect.x = largura - randrange(30, 300, 90)

    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = largura
            self.rect.y = randrange(50, 200, 50)
        self.rect.x -= velocidade_jogo

class Chao(pygame.sprite.Sprite):
    def __init__(self, pos_x):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_floor.subsurface((0, 0), (128, 128))
        self.image = pygame.transform.scale(self.image, (1*128, 2*128))
        self.rect = self.image.get_rect()
        self.rect.y = altura - 98
        self.rect.x = pos_x * 55

    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = largura
        self.rect.x -= 10

class Cacto(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((32 * 2, 0), (32, 32))
        self.image = pygame.transform.scale(self.image, (3 * 32, 3 * 32))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.escolha = escolha_obstaculo
        self.rect.center = (largura, altura-78)
        self.rect.x = largura

    def update(self):
        if self.escolha == 0:
            if self.rect.topright[0] < 0:
                self.rect.x = largura
            self.rect.x -= velocidade_jogo


class DinoVoador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagens_dinossauro = []
        for i in range(0,2):
            img = sprite_sheet.subsurface((i*32,0), (32,32))
            img = pygame.transform.scale(img, (3*32, 3*32))
            self.imagens_dinossauro.append(img)

        self.index_lista = 0
        self.image = self.imagens_dinossauro[self.index_lista]
        self.mask = pygame.mask.from_surface(self.image)
        self.escolha = escolha_obstaculo
        self.rect = self.image.get_rect()
        self.rect.center = (largura, 300)
        self.rect.x = largura

    def update(self):
        if self.escolha == 1:
            if self.rect.topright[0] < 0:
                self.rect.x = largura
            self.rect.x -= velocidade_jogo

            if self.index_lista > 1:
                self.index_lista = 0
            self.index_lista += 0.25
            self.image = self.imagens_dinossauro[int(self.index_lista)]

class Moeda(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.imagens_coin = []
        for i in range(15):
            img = sprite_coin.subsurface((0,i*16), (16,16))
            img = pygame.transform.scale(img, (2*16, 2*16))
            self.imagens_coin.append(img)
        self.index_lista = 0
        self.image = self.imagens_coin[self.index_lista]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.reposicionar()

    def reposicionar(self):
    # Faz a moeda aparecer em uma posição aleatória dentro de um intervalo válido
        self.rect.x = randrange(largura, largura + 200)  # Moeda aparece fora da tela inicial
        self.rect.y = randrange(dino.pos_y_inicial - 150, dino.pos_y_inicial - 30) # Limite entre o chão e o alcance do pulo
 
    def update(self):
        if self.rect.topright[0] < 0:  # Saiu da tela
            self.reposicionar()
        self.rect.x -= velocidade_jogo  # Movimento lateral
    
    # Atualizar o índice do frame
        self.index_lista += 0.2  # Ajuste a velocidade da animação
        if self.index_lista >= len(self.imagens_coin):
            self.index_lista = 0
        self.image = self.imagens_coin[int(self.index_lista)]



todas_as_sprites = pygame.sprite.Group()
dino = Dino()
todas_as_sprites.add(dino)

for i in range(4):
    nuvem = Nuvens()
    todas_as_sprites.add(nuvem)

for i in range(largura):
    chao = Chao(i)
    todas_as_sprites.add(chao)

cacto = Cacto ()
todas_as_sprites.add(cacto)

dino_voador = DinoVoador()
todas_as_sprites.add(dino_voador)

moeda = Moeda()
todas_as_sprites.add(moeda)

grupo_obstaculos = pygame.sprite.Group()
grupo_obstaculos.add(cacto)
grupo_obstaculos.add(dino_voador)

grupo_moedas = pygame.sprite.Group()
grupo_moedas.add(moeda)

maior_pontuacao, maior_tempo = carregar_recordes()
relogio = pygame.time.Clock()


# Loop principal
while True:
    opcao = mostrar_menu()

    if opcao == "iniciar":
        # Reiniciar o jogo e começar a partida
        reiniciar_jogo()
        relogio = pygame.time.Clock()

        while True:
            relogio.tick(30)
            tela.blit(background, (0, 0))
            todas_as_sprites.draw(tela)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE and colidiu == False:
                        if dino.rect.y != dino.pos_y_inicial:
                            pass
                        else:
                            dino.pular()
                    if event.key == K_r and colidiu == True:
                        reiniciar_jogo()

            colisoes = pygame.sprite.spritecollide(dino, grupo_obstaculos, False, pygame.sprite.collide_mask)
            pontuacao = pygame.sprite.spritecollide(dino, grupo_moedas, True, pygame.sprite.collide_mask)

            todas_as_sprites.draw(tela)

            if cacto.rect.topright[0] <= 0 or dino_voador.rect.topright[0] <= 0:
                escolha_obstaculo = choice([0, 1])
                cacto.rect.x = largura
                dino_voador.rect.x = largura
                cacto.escolha = escolha_obstaculo
                dino_voador.escolha = escolha_obstaculo

            if colisoes and colidiu == False:
                som_colisao.play()
                colidiu = True

            if colidiu == True:
                if tempo % 100 == 0:
                    tempo += 1
                if tempo > maior_tempo:
                    maior_tempo = tempo
                if pontos > maior_pontuacao:
                    maior_pontuacao = pontos
                salvar_recordes(maior_pontuacao, maior_tempo)
                game_over = exibe_mensagem('GAME OVER', 40, preto)
                tela.blit(game_over, (largura//2, altura//2))
                recorde_pontos = exibe_mensagem(f"Maior Pontuação: {maior_pontuacao}", 25, preto)
                recorde_tempo = exibe_mensagem(f"Maior Tempo: {maior_tempo}s", 25, preto)
                tela.blit(recorde_pontos, (largura // 2 - 200, altura // 2 + 10))
                tela.blit(recorde_tempo, (largura // 2 - 200, altura // 2 + 40))
                restart = exibe_mensagem('Pressione r para reiniciar', 25, preto)
                tela.blit(restart, (largura//2, altura // 2 + 60))
                


            else:
                tempo += 1
                todas_as_sprites.update()
                texto_tempo = exibe_mensagem(tempo, 40, preto)
                texto_pontuacao = exibe_mensagem(f"Pontos: {pontos}", 40, preto)
                tela.blit(texto_pontuacao, (30, 30))
                if pontuacao:  # Se houve colisão com uma moeda
                    pontos += 1  # Incrementa a pontuação
                    som_pontuacao.play()
                    nova_moeda = Moeda()
                    grupo_moedas.add(nova_moeda)
                    todas_as_sprites.add(nova_moeda)
                    
                    
            if tempo % 100 == 0:
                som_tempo.play()
                if velocidade_jogo >= 23:
                    velocidade_jogo += 0
                else:
                    velocidade_jogo += 2

            tela.blit(texto_tempo, (520, 30))
            tela.blit(texto_pontuacao, (30, 30))
            pygame.display.flip()

    elif opcao == "instrucoes":
        mostrar_instrucoes()

    elif opcao == "records":
        mostrar_records()
        
    