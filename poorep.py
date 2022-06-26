def calcula_imc(peso, altura):
    situacao = ''
    converter_altura = altura / 100
    imc = peso / (converter_altura ** 2)
    if imc < 17:
        situacao = 'Muito abaixo peso'
        return situacao
    elif 17 <= imc <= 18.49:
        situacao = 'Abaixo peso'
        return situacao
    elif 18.50 <= imc <= 24.99:
        situacao = 'Peso normal'
        return situacao
    elif 25 <= imc <= 29.99:
        situacao = 'Acima peso'
        return situacao
    elif 30 <= imc <= 34.99:
        situacao = 'Obesidade 1'
        return situacao
    elif 35 <= imc <= 39.99:
        situacao = 'Obesidade 2'
        return situacao
    else:
        situacao = 'Obesidade 3'
        return situacao

    class Tela:
        def __init__(self):
            layout = [
                [Text('Peso em KG', size=(5, 2)), Input(size=(5, 0), key='peso')],
                [Text('Altura em CM', size=(5, 2)), Input(size=(5, 0), key='altura')],
                [Text('Resultado do IMC:')],
                [Output(size=(20, 5))],
                [Button('Verificar IMC', size=(20, 0), key='botao')]
            ]
            self.janela = Window('IMC', size=(200, 200), layout=layout, element_justification='c')
            self.button, self.values = self.janela.Read()

        def iniciar(self):
            while True:
                # Informações na tela mantidas em loop até que seja fechada a janela.
                event, self.values = self.janela.Read()
                if event in ('botao', Button):
                    self.retorno()
                elif event in (None, WIN_CLOSED):
                    break

        def retorno(self):
            # esse método tem como objetivo mostrar o resultado na tela.
            peso = self.values['peso']
            altura = self.values['altura']
            print(f'Peso: {peso}')
            print(f'Altura: {altura}')
            cal_peso = float(peso)
            cal_altura = float(altura)
            resultado = calcula_imc(cal_peso, cal_altura)
            print(f'Situação: {resultado}')