def responder(pergunta):
    pergunta = pergunta.lower()

    if "olá" in pergunta or "oi" in pergunta:
        return "Olá, como posso ajudar você?"
    elif "tudo bem?" in pergunta:
        return "Tudo ótimo e você?"
    elif "como está o clima hoje?" in pergunta:
        return "O clima parece agradável hoje :)"
    elif "você prefere frio ou calor?" in pergunta:
        return "O inverno parece mais agradável"
    else:
        return "Desculpe, não entendi, pode repetir?"

def iniciar_chatbot():
    print("Chatbot: Olá! Digite 'sair' para encerrar.")
    while True:
        usuario = input("Você: ")
        if usuario.lower() == "sair":
            print("Chatbot: Até a próxima!")
            break
        resposta = responder(usuario)
        print("Chatbot:", resposta)

if __name__ == "__main__":
    iniciar_chatbot()
