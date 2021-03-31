from PySimpleGUI import PySimpleGUI as sg


def validador(cpf_user):
    while True:
        if len(cpf_user) == 11 and cpf_user.isnumeric():
            break
        else:
            return 1
    for i in range(2):
        if i == 0:
            soma1 = 0
            for j, num in enumerate(cpf_user):
                if j < 9:
                    soma1 += (j+1)*int(num)
            resto_soma1 = soma1 % 11
            unidade_resto_soma1 = resto_soma1 % 10
            if unidade_resto_soma1 != int(cpf_user[9]):
                return 2
        if i == 1:
            soma2 = 0
            for k, num in enumerate(cpf_user):
                if k < 10:
                    soma2 += k*int(num)
            resto_soma2 = soma2 % 11
            unidade_resto_soma2 = resto_soma2 % 10
            if unidade_resto_soma2 != int(cpf_user[10]):
                return 2
    return 0


def validador_gui():
    sg.theme('Reddit')
    layout = [
        [sg.Text('CPF'), sg.Input(key='cpf', do_not_clear=False, size=(15, 0))],
        [sg.Button('Validar')]
    ]

    janela = sg.Window(title='Validador de CPF', layout=layout)

    while True:
        eventos, valores = janela.read()
        if eventos == 'Validar':
            cpf_user = valores['cpf']
            if validador(cpf_user) == 1:
                sg.popup_ok('Use somente números e verifique a quantidade de dígitos!', no_titlebar=True)
            elif validador(cpf_user) == 2:
                sg.popup_ok('CPF inválido!', no_titlebar=True)
            elif validador(cpf_user) == 0:
                sg.popup_ok('CPF Válido!', no_titlebar=True)
        if eventos == sg.WINDOW_CLOSED:
            break


def main():
    validador_gui()


main()
