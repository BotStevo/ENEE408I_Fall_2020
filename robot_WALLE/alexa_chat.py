#!/usr/bin/env python3
# Allows Alexa to command the Balboa to stand up or fall down
# Derived from examples in the Flask-Ask repo: https://github.com/johnwheeler/flask-ask

import time
import serial
from robot_chat_client import RobotChatClient
from flask import Flask
from flask_ask import Ask, statement

ngrokLink = '1456bfb9148e.ngrok.io'     # EDIT ME!!
alexa_skill_name = "Muscles"            # EDIT ME!!  
username = "Wall-E"                     # EDIT ME!!
app = Flask(__name__)
ask = Ask(app, '/')

'''
    This section of code contains all the intent responses.
    (Change this with your own intents / Serial Messages)
'''

@ask.intent('Forward')
def respond():
    serial_message = 'forward'
    chat_message = "my robot is going forward"
    speech_text = 'I am going forward.'

    ser.write(serial_message.encode('utf-8'))

    if chat_message != "":   
        client.send({ 
            'type': 'message', 
            'user': username,
            'message': chat_message})

    return statement(speech_text).simple_card(alexa_skill_name, speech_text)

@ask.intent('Stop')
def respond():
    serial_message = 'stop'
    chat_message = "my robot is stopping"
    speech_text = 'I have stopped.'

    ser.write(serial_message.encode('utf-8'))

    if chat_message != "":
        client.send({
            'type': 'message',
            'user': username,
            'message': chat_message})

    return statement(speech_text).simple_card(alexa_skill_name, speech_text)

@ask.intent('Greet')
def respond():
    serial_message = 'greet'
    chat_message = "my robot is greeting"
    speech_text = 'Nice to meet you, I am steven\'s robot!!!'

    ser.write(serial_message.encode('utf-8'))

    if chat_message != "":
        client.send({
            'type': 'message',
            'user': username,
            'message': chat_message})

    return statement(speech_text).simple_card(alexa_skill_name, speech_text)

@ask.intent('Roam')
def respond():
    serial_message = 'wander'
    chat_message = "my robot is roaming"
    speech_text = 'I will go explore'

    ser.write(serial_message.encode('utf-8'))

    if chat_message != "":
        client.send({
            'type': 'message',
            'user': username,
            'message': chat_message})

    return statement(speech_text).simple_card(alexa_skill_name, speech_text)

@ask.intent('AskOthersToStop')
def respond():
    serial_message = 'stop'
    chat_message = ""
    command = 0
    speech_text = 'I asked the others to stop'

    ser.write(serial_message.encode('utf-8'))

    if chat_message != "":
        client.send({
            'type': 'message',
            'user': username,
            'message': chat_message})

    if command != "":
        client.send({'type': 'command',
                     'user': username,
                     'command': command})

    return statement(speech_text).simple_card(alexa_skill_name, speech_text)

@ask.intent('AskOthersToGo')
def respond():
    serial_message = 'forward'
    chat_message = ""
    command = 1
    speech_text = 'I asked the others to go'

    ser.write(serial_message.encode('utf-8'))

    if chat_message != "":
        client.send({
            'type': 'message',
            'user': username,
            'message': chat_message})

    if command != "":
        client.send({'type': 'command',
                     'user': username,
                     'command': command})

    return statement(speech_text).simple_card(alexa_skill_name, speech_text)

def recieve_message(message_dict):

    if message_dict['type'] == 'message':
        print('\n{0} : {1}\n'.format(message_dict['user'], message_dict['message']))

    elif message_dict['type'] == 'command':
        print('Receieved Command From:{0} Command:[1}'.format(
              message_dict['user'],
              message_dict['command']))
        ser.write(int(message_dict['command']))

    elif message_dict['type'] == 'users':
        print('Number of users: {}'.format(message_dict['count']))

def connectChat():
    print('Creating RobotChatClient object')
    global client
    client = RobotChatClient('wss://' + ngrokLink, callback=recieve_message)
    print("Connected!")

    time.sleep(1)

    client.send({'type': 'message',
        'user': 'User Joined: Alexa Chat Test',
                 'foo': username})

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 9600)
    connectChat()
    app.run()
