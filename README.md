# rasa-pizza-chatbot
Código-fonte do agente conversacional baseado no framework RASA para atender clientes de uma pizzaria. O contexto real foi simplificado para fins didáticos.

O modelo foi construído em português, e necessita, além da instalação do RASA, também o spaCy e seu modelo em português.

```
pip install spacy
```
```
python –m spacy download pt_core_news_md
```

Para executar o chatbot você deve (i) subir o servidor de actions do RASA e (ii) iniciar o chatbot (rodar ambos comandos partir do diretório do projeto).

```
rasa run actions
```
```
rasa shell
```


