# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
 
from datetime import datetime


# Ação customizada para escrever o pedido em um arquivo texto
# Aqui poderíamos inserir em um banco de dados, mandar imprimir, etc.
# Sempre que for utilizar ações cutomizadas você deve:
# 1) Definir o endereço do servidor de ações no arquivo endpoints.yml
# 2) antes de iniciar o chatbot deve-se iniciar um servidor de ações com o comando: rasa run actions
class ActionEscrevePedido(Action):

	def name(self) -> Text:
		return "action_escreve_pedido"

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		print("Escrevendo arquivo de pedido...")

		# Escreve arquivo com timestamp atual e pedido
		pedidoFile = "pedidos/" + datetime.now().strftime("%d-%b-%Y-%H-%M-%S") + ".txt"
		print("Pedido escrito no arquivo: " + pedidoFile)
		f = open(pedidoFile, "w")
		f.write("Pedido: Pizza " + tracker.get_slot('tamanho') )
		f.close()

		# Envio uma das responses definidas no domain
		dispatcher.utter_message(response = "utter_finaliza_pedido")
		# Poderia enviar uma mensagem fixa
		#dispatcher.utter_message(text="Hello World!")

		return []
