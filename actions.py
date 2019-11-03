from typing import Any, Text, Dict, List, Union, Optional
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, Restarted, FollowupAction
from rasa_sdk.forms import FormAction
import sqlite3

offset_value = 0



class JobForm(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "job_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["skills", "experience", "location"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""
            
        #"loan_amount": self.from_text(intent=None),
    

        return {
            "skills": [
                self.from_text(intent=["my_skills","skills_job",None]),
                #self.from_entity(
                #    entity="skills",intent=["my_skills","skills_job",None]),
            ],
            "experience": [
                self.from_entity(
                    entity="experience", intent=["experience"]
                ),
            ],
            "location": [
                self.from_text(intent=["location",None]),
                #self.from_entity(entity="location", intent=["location",None]),
            ],
        }

    
    # USED FOR DOCS: do not rename without updating in docs
    def validate_skills(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Optional[Text]:
        """Validate cuisine value."""

        
        return {"skills": value}
      

    def validate_experience(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Optional[Text]:
        """Validate num_people value."""

        
        return {"experience": value}
        

    def validate_location(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Any:
        """Validate outdoor_seating value."""

        
        return {"location": value}
        
   
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        #dispatcher.utter_template("utter_application", tracker)
        return []



class action_search_jobs(Action):
    def name(self) -> Text:
        return "action_search_jobs"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
    
    
        #dispatcher.utter_template("utter_application", tracker)
        global offset_value
            
        offset_value = 0
        conn = sqlite3.connect('job_data.db')     
        result = tracker.get_slot('skills')
        experience_req = tracker.get_slot('experience')
        location_pref = tracker.get_slot('location')
        
        if experience_req == '0':
            experience_format = 0
        elif experience_req == '0-2':
            experience_format = 2
        elif experience_req == '2-4':
            experience_format = 4
        else:
            experience_format = 25
        
        
        
        
        
        if result == None:
            result=[]
            ext_entity = (tracker.latest_message)['text']
            skills_list = ["javaScript","sql","java","ruby","php","python","c","c++","c#","html","css"]
            split_space = ext_entity.split()
            split_comma = ext_entity.split(',')
            split_all = split_comma+split_space
            for i in skills_list:
                if i in split_all:
                    result.append(i)
                    
                    
            
            if len(result)>2:       
                q = conn.execute("SELECT DISTINCT company,position from joblistings \
                          WHERE skills_req like '%{}%' or  skills_req like '%{}%' or  skills_req like '%{}%' LIMIT 5\
                          ".format(result[0].lower(),result[1].lower(),result[2].lower()))
            elif len(result)==2:
                #dispatcher.utter_message("s")
                q = conn.execute("SELECT DISTINCT company,position from joblistings \
                          WHERE skills_req like '%{}%' or  skills_req like '%{}%' LIMIT 5 \
                          ".format(result[0].lower(),result[1].lower()))
            else:
                q = conn.execute("SELECT DISTINCT company,position from joblistings \
                          WHERE skills_req like '%{}%' LIMIT 5 \
                          ".format(result[0].lower()))


            r=(q.fetchall())
            dispatcher.utter_message("select the position for which you want to enquire")
            buttons = []
        
            for row in r:
            
                title = ("company {} position {}".format(row[0],row[1]))
                payload = ('company {} position {}'.format(row[0],row[1]))
                buttons.append({ "title": title, "payload": payload })
            
            if len(r) > 4:
                buttons.append({ "title": "Show more" ,"payload":"Show more"})    
            
            s = ","
            s = s.join(result) 
            #print(s) 
            #return(SlotSet('skills',s))
            
            dispatcher.utter_button_message("{}".format(s),buttons) 
            return [SlotSet('skills',s)]

            



        
        else:
            result = result.replace(' ',',')
            
            if ',' in result:
                   result = [x.strip() for x in result.split(',')]
          
            if 'and' in result:
                result.remove('and')
        
            if location_pref == 'no':
                if len(result)>2:       
                        q = conn.execute("SELECT DISTINCT company,position from joblistings \
                                  WHERE (skills_req like '%{}%' or  skills_req like '%{}%' or  skills_req like '%{}%')\
                                  and exp_req <= '{}' LIMIT 5\
                                  ".format(result[0].lower(),result[1].lower(),result[2].lower(),experience_format))
                elif len(result)==2:
                        dispatcher.utter_message("select the position for which you want to enquire")
                        q = conn.execute("SELECT DISTINCT company,position from joblistings \
                                  WHERE (skills_req like '%{}%' or  skills_req like '%{}%')\
                                  and exp_req <= '{}' LIMIT 5 \
                                  ".format(result[0].lower(),result[1].lower(),experience_format))
                else:
                    q = conn.execute("SELECT DISTINCT company,position from joblistings \
                                  WHERE skills_req like '%{}%' and exp_req <= '{}' LIMIT 5 \
                                  ".format(result[0].lower(),experience_format))
                
            else: 
        
                if len(result)>2:       
                        q = conn.execute("SELECT DISTINCT company,position from joblistings \
                                  WHERE (skills_req like '%{}%' or  skills_req like '%{}%' or  skills_req like '%{}%')\
                                  and exp_req <= '{}' and job_location = '{}' LIMIT 5\
                                  ".format(result[0].lower(),result[1].lower(),result[2].lower(),experience_format,location_pref.lower()))
                elif len(result)==2:
                        dispatcher.utter_message("select the position for which you want to enquire")
                        q = conn.execute("SELECT DISTINCT company,position from joblistings \
                                  WHERE (skills_req like '%{}%' or  skills_req like '%{}%')\
                                  and exp_req <= '{}' and job_location = '{}' LIMIT 5 \
                                  ".format(result[0].lower(),result[1].lower(),experience_format,location_pref.lower()))
                else:
                    q = conn.execute("SELECT DISTINCT company,position from joblistings \
                                  WHERE skills_req like '%{}%' and exp_req <= '{}' and job_location = '{}' LIMIT 5 \
                                  ".format(result[0].lower(),experience_format,location_pref.lower()))


            r=(q.fetchall())
            dispatcher.utter_message("select the position for which you want to enquire")
            buttons = []
            
            for row in r:
                
                title = ("company {} position {}".format(row[0],row[1]))
                payload = ('company {} position {}'.format(row[0],row[1]))
                buttons.append({ "title": title, "payload": payload })
                
            if len(r) > 4:
                buttons.append({ "title": "Show more" ,"payload":"Show more"})    
            
            dispatcher.utter_button_message("",buttons)  
        
        
            
       
        
        
        
        
        #dispatcher.utter_button_message("",more)
        

class action_search_jobs_more(Action):
    def name(self) -> Text:
        return "action_search_jobs_more"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        conn = sqlite3.connect('job_data.db')     
        result = tracker.get_slot('skills')
        experience_req = tracker.get_slot('experience')
        location_pref = tracker.get_slot('location')
        
        if experience_req == '0':
            experience_format = 0
        elif experience_req == '0-2':
            experience_format = 2
        elif experience_req == '2-4':
            experience_format = 4
        else:
            experience_format = 25
        
        result = result.replace(' ',',')
        
        if ',' in result:
               result = [x.strip() for x in result.split(',')]
        
      
        if 'and' in result:
            result.remove('and')
            
        global offset_value
            
        offset_value += 5
        
        if len(result)>2:       
                    q = conn.execute("SELECT DISTINCT company,position from joblistings \
                              WHERE (skills_req like '%{}%' or  skills_req like '%{}%' or  skills_req like '%{}%')\
                              and exp_req <= '{}' and job_location = '{}' LIMIT 5  OFFSET {}\
                              ".format(result[0].lower(),result[1].lower(),result[2].lower(),experience_format,location_pref.lower(),offset_value))
        elif len(result)==2:
                    #dispatcher.utter_message("select the position for which you want to enquire")
                    q = conn.execute("SELECT DISTINCT company,position from joblistings \
                              WHERE (skills_req like '%{}%' or  skills_req like '%{}%')\
                              and exp_req <= '{}' and job_location = '{}' LIMIT 5  OFFSET {}\
                              ".format(result[0].lower(),result[1].lower(),experience_format,location_pref.lower(),offset_value))
        else:
                q = conn.execute("SELECT DISTINCT company,position from joblistings \
                              WHERE skills_req like '%{}%' and exp_req <= '{}' and job_location = '{}' LIMIT 5  OFFSET {}\
                              ".format(result[0].lower(),experience_format,location_pref.lower(),offset_value))
            
       
        '''
        if len(result)>2:       
                q = conn.execute("SELECT DISTINCT company,position from joblistings \
                          WHERE skills_req like '%{}%' or  skills_req like '%{}%' or  skills_req like '%{}%' LIMIT 5 OFFSET {}\
                          ".format(result[0].lower(),result[1].lower(),result[2].lower(),offset_value))
        elif len(result)==2:
                q = conn.execute("SELECT DISTINCT company,position from joblistings \
                          WHERE skills_req like '%{}%' or  skills_req like '%{}%' LIMIT 5 OFFSET {}\
                          ".format(result[0].lower(),result[1].lower(),offset_value))
        else:
            q = conn.execute("SELECT DISTINCT company,position from joblistings \
                          WHERE skills_req like '%{}%' LIMIT 5 OFFSET {}\
                          ".format(result[0].lower(),offset_value))
        '''

        r=(q.fetchall())
        dispatcher.utter_message("select the position for which you want to enquire")
        buttons = []
        
        for row in r:
            
            title = ("company {} position {}".format(row[0],row[1]))
            payload = ('company {} position {}'.format(row[0],row[1]))
            buttons.append({ "title": title, "payload": payload })
            
        buttons.append({ "title": "Show previous jobs" ,"payload":"Show previous jobs"})    
        dispatcher.utter_button_message("",buttons) 
        

class action_search_job_desc(Action):
    def name(self) -> Text:
        return "action_search_job_desc"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
      conn = sqlite3.connect('job_data.db')     
      company = tracker.get_slot('company')
      job = tracker.get_slot('job')
      q = conn.execute("select job_description from joblistings where company='{}' and position='{}' ".format(company.lower(),job.lower()))
      
      r=(q.fetchall())
      for row in r:
          x=row[0]
    
      dispatcher.utter_message(x)
      dispatcher.utter_template('utter_ask_job_queries',tracker)
      #return [FollowupAction("action_search_jobs")]

class action_greet(Action):
    def name(self) -> Text:
        return "action_greet"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
      
      message = (tracker.latest_message)['text']
      sent = [i for i in message.split(' ')]
      
      words = ["wtf",
         "WTF",
         "what the fuck",
         "what the f**k",
         "f*uck",
         "f*uck you",
         "fucker",
         "You suck",
         "I hate you",
         "idiot",
         "stfu",
         "shut the f*** up",
         "f*uk",
         "f**k",
         "fuck",
         "wtf?",
         "wtf bot",
         ]
      
      flag = 0
      for j in sent:    
        if j in words:
            flag = 1    
      if flag==1:
        
        dispatcher.utter_template('utter_out_of_context',tracker)
      else:
        dispatcher.utter_template('utter_greet',tracker)
        dispatcher.utter_template('utter_start',tracker)
        #return [Restarted()]
     # return [FollowupAction("action_search_jobs")]
      

class action_questions(Action):
    def name(self) -> Text:
        return "action_questions"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
      
      faq = tracker.get_slot('faq')
          #'utter_{}'.format(faq.upper())
      dispatcher.utter_template('utter_{}'.format(faq.upper()),tracker)





#      dispatcher.utter_template('utter_{}'.format(faq.upper()),tracker)


class action_search_exp(Action):
    def name(self) -> Text:
        return "action_search_exp"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
      conn = sqlite3.connect('job_data.db')     
      company = tracker.get_slot('company')
      job = tracker.get_slot('job')
      q = conn.execute("select exp_req from joblistings where company='{}' and position='{}' ".format(company.lower(),job.lower()))
      
      r=(q.fetchall())
      for row in r:
          x=row[0]
    
      dispatcher.utter_message(x+' years')
      dispatcher.utter_template('utter_ask_job_queries',tracker)



class action_search_jobtime(Action):
    def name(self) -> Text:
        return "action_search_jobtime"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
      conn = sqlite3.connect('job_data.db')     
      company = tracker.get_slot('company')
      job = tracker.get_slot('job')
      q = conn.execute("select job_time from joblistings where company='{}' and position='{}' ".format(company.lower(),job.lower()))
      
      r=(q.fetchall())
      for row in r:
          x=row[0]
    
      dispatcher.utter_message('timing is :' + x)
      dispatcher.utter_template('utter_ask_job_queries',tracker)



   
class action_search_salary(Action):
    def name(self) -> Text:
        return "action_search_salary"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
      conn = sqlite3.connect('job_data.db')     
      company = tracker.get_slot('company')
      job = tracker.get_slot('job')
      q = conn.execute("select package from joblistings where company='{}' and position='{}' ".format(company.lower(),job.lower()))
      
      r=(q.fetchall())
      for row in r:
          x=row[0]
    
      dispatcher.utter_message(x)
      dispatcher.utter_template('utter_ask_job_queries',tracker)

class action_search_address(Action):
    def name(self) -> Text:
        return "action_search_address"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
      conn = sqlite3.connect('job_data.db')     
      cuisine = tracker.get_slot('company')
      q = conn.execute("select job_location from joblistings where company='{}' ".format(cuisine.lower()))
      
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
      q = conn.execute("select skills_req from joblistings where company='{}' OR position='{}' ".format(cuisine.lower(),cuisine.lower()))

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
      q = conn.execute("select qual_req from joblistings where company='{}' OR position='{}' ".format(cuisine.lower(),cuisine.lower()))
      
      r=(q.fetchall())
      for row in r:
          x=row[0]
      
      dispatcher.utter_message("qualifications required are " + x)
      dispatcher.utter_template('utter_ask_job_queries',tracker)
       
        
        
        
class action_restarting(Action):
    """ This is for restarting the chat"""

    def name(self):
        return "action_restarting"

    def run(self, dispatcher, tracker, domain):
        
        return [Restarted()]
