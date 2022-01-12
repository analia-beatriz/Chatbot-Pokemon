# This files contains your custom actions which can be used to run
# custom Python code.

# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
from rasa_sdk.events import SlotSet
from pymongo import MongoClient


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_show_pokemon"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        api_adress='https://pokeapi.co/api/v2/pokemon/'
        pokemon = tracker.get_slot("nome") 
        url = api_adress + pokemon 
        usuario = tracker.get_slot('usuario')

        
        
        json_data = requests.get(url).json()
        data = json_data['types'][0]['type']['name']
        resposta = f"{usuario}, o pokemon {pokemon} é do tipo {data}"
        #Conexão com o MongoDB
        client = MongoClient(f'mongodb+srv://ana:lia2345@cluster0.nbfu5.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
        db = client["pokemonsdatabase"]
        col = db["pok"]
        m = [{"usuario": usuario, "pokemon":json_data}]
        col.insert_many(m)

      

        dispatcher.utter_message(text=resposta)

        return [SlotSet("nome", None)]