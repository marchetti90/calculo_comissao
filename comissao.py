from tkinter import *

janela = Tk()
janela.title("Suseranus Comissão")
janela.geometry("300x200+200+200")
lb_valor_comissao = Label(janela, text="Insira o valor vendido",font=('Arial', 15))
lb_valor_comissao.pack(anchor=CENTER)

def _calcular_comissao():
    par_30k = 30000
    par_50k = 59999
    par_60k = 60000
    valor_digitado_f = float(ed_valor.get())
    if valor_digitado_f <= par_30k:
        valor_calculado = (valor_digitado_f * 0.5) / 100
        lb_valor_comissao["text"] = f'R$ {valor_calculado:.2f}'
    elif valor_digitado_f <= par_50k:
        valor_calculado = (((valor_digitado_f - float(par_30k)) * 1) / 100) + 150
        lb_valor_comissao["text"] = f'R$ {valor_calculado:.2f}'
    elif valor_digitado_f >= par_60k:
        valor_calculado = (((valor_digitado_f - float(par_60k)) * 2) / 100) + 500
        lb_valor_comissao["text"] = f'R$ {valor_calculado:.2f}'

ed_valor = Entry(janela)
ed_valor.place(x=40,y=80)
ed_valor.pack(side=TOP, fill=BOTH)
btn_gerar_comissao = Button(janela, text='Calcular', font=('Arial', 15), command=_calcular_comissao)
btn_gerar_comissao.pack(side=TOP)
lb_valor_comissao = Label(janela, text="",font=('Arial', 20))
lb_valor_comissao.pack(side=TOP, fill=BOTH, expand=True)

copyright_var = Label(janela, text="developed by Marchetti",font=('Arial', 7))
copyright_var.pack(side=RIGHT)

janela.iconbitmap('C:\Suseranus\ico.ico')

janela = janela.mainloop()
