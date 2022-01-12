# 🟢 CHATBOT - POKEMON 🟢
<img src="Imagem/logo.png" width=150 height=200 align="right">

---
### CHATBOT
O chatbot construído tem como objetivo criar uma conversa com o usuário a qual ele irá armazenar o nome do usuario e realizar uma busca por um determinado tipo de pokemon que desejar.
 --- 

# Desenvolvimento
## Dependências
   * Python 3.8
   * Rasa e seus componentes
   * Pymongo

## Conexão com o BD
A conexão feita com o DB é com o MongoDB pelo pymongo, ele irá  armazena o nome do usuário o qual está conversando com o bot e os dados do tipo do pokemon que for pesquisado.

## Conexão com a API
A API utilizada nesse projeto foi a https://pokeapi.co, a qual, a partir do nome do pokemon busca o seu tipo como por exemplo o pokemon pikachu que é do tipo elétrico. Um dos problemas encontrado na conexão com a API foi a questão que quando o bot recebe um determinado nome diferente de pokemon, ele acaba enviando o ultimo pokemon pedido.
---
## Como utilizar?
Para utilizar a aplicação e conversar com o bot, além de possuir as depêndencias, basta abrir um terminal e executar o comando "run rasa actions", e em outro terminal executar o comando "rasa shell" e então é só conversar com o bot que ele trará as informações necessárias. Para encerrar a conversa, envie a mensagem "/stop" e ele encerrará o funcionamento.


# Utilizando o ChatBot 
Para utilizar a aplicação com o bot, basta abrir um terminal e executar o comando "run rasa actions", e em outro terminal executar o comando "rasa shell" e então é só iniciar uma conversa com o bot.
   * Dê os cumprimentos ao chatbot
   * Diga sua intenção ao chatbot
   * Digite o seu primeiro nome 
   * Informe o nome do pokemon que deseja saber o tipo 
--- 

## Desenvolvido por 
 👩‍💻 Anália Beatriz


---