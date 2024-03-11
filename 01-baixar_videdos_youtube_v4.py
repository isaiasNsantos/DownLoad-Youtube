import os
from pytube import YouTube


def exibir_menu():
    print('''
███████╗██████╗░███████╗███████╗░░░░░░██████╗░░█████╗░░██╗░░░░░░░██╗███╗░░██╗
██╔════╝██╔══██╗██╔════╝██╔════╝░░░░░░██╔══██╗██╔══██╗░██║░░██╗░░██║████╗░██║
█████╗░░██████╔╝█████╗░░█████╗░░█████╗██║░░██║██║░░██║░╚██╗████╗██╔╝██╔██╗██║
██╔══╝░░██╔══██╗██╔══╝░░██╔══╝░░╚════╝██║░░██║██║░░██║░░████╔═████║░██║╚████║
██║░░░░░██║░░██║███████╗███████╗░░░░░░██████╔╝╚█████╔╝░░╚██╔╝░╚██╔╝░██║░╚███║
╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚══════╝░░░░░░╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝░░╚══╝

██╗░░░██╗░█████╗░██╗░░░██╗████████╗██╗░░░██╗██████╗░███████╗
╚██╗░██╔╝██╔══██╗██║░░░██║╚══██╔══╝██║░░░██║██╔══██╗██╔════╝
░╚████╔╝░██║░░██║██║░░░██║░░░██║░░░██║░░░██║██████╦╝█████╗░░
░░╚██╔╝░░██║░░██║██║░░░██║░░░██║░░░██║░░░██║██╔══██╗██╔══╝░░
░░░██║░░░╚█████╔╝╚██████╔╝░░░██║░░░╚██████╔╝██████╦╝███████╗
░░░╚═╝░░░░╚════╝░░╚═════╝░░░░╚═╝░░░░╚═════╝░╚═════╝░╚══════╝ ''')

# FUNÇÕES

# LINPAR O TERMINAL 
def limpar_terminal():
    os.system('cls')

# SAIR DO APP
def finalizar_app():
    print('Finalizando app!')

# ELA VERIFICA SE ALGO FOI DIGITADO FORA DO ESPERADO- 
def opcao_invalida():  
    print('opção invalida, tente novamente!\n')
    voltar_ao_menu_principal()
    exibir_menu()
    opcoes()
    limpar_terminal()

# VOLTAR AO MENU
def voltar_ao_menu_principal():
    input('\nDigite \033[33m[Enter]\033[m para voltar ao menu principal.')
    main()  # VOLTANTO AO MENU PRINCIPA

# OPÇÕES 
def opcoes():
    try:
        print('''
Escolha uma das opções abaixo.\n
✔  1. Extensão MP4 -"Video"
✔  2. Extenção MP3 -"Audio"  
✔  3. Finalizar app   
        ''')
        opcoes = int(input('Digite a opção desejada:  '))

        if opcoes == 1:
            video()
        elif opcoes == 2:
            audio()
        elif opcoes == 3:
            finalizar_app()
            # limpar_terminal()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

# FUNÇÃO PARA BAIXAR  VIDEOS
def video():
    url = input(' URL: ')
    youtube = YouTube(url)
    pasta_videos = os.getcwd() + os.sep + "MP4"
    stream = youtube.streams.get_highest_resolution()
    stream.download(output_path=pasta_videos)
    print('|Seu download está pronto na pasta MP4|')

# FUNÇÃO PARA BAIXAR AUDIO
def audio():
    url = YouTube(str(input(" URL: ")))
    video = url.streams.filter(only_audio=True).first()
    pasta_audio = os.getcwd() + os.sep + "MP3"
    out_file = video.download(output_path=pasta_audio)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    print(url.title + " |Seu download está pronto na pasta MP3|")


def main():
    exibir_menu()
    opcoes()


if __name__ == '__main__':
    main()
