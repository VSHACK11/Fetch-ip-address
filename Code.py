import socket

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
def getip():
  return local_ip
  
