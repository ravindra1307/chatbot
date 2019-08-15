
  
 ## think path
* greet
  - utter_greet
  - action_restarting
* think
  - utter_think
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
  - utter_more
* goodbye
  - utter_goodbye
  - action_restarting

## think path2
* think
  - utter_think
  - utter_did_that_help
* deny
  - utter_ask_again
* think
  - utter_think
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye
  - action_restarting
 
  
## job path
* greet
  - utter_greet
  - action_restarting	
* skills_job{"company": "amazon"}
  - action_skills
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye
  - action_restarting

## job path
* greet
  - utter_greet
  - action_restarting
* skills_job{"job": "ml engineer"}
  - action_skills
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye
  - action_restarting
  
  
## job profile path
* greet
  - utter_greet
  - action_restarting
* job_profile
  - utter_job_profile
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting


## company address path 0
* greet
  - utter_greet
  - action_restarting
* company_address{"location": "bhopal","company": "google"}
  - action_search_address
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting
  

## company address path 1
* greet
  - utter_greet
  - action_restarting
* company_address{"company": "microsoft"}
  - action_search_address
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting

## company address path 2
* greet
  - utter_greet
  - action_restarting
* company_address{"company": "tcs","location": "mumbai"}
  - action_search_address
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting
  
## company address path 3
* greet
  - utter_greet
  - action_restarting
* company_address{"company": "nvidia"}
  - action_search_address
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting

## interview round path
* greet
  - utter_greet
  - action_restarting
* interview_round{"company": "tata"}
  - utter_interview_round
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting


## application path
* greet
  - utter_greet
  - action_restarting
* application_status
  - utter_application
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting


## interview document path
* greet
  - utter_greet
  - action_restarting
* interview_document
  - utter_interview_document
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting

## stupid question path
* greet
  - utter_greet
  - action_restarting
* stupid
  - utter_stupid_question
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting  
  
  
## holidays
* greet
  - utter_greet
  - action_restarting
* holidays
  - utter_holidays
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting


## user ideal path
* greet
  - utter_greet
  - action_restarting
* user_ideal
  - utter_user_ideal
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting 
 
 
## helpful path
* greet
  - utter_greet
  - action_restarting
* helpful
  - utter_helpful
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting


## company instructions path
* greet
  - utter_greet
  - action_restarting
* company_instructions
  - utter_company_instructions
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting 
 
 
## popular company path
* greet
  - utter_greet
  - action_restarting
* popular_company{"company": "intel"}
  - utter_popular_company
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting  
  
## company job time path
* greet
  - utter_greet
  - action_restarting
* company_job_time
  - utter_company_job_time
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting 
 
 
## company apti ans path
* greet
  - utter_greet
  - action_restarting
* company_apti_ans
  - utter_company_apti_ans
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting 
 
 
## company better path
* greet
  - utter_greet
  - action_restarting
* company_better{"company": "nvidia","company": "amd"}
  - utter_company_better
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting


## company achievement path
* greet
  - utter_greet
  - action_restarting
* company_achievement{"company": "asus"}
  - utter_company_achievement
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting


## interview time path
* greet
  - utter_greet
  - action_restarting
* interview_time
  - utter_interview_time
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting

## salary path
* greet
  - utter_greet
  - action_restarting
* salary
  - utter_salary
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting

## interview taker path
* greet
  - utter_greet
  - action_restarting
* charge
  - utter_charge
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting  
  
## company vacancies path
* greet
  - utter_greet
  - action_restarting
* company_vacancies{"company": "acer"}
  - utter_company_vacancies
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting

## job match path
* greet
  - utter_greet
  - action_restarting
* job_match
  - utter_job_match
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting


## work LMN employee
* greet
  - utter_greet
  - action_restarting
* LMN
  - utter_LMN
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting

## interview success path
* greet
  - utter_greet
  - action_restarting
* interview_success
  - utter_interview_success
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting


## company motto
* greet
  - utter_greet
  - action_restarting
* company_motto{"company": "hp"}
  - utter_company_motto
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting 
 
 
## interview date path
* greet
  - utter_greet
  - action_restarting
* interview_date
  - utter_interview_date
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting 
 
## interview history path  
* greet
  - utter_greet
  - action_restarting
* interview_history
  - utter_interview_history
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting


## job description applied path
* greet
  - utter_greet
  - action_restarting
* job_description_applied
  - utter_job_description_applied
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting

## eligibility path
* greet
  - utter_greet
  - action_restarting
* eligibility_criteria{"job": "ml engineer"}
  - utter_eligibility_criteria
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting
  
## eligibility path 2
* greet
  - utter_greet
  - action_restarting
* eligibility_criteria{"job": "data scientist"}
  - utter_eligibility_criteria
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting
  
  



## fallback
- utter_unclear