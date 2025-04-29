import customtkinter
from Jogo.Centralizar import centralizar_janela

def proximo():
  from Jogo.Escolha import escolha
  
  for widget in JanelaInicial.winfo_children():
    widget.destroy()
  
  escolha(JanelaInicial)

JanelaInicial = customtkinter.CTk()
JanelaInicial.geometry('300x200')
JanelaInicial.title('Pedra Papel Tesoura')

centralizar_janela(JanelaInicial, largura=425, altura= 250)

text = customtkinter.CTkLabel(JanelaInicial,
                              text='Bem vindo ao \n\n'
                              'Pedra X Papel X Tesoura',
                              text_color='White',
                              font=('Arial', 20))
text.pack(pady=25)

start = customtkinter.CTkButton(JanelaInicial,
                                text='Começar',
                                text_color='White',
                                corner_radius= 17,
                                width= 150,
                                font=('Arial', 16),
                                command=proximo)
start.pack(pady=50)

JanelaInicial.mainloop()
