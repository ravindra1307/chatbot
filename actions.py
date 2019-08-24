from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, Restarted

import sqlite3

class action_search_jobs(Action):
    def name(self) -> Text:
        return "action_search_jobs"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        conn = sqlite3.connect('job_data.db')     
        cuisine = tracker.get_slot('skills')
        cuisine = cuisine.replace(' ',',')

        if ',' in cuisine:
               result = [x.strip() for x in cuisine.split(',')]
      
        if 'and' in result:
            result.remove('and')
        
        if len(result)>2:       
                q = conn.execute("SELECT DISTINCT company,job from company_data \
                          WHERE skills like '%{}%' or  skills like '%{}%' or  skills like '%{}%' LIMIT 5\
                          ".format(result[0].lower(),result[1].lower(),result[2].lower()))
        elif len(result)==2:
                q = conn.execute("SELECT DISTINCT company,job from company_data \
                          WHERE skills like '%{}%' or  skills like '%{}%' LIMIT 5 \
                          ".format(result[0].lower(),result[1].lower()))
        else:
            q = conn.execute("SELECT DISTINCT company,job from company_data \
                          WHERE skills like '%{}%' LIMIT 5 \
                          ".format(result[0].lower()))
        r=(q.fetchall())
        dispatcher.utter_message("select the job for which you want to enquire")
        buttons = []
        
        for row in r:
            
            title = ("company {} job {}".format(row[0],row[1]))
            payload = ('company {} job {}'.format(row[0],row[1]))
            buttons.append({ "title": title, "payload": payload })
            
        dispatcher.utter_button_message("",buttons)       

class action_search_job_desc(Action):
    def name(self) -> Text:
        return "action_search_job_desc"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
      conn = sqlite3.connect('job_data.db')     
      company = tracker.get_slot('company')
      job = tracker.get_slot('job')
      q = conn.execute("select job_desc from company_data where company='{}' and job='{}' ".format(company.lower(),job.lower()))
      
      r=(q.fetchall())
      for row in r:
          x=row[0]
    
      dispatcher.utter_message(x)


class action_questions(Action):
    def name(self) -> Text:
        return "action_questions"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
      
      faq = tracker.get_slot('faq')
          #'utter_{}'.format(faq.upper())
      dispatcher.utter_template('utter_{}'.format(faq.upper()),tracker)


class action_search_exp(Action):
    def name(self) -> Text:
        return "action_search_exp"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
      conn = sqlite3.connect('job_data.db')     
      company = tracker.get_slot('company')
      job = tracker.get_slot('job')
      q = conn.execute("select experience from company_data where company='{}' and job='{}' ".format(company.lower(),job.lower()))
      
      r=(q.fetchall())
      for row in r:
          x=row[0]
    
      dispatcher.utter_message(x+' years')
   
class action_search_salary(Action):
    def name(self) -> Text:
        return "action_search_salary"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
      conn = sqlite3.connect('job_data.db')     
      company = tracker.get_slot('company')
      job = tracker.get_slot('job')
      q = conn.execute("select package from company_data where company='{}' and job='{}' ".format(company.lower(),job.lower()))
      
      r=(q.fetchall())
      for row in r:
          x=row[0]
    
      dispatcher.utter_message(x)

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

class action_eligibility_criteria(Action):
    def name(self) -> Text:
        return "action_eligibility_criteria"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
      conn = sqlite3.connect('job_data.db')     
      #cuisine = 'data scientist'
      cuisine = tracker.get_slot('company') or tracker.get_slot('job')
      q = conn.execute("select qualification from company_data where company='{}' OR job='{}' ".format(cuisine.lower(),cuisine.lower()))
      
      r=(q.fetchall())
      for row in r:
          x=row[0]
      
      dispatcher.utter_message("qualifications required are " + x)
       
        
        
        
class action_restarting(Action):
    """ This is for restarting the chat"""

    def name(self):
        return "action_restarting"

    def run(self, dispatcher, tracker, domain):
        
        return [Restarted()]
