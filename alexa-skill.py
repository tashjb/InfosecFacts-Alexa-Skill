"""
This sample demonstrates a simple skill built with the Amazon Alexa Skills Kit.
The Intent Schema, Custom Slots, and Sample Utterances for this skill, as well
as testing instructions are located at http://amzn.to/1LzFrj6

For additional samples, visit the Alexa Skills Kit Getting Started guide at
http://amzn.to/1LGWsLG
"""

from __future__ import print_function
import random


# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
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
        },
        'shouldEndSession': should_end_session
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
    card_title = "Welcome"
    speech_output = "Welcome to the Cyber Security Facts Alexa Skill. " \
                    "You can ask me to tell you a fact by saying, " \
                    "Give me a fact about Cyber Security."
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "You can ask me to tell you a fact by saying, " \
                    "Give me a fact about Cyber Security."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Hope you enjoyed hearing some infosec facts! " \
                    "Have a great day. "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))

infoSecFacts = [
    'MyDoom, first discovered in 2004, is considered to be the most expensive malware in infosec history. It became the fastest spreading email worm and caused an estimated $38.5 billion work of damage!',
    'An international cyber crime ring based out of Eastern Europe managed to steal $1 billion in 2 years from 100 different banks in nearly 30 countries using spear phishing emails targeting bank employees.',
    'Hacktivism accounts for half of the cyber attacks launched in the world.',
    'The estimated global cost of Cyber attacks annually is $400 billion.',
    'In 2016 the estimated global expenditure on security products was $81.6 billion',
    'According to the Cyber Security Community, cybercrime damage is likely to hit $6 trillion annually by 2021',
    'Over the next five years, cybersecurity expenditure is likely to exceed $1 trillion',
    'The number of vacant cyber security jobs is likely to reach up to 1.5 million by 2019',
    'Global ransomware damage costs are predicted to exceed $5 billion in 2017. Thats up from $325 million in 2015, a 15 times increase in two years.',
    'The Deepweb refers to part of the Internet, specifically the world wide web, so anything that starts www, that isnt indexed by search engines, so cant be accessed by Google.',
    'The Darknet refers to non-www networks, where users may need separate software to access them. For example, Silk Road is hosted on [Darknet] networks like I2P and Tor.',
    'According to the UK Department for Culture, Media and Sport; Just under half (46%) of all UK businesses identified at least one cyber security breach or attack in the last year. Study March 2017',
    'More than 4,000 ransomware attacks have occurred every day since the beginning of 2016.',
    'In 2016 95 percent of breached records came from three industries in 2016: Government, retail, and technology',
    'Around one billion accounts and records were compromised worldwide in 2016. Thats roughly three for every American citizen',
    '64% of companies have experienced web-based attacks.',
    'In 2016, 40% of companies expect a data breach caused by malicious insiders',
    '62% of companies have experienced phishing & social engineering attacks.',
    'The median number of days that attackers stay dormant within a network before detection is over 200',
    'Average time to detect a malicious or criminal attack by a global study sample of organizations was 170 days',
    'There were 56,000 ransomware infections in March 2016, alone',
    'According to a study by Webroot in 2015, 97% of malware is unique to a specific endpoint, rendering signature-based security virtually useless',
    'In May 2016, once-popular social networking site Myspace announced that it was the victim of one of the largest data breaches in history. Over 360 million accounts were compromised, including the email addresses and passwords of past users. It is not known when the initial breach occurred.',
    'In late 2014, a "state-sponsored actor" hacked former Internet giant Yahoo, compromising a record 500 million accounts. The criminals made off with names, email addresses, telephone numbers, dates of birth, encrypted passwords, and the answers to users security questions.',
    'Daily deals company LivingSocial had its network compromised in 2013, with hackers stealing roughly 50 million names, email addresses, birthdays, and encrypted passwords from its SQL database.',
    'In 2004, online auction house eBay suffered the largest hack in U.S. history, losing 145 million login credentials to a hacker using an internal eBay corporate account. Names, email and street addresses, phone numbers, and birth dates were compromised.',
    'Credit and debit card processing firm Heartland Payment Systems became one of the largest data breach victims in U.S. history when hackers compromised more than 130 million accounts in 2008.'
    ]
    

def set_fact_in_session(intent, session):
    
    card_title = 'InfoSec Fact'
    session_attributes = {}

    if intent['name'] == 'factIntent':
        speech_output = random.choice(infoSecFacts)
        reprompt_text = None
        should_end_session = True
    else:
        speech_output = "I'm not sure what you said. " \
                        "Please try again."
        reprompt_text = "I'm not sure what your asking. " \
                        "You can ask me to tell you a fact by saying, " \
                        "Give me a fact about Cyber Security."
        should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "factIntent":
        return set_fact_in_session(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    if (event['session']['application']['applicationId'] !=
            "amzn1.ask.skill.50158b1a-edbf-445b-85fe-fa098855c4f9"):
    	raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
