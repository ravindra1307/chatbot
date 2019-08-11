# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message("Hello World!")
#
#         return []
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet



import sqlite3


class action_search_address(Action):
    def name(self) -> Text:
        return "action_search_address"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
      conn = sqlite3.connect('job_data.db')     
      cuisine = tracker.get_slot('company')
      q = conn.execute("select location from company_data where company='{}' ".format(cuisine.lower()))
      

      r=(q.fetchall())
      for row in r:
          x=row[0]
      dispatcher.utter_message("address of {} is ".format(cuisine.lower()) + x)
  
class action_skills(Action):
    def name(self) -> Text:
        return "action_skills"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
      conn = sqlite3.connect('job_data.db')     
      #cuisine = 'data scientist'
      cuisine = tracker.get_slot('company') or tracker.get_slot('job')
      q = conn.execute("select skills from company_data where company='{}' OR job='{}' ".format(cuisine.lower(),cuisine.lower()))
      

      r=(q.fetchall())
      for row in r:
          x=row[0]
      
      dispatcher.utter_message("skills required are " + x)

'''
conn = sqlite3.connect('job_data.db')     
#cuisine = tracker.get_slot('company') or tracker.get_slot('job')
cuisine = 'data scientist'
q = conn.execute("select skills from company_data where company='{}' OR job='{}' ".format(cuisine.lower(),cuisine.lower()))
      

r=(q.fetchall())
for row in r:
   x=row[0]
print(x)
#dispatcher.utter_message("skills required are " + x)
'''