import requests
from requests import Response
from tkinter import *

def cotacoes():
    coleta = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    coleta_dic = coleta.json()

    cotacao_dolar = coleta_dic['USDBRL']['bid']
    cotacao_euro = coleta_dic['EURBRL']['bid']
    cotacao_btc = coleta_dic['BTCBRL']['bid']

    texto_resposta['text'] = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

janela = Tk()
janela.title("Cotação Atual de Moedas")
texto = Label(janela, text="Clique aqui para ver as cotações de moedas")
texto.grid(column=0, row=0, padx=10, pady=10)

botao = Button(janela, text="Buscar cotações", command=cotacoes)
botao.grid(column=0, row=1, padx=10, pady=10)

texto_resposta = Label(janela, text="")
texto_resposta.grid(column=0, row=2, padx=10, pady=10)


janela.mainloop()