import customtkinter
from Jogo.Resultado import Pedra, Papel, Tesoura

def escolha(JanelaInicial):
  def PedraB():
    for widget in JanelaInicial.winfo_children():
      widget.destroy()
    Pedra(JanelaInicial)

  def PapelB():
    for widget in JanelaInicial.winfo_children():
      widget.destroy()
    Papel(JanelaInicial)

  def TesouraB():
    for widget in JanelaInicial.winfo_children():
      widget.destroy()
    Tesoura(JanelaInicial)

  text = customtkinter.CTkLabel(JanelaInicial,
                                text='A IA já escolheu a dela!\nQual sua escolha?',
                                text_color='White',
                                font=('Arial', 20))
  text.pack(pady=25)

  frame_botoes = customtkinter.CTkFrame(JanelaInicial, fg_color="transparent")
  frame_botoes.pack(pady=60)
 
  pedraB = customtkinter.CTkButton(frame_botoes,
                                  text='Pedra',
                                  text_color='White',
                                  corner_radius=17,
                                  width=100,
                                  font=('Arial', 16),
                                  command=lambda: PedraB())
  pedraB.grid(row=0, column=0, padx=10)

  papelB = customtkinter.CTkButton(frame_botoes,
                                  text='Papel',
                                  text_color='White',
                                  corner_radius=17,
                                  width=100,
                                  font=('Arial', 16),
                                  command=lambda: PapelB())
  papelB.grid(row=0, column=1, padx=10)

  tesouraB = customtkinter.CTkButton(frame_botoes,
                                  text='Tesoura',
                                  text_color='White',
                                  corner_radius=17,
                                  width=100,
                                  font=('Arial', 16),
                                  command=lambda: TesouraB())
  tesouraB.grid(row=0, column=2, padx=10)
  
  JanelaInicial.mainloop()