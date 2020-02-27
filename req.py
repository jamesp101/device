import requests

import config


address = "http://"+config.HOST+":" + config.PORT

print(address+"/device/1")

r = requests.get(address + "/device/1")

print(r)
