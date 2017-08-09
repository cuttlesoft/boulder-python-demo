# -*- coding: utf-8 -*-
"""
    complex-skill.py
    ~~~~~~~~~~~~~~~~
    an alexa skill that remembers your favorite 14er
"""

import logging

from flask import Flask, render_template
from flask_ask import Ask, session, question, statement


app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)


@ask.launch
def launch():
    card_title = render_template('card_title')
    question_text = render_template('welcome')
    reprompt_text = render_template('welcome_reprompt')
    return question(question_text).reprompt(reprompt_text).simple_card(card_title, question_text)


@ask.intent('MyFourteenerIsIntent', mapping={'fourteener': 'Fourteener'})
def my_fourteener_is(fourteener):
    card_title = render_template('card_title')
    if fourteener is not None:
        session.attributes["FOURTEENER"] = fourteener
        question_text = render_template('known_fourteener', fourteener=fourteener)
        reprompt_text = render_template('known_fourteener_reprompt')
    else:
        question_text = render_template('unknown_fourteener')
        reprompt_text = render_template('unknown_fourteener_reprompt')
    return question(question_text) \
        .reprompt(reprompt_text) \
        .simple_card(card_title, question_text)


@ask.intent('WhatsMyFourteenerIntent')
def whats_my_fourteener():
    card_title = render_template('card_title')
    fourteener = session.attributes.get("FOURTEENER")
    if fourteener is not None:
        statement_text = render_template('known_fourteener_bye', fourteener=fourteener)
        return statement(statement_text).simple_card(card_title, statement_text)
    else:
        question_text = render_template('unknown_fourteener_reprompt')
        return question(question_text) \
            .reprompt(question_text) \
            .simple_card(card_title, question_text)


@ask.session_ended
def session_ended():
    return "{}", 200


if __name__ == '__main__':
    app.run(debug=True)
