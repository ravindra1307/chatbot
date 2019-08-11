
  
  
## think path
* greet
  - utter_greet
* think
  - utter_think
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
  - utter_more
* goodbye
  - utter_goodbye

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
 
  
## job path
* greet
  - utter_greet
* skills_job{"company": "amazon"}
  - action_skills
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye

## job path
* greet
  - utter_greet
* skills_job{"job": "ml engineer"}
  - action_skills
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye
  
  
## job profile path
* greet
  - utter_greet
* job_profile
  - utter_job_profile
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye


## company address path 0
* greet
  - utter_greet
* company_address{"location": "bhopal","company": "google"}
  - action_search_address
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye

## company address path 1
* greet
  - utter_greet
* company_address{"company": "microsoft"}
  - action_search_address
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye

## company address path 2
* greet
  - utter_greet
* company_address{"company": "tcs","location": "mumbai"}
  - action_search_address
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye
  
## company address path 3
* greet
  - utter_greet
* company_address{"company": "nvidia"}
  - action_search_address
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye

## interview round path
* greet
  - utter_greet
* interview_round{"company": "tata"}
  - utter_interview_round
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye


## application path
* greet
  - utter_greet
* application_status
  - utter_application
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye


## interview document path
* greet
  - utter_greet
* interview_document
  - utter_interview_document
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye

## stupid question path
* greet
  - utter_greet
* stupid
  - utter_stupid_question
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye  
  
  
## holidays
* greet
  - utter_greet
* holidays
  - utter_holidays
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye


## user ideal path
* greet
  - utter_greet
* user_ideal
  - utter_user_ideal
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
 
 
## helpful path
* greet
  - utter_greet
* helpful
  - utter_helpful
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye


## company instructions path
* greet
  - utter_greet
* company_instructions
  - utter_company_instructions
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
 
 
## popular company path
* greet
  - utter_greet
* popular_company{"company": "intel"}
  - utter_popular_company
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye  
  
## company job time path
* greet
  - utter_greet
* company_job_time
  - utter_company_job_time
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
 
 
## company apti ans path
* greet
  - utter_greet
* company_apti_ans
  - utter_company_apti_ans
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
 
 
## company better path
* greet
  - utter_greet
* company_better{"company": "nvidia","company": "amd"}
  - utter_company_better
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye


## company achievement path
* greet
  - utter_greet
* company_achievement{"company": "asus"}
  - utter_company_achievement
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye


## interview time path
* greet
  - utter_greet
* interview_time
  - utter_interview_time
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye

## salary path
* greet
  - utter_greet
* salary
  - utter_salary
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye

## interview taker path
* greet
  - utter_greet
* charge
  - utter_charge
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye  
  
## company vacancies path
* greet
  - utter_greet
* company_vacancies{"company": "acer"}
  - utter_company_vacancies
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye

## job match path
* greet
  - utter_greet
* job_match
  - utter_job_match
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye


## work LMN employee
* greet
  - utter_greet
* LMN
  - utter_LMN
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye

## interview success path
* greet
  - utter_greet
* interview_success
  - utter_interview_success
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye


## company motto
* greet
  - utter_greet
* company_motto{"company": "hp"}
  - utter_company_motto
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
 
 
## interview date path
* greet
  - utter_greet
* interview_date
  - utter_interview_date
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
 
## interview history path  
* greet
  - utter_greet
* interview_history
  - utter_interview_history
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye


## job description applied path
* greet
  - utter_greet
* job_description_applied
  - utter_job_description_applied
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye

## eligibility path
* greet
  - utter_greet
* eligibility_criteria{"job": "ml engineer"}
  - utter_eligibility_criteria
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye
  
## eligibility path 2
* greet
  - utter_greet
* eligibility_criteria{"job": "data scientist"}
  - utter_eligibility_criteria
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye
  
  



## fallback
- utter_unclear

