from tkinter import *


janela = Tk()
janela.geometry("600x350") 
janela.minsize(600, 350) 
janela.maxsize(600, 350)
janela.title('CALCULADORA')


#MOSTRA O SESULTUDO
resultado = Label(text='',width=51,height=4,font='Times 15 bold',fg='#0D0000', bg='#FFF')
resultado.grid(row=0,column=0,columnspan=4)

#BOTAO DE MULTIPLICAR
def apertMult():
    resultado['text'] += '*'
multi = Button(text='*',width=20,height=2,fg='#FFF',bg='#0D0000',font='Times 12 bold', command=apertMult )
multi.grid(row=1,column=3)

#BOTAO 7
def apert7():
    resultado['text'] += '7'
bot7 = Button(text='7',width=13,height=2,fg='#0D0000',bg='#87CEFA',font='Times 12 bold',command=apert7)
bot7.grid(row=1, column= 0)

#BOTAO 8
def apert8():
    resultado['text'] += '8'
bot8 = Button(text='8',width=13,height=2,fg='#0D0000',bg='#87CEFA',font='Times 12 bold',command=apert8)
bot8.grid(row=1, column= 1)

#BOTAO 9
def apert9():
    resultado['text'] += '9'
bot9 = Button(text='9',width=13,height=2,fg='#0D0000',bg='#87CEFA',font='Times 12 bold',command=apert9)
bot9.grid(row=1, column= 2)

#FUNCAO E BOTAO PARA DIVISÃO
def apertdiv():
    resultado['text'] += '/'
dividi = Button(text='/',width=20,height=2,fg='#FFF',bg='#0D0000',font='Times 12 bold',command=apertdiv)
dividi.grid(row=2,column=3)

#BOTAO 4
def apert4():
    resultado['text'] += '4'
bot4 = Button(text='4',width=13,height=2,fg='#0D0000',bg='#87CEFA',font='Times 12 bold', command=apert4)
bot4.grid(row=2, column= 0)

#BOTAO 5
def apert5():
    resultado['text'] += '5'
bot5 = Button(text='5',width=13,height=2,fg='#0D0000',bg='#87CEFA',font='Times 12 bold',command=apert5)
bot5.grid(row=2, column= 1)


#BOTAO 6
def apert6():
    resultado['text'] += '6'
bot6 = Button(text='6',width=13,height=2,fg='#0D0000',bg='#87CEFA',font='Times 12 bold', command=apert6)
bot6.grid(row=2, column= 2)


#FUNCAO E BOTAO PARA DIMINUIR 
def apertmenos ():
    resultado['text'] += '-'
diminui = Button(text='-',width=20,height=2,fg='#FFF',bg='#0D0000',font='Times 12 bold',command=apertmenos)
diminui.grid(row=3,column=3)

#BOTAO 1
def apert1 ():
    resultado['text'] += '1'
bot1 = Button(text='1',width=13,height=2,fg='#0D0000',bg='#87CEFA',font='Times 12 bold',command=apert1)
bot1.grid(row=3, column= 0)

#BOTAO 2
def apert2 ():
    resultado['text'] += '2'
bot2 = Button(text='2',width=13,height=2,fg='#0D0000',bg='#87CEFA',font='Times 12 bold',command=apert2)
bot2.grid(row=3, column= 1)

#BOTAO 3
def apert3 ():
    resultado['text'] +='3'
bot3 = Button(text='3',width=13,height=2,fg='#0D0000',bg='#87CEFA',font='Times 12 bold',command=apert3)
bot3.grid(row=3, column= 2)


#FUNCAO E BOTAO DE SOMAR
def apertesoma():
    resultado['text'] += '+'
soma = Button(text='+',width=20,height=2,fg='#FFF',bg='#0D0000',font='Times 12 bold',command=apertesoma)
soma.grid(row=4,column=3)


#BOTAO DE IGUALDADE
def aperteigual ():
    resultado['text'] = str(eval(resultado['text']))
igual = Button(text='=',width=13,height=2,fg='#0D0000',bg='#FFCBDB',font='Times 12 bold',command=aperteigual)
igual.grid(row=4,column=2)


#BOTAO 0
def aperta0():
    resultado['text'] += '0'
bot0 = Button(text='0',width=13,height=2,fg='#0D0000',bg='#87CEFA',font='Times 12 bold', command=aperta0)
bot0.grid(row=4, column= 1)

#BOTAO DE LIMPAR TELA
def apertouc ():
    resultado['text'] = ''
botC = Button(text='C',width=13,height=2,fg='#0D0000',bg='#C0C0C0',font='Times 12 bold',command=apertouc)
botC.grid(row=4, column= 0)

janela.mainloop()

