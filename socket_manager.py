from socketIO_client_nexus import SocketIO, LoggingNamespace
import config




def on_connect():
    print('Connected to Server')

def on_disconnect():
    print('Disconnected from server')


def on_reconnect():
    print('Reconnected from server')





socketIO = SocketIO(config.HOST, config.PORT,   LoggingNamespace)
socketIO.on('connenct', on_connect)
socketIO.on('disconnect', on_disconnect)
socketIO.on('reconnect', on_reconnect)





def get_socktet():
    return socketIO
