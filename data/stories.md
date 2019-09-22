## questions 1
* greet
  - action_greet
* questions{"faq":"NASA"}
 - action_questions
 - action_restarting

## questions 2
* greet
  - action_greet
* questions{"faq":"CS"}
 - action_questions
 - action_restarting
 
 ## questions 3
* greet
  - action_greet
* questions{"faq":"CA"}
 - action_questions
 - action_restarting
 
 ## questions 4
* greet
  - action_greet
* questions{"faq":"MBA"}
 - action_questions
 - action_restarting
 
 ## questions 5
* greet
  - action_greet
* questions{"faq":"ARC"}
 - action_questions
 - action_restarting

## think path
* greet
  - action_greet
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
  - action_greet	
* skills_job{"company": "amazon"}
  - action_skills
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye
  - action_restarting

## job path 1
* greet
  - action_greet
* skills_job{"job": "ml engineer"}
  - action_skills
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye
  - action_restarting
  
## job profile more without 0
* job_profile
  - job_form
  - form{"name": "job_form"}
  - form{"name": null}
  - action_search_jobs
* more
  - action_search_jobs_more
* set job slots{"company": "infosys","job": "machine learning engineer"}
  - action_search_job_desc
* salary
  - action_search_salary
* company_job_time
  - action_search_jobtime 
* eligibility_criteria
  - action_eligibility_criteria 
* company_job_time
  - action_search_jobtime 
* eligibility_criteria
  - action_eligibility_criteria
* experience_required
  - action_search_exp
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting  
  
  
  ## job profile more path 1
* greet
  - action_greet
* job_profile
  - job_form
  - form{"name": "job_form"}
  - form{"name": null}
  - action_search_jobs
* more
  - action_search_jobs_more
* set job slots{"company": "microsoft","job": "product manager"}
  - action_search_job_desc
* company_job_time
  - action_search_jobtime
* experience_required
  - action_search_exp
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting

## job profile more path 2
* greet
  - action_greet
* job_profile
  - job_form
  - form{"name": "job_form"}
  - form{"name": null}
  - action_search_jobs
* more
  - action_search_jobs_more
* set job slots{"company": "amazon","job": "ml engineer"}
  - action_search_job_desc
* salary
  - action_search_salary
* company_job_time
  - action_search_jobtime 
* eligibility_criteria
  - action_eligibility_criteria 
* eligibility_criteria
  - action_eligibility_criteria
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting

## job profile more path 3
* greet
  - action_greet
* job_profile
  - job_form
  - form{"name": "job_form"}
  - form{"name": null}
  - action_search_jobs
* more
  - action_search_jobs_more
* set job slots{"company": "tcs","job": "system engineer"}
  - action_search_job_desc
* company_job_time
  - action_search_jobtime
* experience_required
  - action_search_exp
* salary
  - action_search_salary
* company_job_time
  - action_search_jobtime 
* eligibility_criteria
  - action_eligibility_criteria 
* eligibility_criteria
  - action_eligibility_criteria
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting

## job profile more path 4
* greet
  - action_greet
* job_profile
  - job_form
  - form{"name": "job_form"}
  - form{"name": null}
  - action_search_jobs
* more
  - action_search_jobs_more
* set job slots{"company": "tcs","job": "system engineer"}
  - action_search_job_desc
* company_job_time
  - action_search_jobtime
* experience_required
  - action_search_exp
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting

## job profile more path 5
* greet
  - action_greet
* job_profile
  - job_form
  - form{"name": "job_form"}
  - form{"name": null}
  - action_search_jobs
* more
  - action_search_jobs_more
* set job slots
  - action_search_job_desc
* salary
  - action_search_salary
* company_job_time
  - action_search_jobtime 
* eligibility_criteria
  - action_eligibility_criteria 
* eligibility_criteria
  - action_eligibility_criteria
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting
  
## job profile previous without 0
* job_profile
  - job_form
  - form{"name": "job_form"}
  - form{"name": null}
  - action_search_jobs
* more
  - action_search_jobs_more
* previous
  - action_search_jobs
* set job slots{"company": "infosys","job": "machine learning engineer"}
  - action_search_job_desc
* salary
  - action_search_salary
* company_job_time
  - action_search_jobtime 
* eligibility_criteria
  - action_eligibility_criteria 
* eligibility_criteria
  - action_eligibility_criteria
* company_job_time
  - action_search_jobtime 
* eligibility_criteria
  - action_eligibility_criteria 
* eligibility_criteria
  - action_eligibility_criteria
* experience_required
  - action_search_exp
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting  
  
  
## job profile previous path 1
* greet
  - action_greet
* job_profile
  - job_form
  - form{"name": "job_form"}
  - form{"name": null}
  - action_search_jobs
* more
  - action_search_jobs_more
* previous
  - action_search_jobs  
* set job slots{"company": "microsoft","job": "product manager"}
  - action_search_job_desc
* experience_required
  - action_search_exp
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting

## job profile previous path 2
* greet
  - action_greet
* job_profile
  - job_form
  - form{"name": "job_form"}
  - form{"name": null}
  - action_search_jobs
* more
  - action_search_jobs_more
* previous
  - action_search_jobs
* set job slots{"company": "amazon","job": "ml engineer"}
  - action_search_job_desc
* salary
  - action_search_salary
* company_job_time
  - action_search_jobtime 
* eligibility_criteria
  - action_eligibility_criteria 
* eligibility_criteria
  - action_eligibility_criteria
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting

## job profile previous path 3
* greet
  - action_greet
* job_profile
  - job_form
  - form{"name": "job_form"}
  - form{"name": null}
  - action_search_jobs
* more
  - action_search_jobs_more
* previous
  - action_search_jobs
* set job slots{"company": "tcs","job": "system engineer"}
  - action_search_job_desc
* company_job_time
  - action_search_jobtime
* experience_required
  - action_search_exp
* salary
  - action_search_salary
* company_job_time
  - action_search_jobtime 
* eligibility_criteria
  - action_eligibility_criteria 
* eligibility_criteria
  - action_eligibility_criteria
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting

## job profile previous path 4
* greet
  - action_greet
* job_profile
  - job_form
  - form{"name": "job_form"}
  - form{"name": null}
  - action_search_jobs
* more
  - action_search_jobs_more
* previous
  - action_search_jobs
* set job slots{"company": "tcs","job": "system engineer"}
  - action_search_job_desc
* experience_required
  - action_search_exp
* salary
  - action_search_salary
* company_job_time
  - action_search_jobtime 
* eligibility_criteria
  - action_eligibility_criteria 
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting

## job profile previous path 5
* greet
  - action_greet
* job_profile
  - job_form
  - form{"name": "job_form"}
  - form{"name": null}
  - action_search_jobs
* more
  - action_search_jobs_more
* previous
  - action_search_jobs
* set job slots
  - action_search_job_desc
* salary
  - action_search_salary
* company_job_time
  - action_search_jobtime 
* eligibility_criteria
  - action_eligibility_criteria 
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting
 
  
## job profile without 0
* job_profile
  - job_form
  - form{"name": "job_form"}
  - form{"name": null}
  - action_search_jobs
* set job slots{"company": "infosys","job": "machine learning engineer"}
  - action_search_job_desc
* salary
  - action_search_salary
* company_job_time
  - action_search_jobtime 
* eligibility_criteria
  - action_eligibility_criteria 
* company_job_time
  - action_search_jobtime 
* eligibility_criteria
  - action_eligibility_criteria
* experience_required
  - action_search_exp
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting

## job profile without 1
* job_profile
  - job_form
  - form{"name": "job_form"}
  - form{"name": null}
  - action_search_jobs
* set job slots{"company": "infosys","job": "machine learning engineer"}
  - action_search_job_desc
* salary
  - action_search_salary
* goodbye
  - utter_goodbye 
  - action_restarting  
  
  
## job profile path 0
* greet
  - action_greet
* job_profile
  - job_form
  - form{"name": "job_form"}
  - form{"name": null}
  - action_search_jobs
* set job slots{"company": "tcs","job": "system engineer"}
  - action_search_job_desc
* salary
  - action_search_salary
* company_job_time
  - action_search_jobtime 
* eligibility_criteria
  - action_eligibility_criteria
* company_job_time
  - action_search_jobtime 
* eligibility_criteria
  - action_eligibility_criteria
* experience_required
  - action_search_exp
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting

## job profile path 1
* greet
  - action_greet
* job_profile
  - job_form
  - form{"name": "job_form"}
  - form{"name": null}
  - action_search_jobs
* set job slots{"company": "microsoft","job": "product manager"}
  - action_search_job_desc
* experience_required
  - action_search_exp
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting

## job profile path 2
* greet
  - action_greet
* job_profile
  - job_form
  - form{"name": "job_form"}
  - form{"name": null}
  - action_search_jobs
* set job slots{"company": "amazon","job": "ml engineer"}
  - action_search_job_desc
* salary
  - action_search_salary
* company_job_time
  - action_search_jobtime 
* eligibility_criteria
  - action_eligibility_criteria
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting

## job profile path 3
* greet
  - action_greet
* job_profile
  - job_form
  - form{"name": "job_form"}
  - form{"name": null}
  - action_search_jobs
* set job slots{"company": "tcs","job": "system engineer"}
  - action_search_job_desc
* experience_required
  - action_search_exp
* salary
  - action_search_salary
* company_job_time
  - action_search_jobtime 
* eligibility_criteria
  - action_eligibility_criteria
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting

## job profile path 4
* greet
  - action_greet
* job_profile
  - job_form
  - form{"name": "job_form"}
  - form{"name": null}
  - action_search_jobs
* set job slots{"company": "tcs","job": "system engineer"}
  - action_search_job_desc
* experience_required
  - action_search_exp
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting

## job profile path 5
* greet
  - action_greet
* job_profile
  - job_form
  - form{"name": "job_form"}
  - form{"name": null}
  - action_search_jobs
* set job slots
  - action_search_job_desc
* salary
  - action_search_salary
* company_job_time
  - action_search_jobtime 
* eligibility_criteria
  - action_eligibility_criteria
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting

## job profile path 6
* greet
  - action_greet
* job_profile
  - job_form
  - form{"name": "job_form"}
  - form{"name": null}
  - action_search_jobs
* set job slots{"company": "microsoft","job": "product manager"}
  - action_search_job_desc
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting

## job profile path 7
* greet
  - action_greet
* job_profile
  - job_form
  - form{"name": "job_form"}
  - form{"name": null}
  - action_search_jobs{"company": "google","job": "data scientist"}
* set job slots
  - action_search_job_desc
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting

## job profile path 8
* greet
  - action_greet
* job_profile
  - job_form
  - form{"name": "job_form"}
  - form{"name": null}
  - action_search_jobs
* set job slots{"company": "microsoft","job": "product manager"}
  - action_search_job_desc

## job profile path 9
* greet
  - action_greet
* job_profile
  - job_form
  - form{"name": "job_form"}
  - form{"name": null}
  - action_search_jobs
* set job slots{"company": "microsoft","job": "product manager"}
  - action_search_job_desc

## job profile path 10
* greet
  - action_greet
* job_profile
  - job_form
  - form{"name": "job_form"}
  - form{"name": null}
  - action_search_jobs{"company": "google","job": "data scientist"}
* set job slots
  - action_search_job_desc

## job profile path 11
* greet
  - action_greet
* job_profile
  - job_form
  - form{"name": "job_form"}
  - form{"name": null}
  - action_search_jobs{"company": "google","job": "data scientist"}
* set job slots
  - action_search_job_desc

## company address path 0
* greet
  - action_greet
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
  - action_greet
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
  - action_greet
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
  - action_greet
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
  - action_greet
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
  - action_greet
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
  - action_greet
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
  - action_greet
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
  - action_greet
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
  - action_greet
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
  - action_greet
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
  - action_greet
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
  - action_greet
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
  - action_greet
* company_job_time
  - action_search_jobtime
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting 

## company job time path 1
* greet
  - action_greet
* company_job_time
  - action_search_jobtime
* affirm OR thanks
  - utter_gratitude

 
## company apti ans path
* greet
  - action_greet
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
  - action_greet
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
  - action_greet
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
  - action_greet
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
  - action_greet
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
  - action_greet
* charge
  - utter_charge
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting  


## job match path
* greet
  - action_greet
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
  - action_greet
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
  - action_greet
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
  - action_greet
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
  - action_greet
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
  - action_greet
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
  - action_greet
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
  - action_greet
* eligibility_criteria{"job": "ml engineer"}
  - action_eligibility_criteria
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting
  
## eligibility path 2
* greet
  - action_greet
* eligibility_criteria{"job": "data scientist"}
  - action_eligibility_criteria
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye 
  - action_restarting
  
  



## fallback
- utter_unclear















## deny think path
* greet
  - action_greet
* think
  - utter_think
  - utter_did_that_help
* deny
  - utter_ask_again
  - action_restarting



## deny think path2
* think
  - utter_think
  - utter_did_that_help
* deny
  - utter_ask_again
  - action_restarting
* think
  - utter_think
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye
  - action_restarting
 
 
  
## deny job path
* greet
  - action_greet	
* skills_job{"company": "amazon"}
  - action_skills
  - utter_did_that_help
* deny
  - utter_ask_again
  - action_restarting



## deny job path 1
* greet
  - action_greet
* skills_job{"job": "ml engineer"}
  - action_skills
  - utter_did_that_help
* deny
  - utter_ask_again
  - action_restarting
  
  
  
  
## deny job profile path 0
* greet
  - action_greet
* job_profile
  - job_form
  - form{"name": "job_form"}
  - form{"name": null}
  - action_search_jobs
* set job slots{"company": "tcs","job": "system engineer"}
  - action_search_job_desc
* experience_required
  - action_search_exp
* salary
  - action_search_salary
* company_job_time
  - action_search_jobtime 
* eligibility_criteria
  - action_eligibility_criteria
* company_job_time
  - action_search_jobtime 
* eligibility_criteria
  - action_eligibility_criteria
* deny
  - utter_ask_again 
  - action_restarting



## deny job profile path 1
* greet
  - action_greet
* job_profile
  - job_form
  - form{"name": "job_form"}
  - form{"name": null}
  - action_search_jobs
* set job slots{"company": "microsoft","job": "product manager"}
  - action_search_job_desc
* experience_required
  - action_search_exp
* salary
  - action_search_salary
* company_job_time
  - action_search_jobtime 
* eligibility_criteria
  - action_eligibility_criteria
* company_job_time
  - action_search_jobtime 
* eligibility_criteria
  - action_eligibility_criteria
* deny
  - utter_ask_again 
  - action_restarting



## deny job profile path 2
* greet
  - action_greet
* job_profile
  - job_form
  - form{"name": "job_form"}
  - form{"name": null}
  - action_search_jobs
* set job slots{"company": "amazon","job": "ml engineer"}
  - action_search_job_desc
* experience_required
  - action_search_exp
* deny
  - utter_ask_again 
  - action_restarting



## deny job profile path 3
* greet
  - action_greet
* job_profile
  - job_form
  - form{"name": "job_form"}
  - form{"name": null}
  - action_search_jobs
* set job slots{"company": "tcs","job": "system engineer"}
  - action_search_job_desc
* salary
  - action_search_salary
* company_job_time
  - action_search_jobtime 
* eligibility_criteria
  - action_eligibility_criteria
* company_job_time
  - action_search_jobtime 
* eligibility_criteria
  - action_eligibility_criteria
* deny
  - utter_ask_again 
  - action_restarting



## deny job profile path 4
* greet
  - action_greet
* job_profile
  - job_form
  - form{"name": "job_form"}
  - form{"name": null}
  - action_search_jobs
* set job slots{"company": "tcs","job": "system engineer"}
  - action_search_job_desc
* salary
  - action_search_salary
* company_job_time
  - action_search_jobtime 
* eligibility_criteria
  - action_eligibility_criteria
* company_job_time
  - action_search_jobtime 
* eligibility_criteria
  - action_eligibility_criteria
* experience_required
  - action_search_exp
* deny
  - utter_ask_again 
  - action_restarting



## deny job profile path 5
* greet
  - action_greet
* job_profile
  - job_form
  - form{"name": "job_form"}
  - form{"name": null}
  - action_search_jobs
* set job slots
  - action_search_job_desc
* deny
  - utter_ask_again 
  - action_restarting



## deny job profile path 6
* greet
  - action_greet
* job_profile
  - job_form
  - form{"name": "job_form"}
  - form{"name": null}
  - action_search_jobs
* set job slots{"company": "microsoft","job": "product manager"}
  - action_search_job_desc
* deny
  - utter_ask_again 
  - action_restarting



## deny job profile path 7
* greet
  - action_greet
* job_profile
  - job_form
  - form{"name": "job_form"}
  - form{"name": null}
  - action_search_jobs{"company": "google","job": "data scientist"}
* set job slots
  - action_search_job_desc
* company_job_time
  - action_search_jobtime
* deny
  - utter_ask_again 
  - action_restarting



## deny job profile path 8
* greet
  - action_greet
* job_profile
  - job_form
  - form{"name": "job_form"}
  - form{"name": null}
  - action_search_jobs
* set job slots{"company": "microsoft","job": "product manager"}
  - action_search_job_desc



## deny job profile path 9
* greet
  - action_greet
* job_profile
  - job_form
  - form{"name": "job_form"}
  - form{"name": null}
  - action_search_jobs
* set job slots{"company": "microsoft","job": "product manager"}
  - action_search_job_desc



## deny job profile path 10
* greet
  - action_greet
* job_profile
  - job_form
  - form{"name": "job_form"}
  - form{"name": null}
  - action_search_jobs{"company": "google","job": "data scientist"}
* set job slots
  - action_search_job_desc



## deny job profile path 11
* greet
  - action_greet
* job_profile
  - job_form
  - form{"name": "job_form"}
  - form{"name": null}
  - action_search_jobs{"company": "google","job": "data scientist"}
* set job slots
  - action_search_job_desc



## deny company address path 0
* greet
  - action_greet
* company_address{"location": "bhopal","company": "google"}
  - action_search_address
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting
  
  

## deny company address path 1
* greet
  - action_greet
* company_address{"company": "microsoft"}
  - action_search_address
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting



## deny company address path 2
* greet
  - action_greet
* company_address{"company": "tcs","location": "mumbai"}
  - action_search_address
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting
  
  
  
## deny company address path 3
* greet
  - action_greet
* company_address{"company": "nvidia"}
  - action_search_address
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting



## deny interview round path
* greet
  - action_greet
* interview_round{"company": "tata"}
  - utter_interview_round
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting




## deny application path
* greet
  - action_greet
* application_status
  - utter_application
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting



## deny interview document path
* greet
  - action_greet
* interview_document
  - utter_interview_document
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting



## deny stupid question path
* greet
  - action_greet
* stupid
  - utter_stupid_question
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting  
  
  
  
  
## deny holidays
* greet
  - action_greet
* holidays
  - utter_holidays
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting




## deny user ideal path
* greet
  - action_greet
* user_ideal
  - utter_user_ideal
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting 
 
 
 
 
## deny helpful path
* greet
  - action_greet
* helpful
  - utter_helpful
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting
  


## deny company instructions path
* greet
  - action_greet
* company_instructions
  - utter_company_instructions
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting 
 
 
 
## deny popular company path
* greet
  - action_greet
* popular_company{"company": "intel"}
  - utter_popular_company
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting  
  
  
  
## deny company job time path
* greet
  - action_greet
* company_job_time
  - utter_company_job_time
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting 
 
 
 
## deny company apti ans path
* greet
  - action_greet
* company_apti_ans
  - utter_company_apti_ans
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting 
 
 
 
## deny company better path
* greet
  - action_greet
* company_better{"company": "nvidia","company": "amd"}
  - utter_company_better
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting



## deny company achievement path
* greet
  - action_greet
* company_achievement{"company": "asus"}
  - utter_company_achievement
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting



## deny interview time path
* greet
  - action_greet
* interview_time
  - utter_interview_time
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting


## deny salary path
* greet
  - action_greet
* salary
  - utter_salary
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting


## deny interview taker path
* greet
  - action_greet
* charge
  - utter_charge
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting  
  
  




## deny job match path
* greet
  - action_greet
* job_match
  - utter_job_match
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting



## deny work LMN employee
* greet
  - action_greet
* LMN
  - utter_LMN
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting



## deny interview success path
* greet
  - action_greet
* interview_success
  - utter_interview_success
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting



## deny company motto
* greet
  - action_greet
* company_motto{"company": "hp"}
  - utter_company_motto
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting 
 
 
 
## deny interview date path
* greet
  - action_greet
* interview_date
  - utter_interview_date
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting 
 
 
 
## deny interview history path  
* greet
  - action_greet
* interview_history
  - utter_interview_history
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting



## deny job description applied path
* greet
  - action_greet
* job_description_applied
  - utter_job_description_applied
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting



## deny eligibility path
* greet
  - action_greet
* eligibility_criteria{"job": "ml engineer"}
  - action_eligibility_criteria
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting
  
  
  
## deny eligibility path 2
* greet
  - action_greet
* eligibility_criteria{"job": "data scientist"}
  - action_eligibility_criteria
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting
  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

## nogreet think path
* greet
  - action_greet
* think
  - utter_think
  - utter_did_that_help
* deny
  - utter_ask_again
  - action_restarting

## nogreet think path2
* think
  - utter_think
  - utter_did_that_help
* deny
  - utter_ask_again
  - action_restarting
* think
  - utter_think
  - utter_did_that_help
* affirm OR thanks
  - utter_gratitude
* goodbye
  - utter_goodbye
  - action_restarting
 
  
## nogreet job path
* greet
  - action_greet	
* skills_job{"company": "amazon"}
  - action_skills
  - utter_did_that_help
* deny
  - utter_ask_again
  - action_restarting

## nogreet job path 1
* greet
  - action_greet
* skills_job{"job": "ml engineer"}
  - action_skills
  - utter_did_that_help
* deny
  - utter_ask_again
  - action_restarting
  
  
## nogreet job profile path 0
* greet
  - action_greet
* job_profile
  - job_form
  - form{"name": "job_form"}
  - form{"name": null}
  - action_search_jobs
* set job slots{"company": "tcs","job": "system engineer"}
  - action_search_job_desc
* deny
  - utter_ask_again 
  - action_restarting

## nogreet job profile path 1
* greet
  - action_greet
* job_profile
  - job_form
  - form{"name": "job_form"}
  - form{"name": null}
  - action_search_jobs
* set job slots{"company": "microsoft","job": "product manager"}
  - action_search_job_desc
* deny
  - utter_ask_again 
  - action_restarting

## nogreet job profile path 2
* greet
  - action_greet
* job_profile
  - job_form
  - form{"name": "job_form"}
  - form{"name": null}
  - action_search_jobs
* set job slots{"company": "amazon","job": "ml engineer"}
  - action_search_job_desc
* deny
  - utter_ask_again 
  - action_restarting

## nogreet job profile path 3
* greet
  - action_greet
* job_profile
  - job_form
  - form{"name": "job_form"}
  - form{"name": null}
  - action_search_jobs
* set job slots{"company": "tcs","job": "system engineer"}
  - action_search_job_desc
* deny
  - utter_ask_again 
  - action_restarting

## nogreet job profile path 4
* greet
  - action_greet
* job_profile
  - job_form
  - form{"name": "job_form"}
  - form{"name": null}
  - action_search_jobs
* set job slots{"company": "tcs","job": "system engineer"}
  - action_search_job_desc
* deny
  - utter_ask_again 
  - action_restarting

## nogreet job profile path 5
* greet
  - action_greet
* job_profile
  - job_form
  - form{"name": "job_form"}
  - form{"name": null}
  - action_search_jobs
* set job slots
  - action_search_job_desc
* deny
  - utter_ask_again 
  - action_restarting

## nogreet job profile path 6
* greet
  - action_greet
* job_profile
  - job_form
  - form{"name": "job_form"}
  - form{"name": null}
  - action_search_jobs
* set job slots{"company": "microsoft","job": "product manager"}
  - action_search_job_desc
* deny
  - utter_ask_again 
  - action_restarting

## nogreet job profile path 7
* greet
  - action_greet
* job_profile
  - job_form
  - form{"name": "job_form"}
  - form{"name": null}
  - action_search_jobs{"company": "google","job": "data scientist"}
* set job slots
  - action_search_job_desc
* deny
  - utter_ask_again 
  - action_restarting

## nogreet job profile path 8
* greet
  - action_greet
* job_profile
  - job_form
  - form{"name": "job_form"}
  - form{"name": null}
  - action_search_jobs
* set job slots{"company": "microsoft","job": "product manager"}
  - action_search_job_desc

## nogreet job profile path 9
* greet
  - action_greet
* job_profile
  - job_form
  - form{"name": "job_form"}
  - form{"name": null}
  - action_search_jobs
* set job slots{"company": "microsoft","job": "product manager"}
  - action_search_job_desc

## nogreet job profile path 10
* greet
  - action_greet
* job_profile
  - job_form
  - form{"name": "job_form"}
  - form{"name": null}
  - action_search_jobs{"company": "google","job": "data scientist"}
* set job slots
  - action_search_job_desc

## nogreet job profile path 11
* greet
  - action_greet
* job_profile
  - job_form
  - form{"name": "job_form"}
  - form{"name": null}
  - action_search_jobs{"company": "google","job": "data scientist"}
* set job slots
  - action_search_job_desc

## nogreet company address path 0
* greet
  - action_greet
* company_address{"location": "bhopal","company": "google"}
  - action_search_address
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting
  

## nogreet company address path 1
* greet
  - action_greet
* company_address{"company": "microsoft"}
  - action_search_address
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting

## nogreet company address path 2
* greet
  - action_greet
* company_address{"company": "tcs","location": "mumbai"}
  - action_search_address
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting
  
## nogreet company address path 3
* greet
  - action_greet
* company_address{"company": "nvidia"}
  - action_search_address
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting

## nogreet interview round path
* greet
  - action_greet
* interview_round{"company": "tata"}
  - utter_interview_round
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting


## nogreet application path
* greet
  - action_greet
* application_status
  - utter_application
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting


## nogreet interview document path
* greet
  - action_greet
* interview_document
  - utter_interview_document
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting

## nogreet stupid question path
* greet
  - action_greet
* stupid
  - utter_stupid_question
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting  
  
  
## nogreet holidays
* greet
  - action_greet
* holidays
  - utter_holidays
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting


## nogreet user ideal path
* greet
  - action_greet
* user_ideal
  - utter_user_ideal
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting 
 
 
## nogreet helpful path
* greet
  - action_greet
* helpful
  - utter_helpful
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting


## nogreet company instructions path
* greet
  - action_greet
* company_instructions
  - utter_company_instructions
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting 
 
 
## nogreet popular company path
* greet
  - action_greet
* popular_company{"company": "intel"}
  - utter_popular_company
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting  
  
## nogreet company job time path
* greet
  - action_greet
* company_job_time
  - utter_company_job_time
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting 
 
 
## nogreet company apti ans path
* greet
  - action_greet
* company_apti_ans
  - utter_company_apti_ans
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting 
 
 
## nogreet company better path
* greet
  - action_greet
* company_better{"company": "nvidia","company": "amd"}
  - utter_company_better
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting


## nogreet company achievement path
* greet
  - action_greet
* company_achievement{"company": "asus"}
  - utter_company_achievement
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting


## nogreet interview time path
* greet
  - action_greet
* interview_time
  - utter_interview_time
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting

## nogreet salary path
* greet
  - action_greet
* salary
  - utter_salary
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting

## nogreet interview taker path
* greet
  - action_greet
* charge
  - utter_charge
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting  
  

## nogreet job match path
* greet
  - action_greet
* job_match
  - utter_job_match
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting


## nogreet work LMN employee
* greet
  - action_greet
* LMN
  - utter_LMN
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting

## nogreet interview success path
* greet
  - action_greet
* interview_success
  - utter_interview_success
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting


## nogreet company motto
* greet
  - action_greet
* company_motto{"company": "hp"}
  - utter_company_motto
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting 
 
 
## nogreet interview date path
* greet
  - action_greet
* interview_date
  - utter_interview_date
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting 
 
## nogreet interview history path  
* greet
  - action_greet
* interview_history
  - utter_interview_history
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting


## nogreet job description applied path
* greet
  - action_greet
* job_description_applied
  - utter_job_description_applied
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting

## nogreet eligibility path
* greet
  - action_greet
* eligibility_criteria{"job": "ml engineer"}
  - action_eligibility_criteria
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting
  
## nogreet eligibility path 2
* greet
  - action_greet
* eligibility_criteria{"job": "data scientist"}
  - action_eligibility_criteria
  - utter_did_that_help
* deny
  - utter_ask_again 
  - action_restarting
  
 