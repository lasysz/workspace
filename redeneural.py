import openai

openai.api.key = "SUA_CHAVE_API_KEY"

def perguntar_gpt(pergunta):
    resposta = openai.ChatCompletion.create(
        model="gpt-3-5-turbo",
        messages=[
            {"role": "system", "content": "Você é um assistente simpatico"},
            {"role": "user", "content": pergunta}
        ]
    )
    return resposta.choices[0].message['content']

def iniciar_chat():
    print("GPT Chatbot: Digite 'sair' para encerrar")
    while True:
        user_input = input("Você: ")
        if user_input.lower() == "sair":
            print("Chatbot: Até Logo!")
            break 
        resposta = perguntar_gpt(user_input)
        print("Chatbot" , resposta)

if __name__ == "__main__":
    iniciar_chat()