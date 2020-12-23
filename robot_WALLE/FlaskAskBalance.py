#!/usr/bin/env python3
# Allows Alexa to command the Balboa to stand up or fall down
# Derived from examples in the Flask-Ask repo: https://github.com/johnwheeler/flask-ask

import serial

from flask import Flask
from flask_ask import Ask, statement

app = Flask(__name__)
ask = Ask(app, '/')

@ask.intent('StandUp')
def stand_up():
    speech_text = 'Muscles says its my time to shine'
    print("standing up");
 #   ser.write(b'forward')
    return statement(speech_text).simple_card('Muscles', speech_text)

@ask.intent('LayDown')
def law_down():
    speech_text = 'Muscles says my batteries were getting low anyway'
#    ser.write(b'f')
    return statement(speech_text).simple_card('Muscles', speech_text)

@ask.intent('Forward')
def law_down():
    speech_text = 'Onward!!'
    ser.write(b'forward')
    return statement(speech_text).simple_card('Muscles', speech_text)

@ask.intent('Stop')
def law_down():
    speech_text = 'I\'ll rest for now!!'
    ser.write(b'stop')
    return statement(speech_text).simple_card('Muscles', speech_text)

@ask.intent('Greet')
def law_down():
    speech_text = 'Nice to meet you, I am steven\'s robot!!!'
    ser.write(b'greet')
    return statement(speech_text).simple_card('Muscles', speech_text)

@ask.intent('Roam')
def law_down():
    speech_text = 'I will go explore'
    ser.write(b'wander')
    return statement(speech_text).simple_card('Muscles', speech_text)


if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 9600)
    app.run()
