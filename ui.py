import tkinter as tk
import config
import json
import socket_manager as socket


root = tk.Tk()

root.geometry('400x400')
root.title('Device UI')

label1 = tk.Label(root, text="Connected to: ", )
label1.grid(column=0, row=0,)
label2 = tk.Label(root, text="%s : %s" % (config.HOST, config.PORT))
label2.grid(column=0, row=1,)


# Status Start
tk.Label(root, text="Status:").grid(column=0, row=4)
labelStatus = tk.Label(root, text="DEV_STATUS").grid(column=1, row=4)
# Status End


def change_status():
    io = socket.get_socktet()

    io.on('status_response', lambda: print('on'))
    io.emit('status', json.dumps({'id': config.DEVICEID}))





buttonChangeStatus = tk.Button(root, text="Change Status", command=change_status) \
    .grid(column=4, row=4)


def runWindow():
    root.mainloop()

def get_window():
    return root



runWindow()
