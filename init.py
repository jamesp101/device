from socketIO_client_nexus import SocketIO, LoggingNamespace
import requests
import tkinter as tk
import threading
import sys

import ui

import socket_manager as sm

global threadWindow
global threadSocket


global window


def on_connect():
    print('connect')


def on_disconnect():
    print('disconnect')


def on_reconnect():
    print('reconnect')


def on_aaa_response(*args):
    print('on_aaa_response', args)


def stopThread(thread: threading.Thread):
    thread.join()


def close():
    stopThread(threadSocket)
    sys.exit()




if __name__ == '__main__':
    threadSocket = threading.Thread(target=sm.get_socktet, args=())
    threadSocket.daemon = True
    threadSocket.start()

    threadWindow = threading.Thread(target=ui.get_window.mainloop, args=())
    threadWindow.start()
