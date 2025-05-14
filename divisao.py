import tkinter as tkinter
from tkinter import scrolledtext

def responder_usuario():
    pergunta = entrada_usuario.get().lower()
    exibir_mensagem(f"você: {pergunta}")

if "olá" in pergunta or "oi" in pergunta:
        resposta "Olá, como posso ajudar você?"
    elif "tudo bem?" in pergunta:
        resposta "Tudo ótimo e você?"
    elif "como está o clima hoje?" in pergunta:
        resposta "O clima parece agradável hoje :)"
    elif "você prefere frio ou calor?" in pergunta:
        resposta "O inverno parece mais agradável"
    else:
        resposta "Desculpe, não entendi, pode repetir?"

exibir_mensagem(f"Bot:{resposta}")
entrada_usuario.delete(0, tk.END)

def exibir_mensagem(mensagem):
    area_chat.configure(state="normal")
    area_chat.insert(tk.END, mensagem + '\n')
    area_chat.configure(state='disabled')
    area_chat.see(tk.END)

janela = tk.Tk()
janela.title("Chatbot com Tkinter")
janela.geometry("400x500")

area_chat = scrolledtext.ScrolledText(janela, wrap=tk.WORD, state='disabled', font=("Arial, 12"))
area_chat.pack(padx=10, pady=10, fill=tk.x)

botao_enviar = tk.Button(janela, text="Enviar", command=responder_usuario)
botao_enviar.pack(pady=5)

janela.blind('<Return>',lambda event: responder_usuario())

exibir_mensagem("Bot: Olá! Digite algo para começar")
janela.mainloop()