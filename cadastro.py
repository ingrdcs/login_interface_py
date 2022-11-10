# importando a biblioteca
from PySimpleGUI import PySimpleGUI as sg


# Layout 
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'), sg.Input(key='Usuário', size=(20,1))],
    [sg.Text('Senha'), sg.Input(key='Senha', password_char='*', size=(20,1))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]

# Janela

janela = sg.Window('Login', layout)

# Ler os eventos

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['Usuário'] == 'admin' and valores['Senha'] == 'admin':
            print('Bem vindo ao sistema')