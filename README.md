# Chat com Gemini AI

Um aplicativo de chat simples em Python que permite conversar com o modelo Gemini Pro da Google AI através da linha de comando.

## 🤖 Características

- **Interface de linha de comando** simples e intuitiva
- **Conversação contínua** com histórico mantido durante a sessão
- **Tratamento de erros** robusto para conexões e respostas
- **Logs limpos** com supressão de mensagens desnecessárias
- **Saída fácil** com comando QUIT

## 📋 Pré-requisitos

### Python
- **Python 3.7+** instalado no sistema

### API Key do Google AI
- Conta no [Google AI Studio](https://makersuite.google.com/)
- API Key válida para o Gemini Pro

## 📦 Instalação

### 1. Clone ou baixe o arquivo Python

### 2. Instale as dependências
```bash
pip install google-generativeai
```

### 3. Obtenha sua API Key
1. Acesse [Google AI Studio](https://makersuite.google.com/)
2. Faça login com sua conta Google
3. Vá para "Get API Key"
4. Crie uma nova API Key
5. Copie a chave gerada

## 🚀 Como Usar

### Executar o aplicativo
```bash
python chat_gemini.py
```

### Fluxo de uso
1. **Digite sua API Key** quando solicitado
2. **Aguarde a confirmação** de conexão
3. **Digite suas mensagens** e pressione Enter
4. **Receba as respostas** da AI
5. **Digite QUIT** para encerrar

### Exemplo de uso
```
Digite sua API Key do Gemini: [sua-api-key-aqui]
Conexão estabelecida! Digite sua mensagem (ou QUIT para sair).

Você: Olá, como você está?
AI: Olá! Estou funcionando bem, obrigado por perguntar. Como posso ajudá-lo hoje?

Você: Me conte uma piada
AI: Por que os programadores preferem o modo escuro? Porque a luz atrai bugs! 😄

Você: QUIT
Encerrando o chat...
```

## ⚙️ Funcionalidades Técnicas

### Configuração da API
```python
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat()
```

### Supressão de Logs
- **GRPC fork support** desabilitado para evitar warnings
- **Logs ABSL** configurados para mostrar apenas erros
- **stderr** redirecionado para evitar mensagens desnecessárias

### Tratamento de Erros
- **Validação de conexão** com o modelo
- **Captura de exceções** em tempo de execução
- **Mensagens de erro** informativas para o usuário

## 🔧 Configurações Avançadas

### Modificar o Modelo
Para usar outros modelos do Gemini, altere a linha:
```python
model = genai.GenerativeModel("gemini-pro")
```

Modelos disponíveis:
- `gemini-pro` - Modelo padrão de texto
- `gemini-pro-vision` - Para análise de imagens

### Personalizar Parâmetros
```python
generation_config = {
    "temperature": 0.7,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}
model = genai.GenerativeModel("gemini-pro", generation_config=generation_config)
```

## 🛡️ Segurança

### Proteção da API Key
- **Nunca compartilhe** sua API Key
- **Não faça commit** da chave no controle de versão
- **Use variáveis de ambiente** para produção:

```python
api_key = os.getenv('GEMINI_API_KEY')
```

### Exemplo com variável de ambiente
```bash
export GEMINI_API_KEY="sua-api-key-aqui"
python chat_gemini.py
```

## 📊 Estrutura do Código

```
chat_gemini.py
├── Importações e configurações
├── Função main()
│   ├── Entrada da API Key
│   ├── Configuração do modelo
│   ├── Loop de conversação
│   └── Tratamento de erros
└── Execução principal
```

## 🚨 Solução de Problemas

### Erro de API Key inválida
```
Erro ao conectar ao modelo: Invalid API key
```
**Solução**: Verifique se a API Key está correta e ativa

### Erro de conexão
```
Erro ao conectar ao modelo: Connection failed
```
**Solução**: Verifique sua conexão com a internet

### Erro de quota excedida
```
Erro ao processar a resposta: Quota exceeded
```
**Solução**: Aguarde o reset da quota ou upgrade sua conta

### Problemas com caracteres especiais
**Solução**: Certifique-se de que o terminal suporta UTF-8

## 📈 Limitações

- **Quota de API**: Limitada pelo plano da conta Google AI
- **Histórico**: Perdido ao reiniciar o aplicativo
- **Modelos**: Apenas modelos de texto (Gemini Pro)
- **Interface**: Apenas linha de comando

## 🔮 Possíveis Melhorias

- **Salvar histórico** de conversas em arquivo
- **Interface gráfica** com tkinter ou PyQt
- **Suporte a imagens** com gemini-pro-vision
- **Configurações** via arquivo de configuração
- **Múltiplas sessões** de chat simultâneas

## 📄 Dependências

```
google-generativeai>=0.3.0
```

## 📝 Licença

Este projeto é de código aberto e pode ser usado, modificado e distribuído livremente.

## 🤝 Contribuições

Contribuições são bem-vindas! Você pode:
- Reportar bugs
- Sugerir novas funcionalidades
- Melhorar a documentação
- Otimizar o código
- Adicionar testes unitários

## 📞 Suporte

Para problemas relacionados à API do Gemini, consulte:
- [Documentação oficial do Google AI](https://ai.google.dev/)
- [Google AI Studio](https://makersuite.google.com/)
- [Guias de início rápido](https://ai.google.dev/tutorials)
