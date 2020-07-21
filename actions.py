# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union

import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.events import ReminderScheduled, UserUtteranceReverted, EventType, ConversationPaused, SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
import time
import datetime


INCOMING_ENDPOINT_URL = "http://localhost:3000/api/apps/public/646b8e7d-f1e1-419e-9478-10d0f5bc74d9/incoming"

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []


class SalesForm(FormAction):
    """Collects sales information and adds it to the spreadsheet"""

    def name(self):
        return "sales_form"

    @staticmethod
    def required_slots(tracker):
        return [
            "business_email",
        ]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "business_email": [
                self.from_entity(entity="email"),
                self.from_text(intent="inform"),
            ],
        }

    def validate_business_email(
        self, value, dispatcher, tracker, domain
    ) -> Dict[Text, Any]:
        """Check to see if an email entity was actually picked up by duckling."""

        if any(tracker.get_latest_entity_values("email")):
            # entity was picked up, validate slot
            return {"business_email": value}
        else:
            # no entity was picked up, we want to ask again
            dispatcher.utter_message(template="utter_no_email")
            return {"business_email": None}


    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_message("Thanks for getting in touch, we’ll contact you soon")
        return []


class HandoverAction(Action):

    def name(self) -> Text:
        return "action_handover"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Sorry I couldn't solve your problem. I'm attempting to transfer you to an online agent");
        time.sleep(1)

        payload = {
            'action': 'handover',
            'sessionId': tracker.sender_id
        }

        response = requests.post(INCOMING_ENDPOINT_URL, data=payload)
        print('Handover Endpoint response', response)

        return []


class ActionSetReminder(Action):
    """Schedules a reminder, supplied with the last message's entities."""

    def name(self) -> Text:
        return "action_set_reminder"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("I will remind you in 10 seconds. Please note, you will only see the next message if callbacks are enabled")
        date = datetime.datetime.now() + datetime.timedelta(seconds=10)

        reminder = ReminderScheduled(
            "action_react_to_reminder",
            trigger_date_time=date,
            name="my_reminder",
            kill_on_user_message=False,
        )

        return [reminder]


class ActionReactToReminder(Action):
    """Reminds the user to call someone."""

    def name(self) -> Text:
        return "action_react_to_reminder"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(f"Reminder to call!")

        return []


class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:

        dispatcher.utter_message(template="utter_default")
        return [UserUtteranceReverted()]
