## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
  
## Some question from FAQ
* faq
  - respond_faq
  
## sales form
* contact_sales
    - sales_form                   <!--Run the sales_form action-->
    - form{"name": "sales_form"}   <!--Activate the form-->
    - form{"name": null}           <!--Deactivate the form-->
    
## handover
* human_handoff
    - action_handover
    
## reminder user
* reminder
    - action_set_reminder
    
## greet and handover
* greet
  - utter_greet
* human_handoff
  - action_handover 
  
## greet and reminder
* greet
  - utter_greet
* reminder
  - action_set_reminder



## interactive_story_1
* greet
    - utter_greet
* human_handoff
    - action_handover
* reminder
    - action_set_reminder
* greet
    - utter_greet
* faq
    - respond_faq
* greet
    - utter_greet
* human_handoff
    - action_handover

## interactive_story_2
* greet
    - utter_greet
* human_handoff
    - action_handover
* reminder
    - action_set_reminder
* greet
    - utter_greet
* greet
    - utter_greet
* reminder
    - action_set_reminder


## out of scope
* out_of_scope
    - action_default_fallback