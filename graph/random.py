"""
Generates random numbers and configure web socket.
"""
import threading
from random import random
from channels import Group


def sendmsg(num):
    Group('graphing').send({'text': num})


timer = 0


def random_generator():
    global timer
    n = random()
    sendmsg(str(n))
    timer = threading.Timer(1, random_generator)
    timer.start()


def ws_message(message):
    global timer
    print(message.content['text'])
    if (message.content['text'] == 'start'):
        random_generator()
    else:
        timer.cancel()


def ws_connect(message):
    Group('graphing').add(message.reply_channel)
    Group('graphing').send({'text': 'connected'})


def ws_disconnect(message):
    Group('graphing').send({'text': 'disconnected'})
    Group('graphing').discard(message.reply_channel)
