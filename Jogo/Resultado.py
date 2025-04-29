import customtkinter
from random import choice

list = ['Pedra', 'Papel', 'Tesoura']
Ran = choice(list)

def Pedra(JanelaInicial):
  match Ran:
    case 'Pedra':
      text = customtkinter.CTkLabel(JanelaInicial,
                                    text='A IA escolheu: {}\n\n\n'
                                    'Empate!'.format(Ran),
                                    text_color='White',
                                    font=('Arial', 20))
      text.pack(pady=50)

      JanelaInicial.mainloop()

    case 'Papel':
      text = customtkinter.CTkLabel(JanelaInicial,
                                    text='A IA escolheu: {}\n\n\n'
                                    'Perdeu! ;-;'.format(Ran),
                                    text_color='White',
                                    font=('Arial', 20))
      text.pack(pady=50)

      JanelaInicial.mainloop()

    case 'Tesoura':
      text = customtkinter.CTkLabel(JanelaInicial,
                                    text='A IA escolheu: {}\n\n\n'
                                    'GANHOU!!!!! ;)'.format(Ran),
                                    text_color='White',
                                    font=('Arial', 20))
      text.pack(pady=50)

      JanelaInicial.mainloop()
    
def Papel(JanelaInicial):
  match Ran:
    case 'Pedra':
      text = customtkinter.CTkLabel(JanelaInicial,
                                    text='A IA escolheu: {}\n\n\n'
                                    'GANHOU!!!!! ;)'.format(Ran),
                                    text_color='White',
                                    font=('Arial', 20))
      text.pack(pady=50)

      JanelaInicial.mainloop()

    case 'Papel':
      text = customtkinter.CTkLabel(JanelaInicial,
                                    text='A IA escolheu: {}\n\n\n'
                                    'Empate!'.format(Ran),
                                    text_color='White',
                                    font=('Arial', 20))
      text.pack(pady=50)

      JanelaInicial.mainloop()

    case 'Tesoura':
      text = customtkinter.CTkLabel(JanelaInicial,
                                    text='A IA escolheu: {}\n\n\n'
                                    'Perdeu! ;-;'.format(Ran),
                                    text_color='White',
                                    font=('Arial', 20))
      text.pack(pady=50)

      JanelaInicial.mainloop()

def Tesoura(JanelaInicial): 
  match Ran:
    case 'Pedra':
      text = customtkinter.CTkLabel(JanelaInicial,
                                    text='A IA escolheu: {}\n\n\n'
                                    'Perdeu! ;-;'.format(Ran),
                                    text_color='White',
                                    font=('Arial', 20))
      text.pack(pady=50)

      JanelaInicial.mainloop()

    case 'Papel':
      text = customtkinter.CTkLabel(JanelaInicial,
                                    text='A IA escolheu: {}\n\n\n'
                                    'GANHOU!!!!! ;)'.format(Ran),
                                    text_color='White',
                                    font=('Arial', 20))
      text.pack(pady=50)

      JanelaInicial.mainloop()

    case 'Tesoura':
      text = customtkinter.CTkLabel(JanelaInicial,
                                    text='A IA escolheu: {}\n\n\n'
                                    'Empate!'.format(Ran),
                                    text_color='White',
                                    font=('Arial', 20))
      text.pack(pady=50)

      JanelaInicial.mainloop()


