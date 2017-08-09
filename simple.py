# -*- coding: utf-8 -*-
"""
    simple-skill.py
    ~~~~~~~~~~~~~~~
    a simple Alexa skill to return a random fact about Cuttlefish
"""

from __future__ import print_function
from random import choice


# --------------- Helpers that build all of the responses ----------------------


def build_speechlet_response(title, output, reprompt_text):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        }
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Cuttlesoft"
    speech_output = "Welcome to the Cuttlesoft skill. " \
                    "Ask me about either Cuttlesoft or the amazing cuttlefish"

    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "I can tell you more about Cuttlesoft or some interesting" \
                    "facts about the cuttlefish"
    return build_response(
        session_attributes,
        build_speechlet_response(card_title, speech_output, reprompt_text))


def handle_session_end_request():
    card_title = "Thank you!"
    speech_output = "Cheers, cuttle lover."
    return build_response({},
        build_speechlet_response(card_title, speech_output, None))


def get_cuttlefish_fact(intent):
    """replies with a random cuttlefish fact"""

    facts = [
        "There are over 120 distinct species of cuttlefish.",
        "Cuttlefish can manually control their buoyancy",
        "Baby cuttlefish and small adults use their arms to walk along the ocean floor",
        "Cuttlefish can change to be almost any color, even though they're colorblind",
        "Cuttlefish mimic the shape and texture of objects around them to better hide",
        """Cuttlefish can see behind them, their W-shaped pupils allow them a
        wider horizontal range of vision.""",
        "Females can store multiple sperm packets, then select one for fertilizing",
        """Male cuttlefish will cross dress to get close to females, they do this by tucking their
        fourth pair of arms, the female only has three)""",
        "Cuttlefish hunt using hypnosis turning their bodies into pulsating light and color shows."
    ]

    card_title = "The Amazing Cuttlefish"
    speech_output = choice(facts)
    reprompt_text = "I'm not sure what you asked." \
                    "You can ask me for a cuttlefish fact by saying " \
                    "tell me about cuttlefish."

    return build_response({},
        build_speechlet_response(card_title, speech_output, reprompt_text))


# --------------- Events ------------------

def on_launch(launch_request):
    """ Called when the user launches the skill without specifying what they want"""
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request):
    """ Called when the user specifies an intent for this skill """

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "CuttlefishFactIntent":
        return get_cuttlefish_fact(intent)
    # Dispatch to your skill's welcome intent handler
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    else:
        raise ValueError("Invalid intent")


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """

    appId = event['session']['application']['applicationId']

    print("event.session.application.applicationId=" + appId)

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (appId != "amzn1.ask.skill.xxx"):
    #     raise ValueError("Invalid Application ID")

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'])

    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'])
