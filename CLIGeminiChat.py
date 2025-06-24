import os
import sys
import google.generativeai as genai
import logging


os.environ["GRPC_ENABLE_FORK_SUPPORT"] = "0"
logging.getLogger("absl").setLevel(logging.ERROR)
sys.stderr = open(os.devnull)
def main():

    api_key = input("Digite sua API Key do Gemini: ").strip()
    
    
    genai.configure(api_key=api_key)
    
    
    try:
        model = genai.GenerativeModel("gemini-pro")
        chat = model.start_chat()
        print("Conexão estabelecida! Digite sua mensagem (ou QUIT para sair).\n")
    except Exception as e:
        print(f"Erro ao conectar ao modelo: {e}")
        return
    
    while True:
        user_input = input("Você: ")
        if user_input.strip().upper() == "QUIT":
            print("Encerrando o chat...")
            break
        
        try:
            response = chat.send_message(user_input)
            print("AI:", response.text)
        except Exception as e:
            print(f"Erro ao processar a resposta: {e}")

    print("\nAvisos: \n")

if __name__ == "__main__":
    main()
