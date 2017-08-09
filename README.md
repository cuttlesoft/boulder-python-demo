Boulder Python demo - Alexa Skills
==================================

This repository holds the code examples for my talk on Alexa Skill development with Python. I gave this talk at Boulder-Python on
August 8, 2017.

# Project Organization

There's one file for each skill example; 1. `simple.py`, 2. `complex.py`

Likewise, there's a folder called `speech_assets` where I've added the assets required for each skill, namely the "Sample Utterances", "Intent Schema", and any "Custom Slots". You'll find the assets for each skill in the sub-folders `simple` and `complex`.

# Simple Skill

This was a simple example of a skill written in pure Python (no external dependencies) - it returns a simple Alexa speech response
when the user requests the `CuttlefishFactIntent`.

# Complex Skill

This example utilized the [Flask-Ask](https://github.com/johnwheeler/flask-ask) extension to make a skill where the user can tell
Alexa their favorite 'Fourteener' mountain (for those found in Colorado), and Alexa will remember it using a `session`.

The Flask-Ask library is impressively documented ([flask-ask.readthedocs.io](https://flask-ask.readthedocs.io/en/latest/)) and in addition there are several great tutorials and resources to help you learn more
about developing for Alexa:

 * [Alexa Skills Kit / Flask-Ask Quickstart ](https://alexatutorial.com/)
 * [Alexa Blogs: Flask-Ask: A New Python Framework for Rapid Alexa Skills Kit Development](https://developer.amazon.com/blogs/post/Tx14R0IYYGH3SKT/Flask-Ask-A-New-Python-Framework-for-Rapid-Alexa-Skills-Kit-Development)