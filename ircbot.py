import socket 

# No magic numbers!
recvBytes = 2048

# Hardcode values below
server  = ""
channel = ""
botnick = ""

# Ping the server
def ping():
  ircsock.send(bytes("PONG :pingis\n", 'utf-8'))  

# Send message to the server
def sendMessage(chan , msg):
  ircsock.send(bytes("PRIVMSG "+ chan +" :"+ msg +"\n", 'utf-8')) 

# Join a channel
def joinChannel(chan):
  ircsock.send(bytes("JOIN "+ chan +"\n", 'utf-8'))

# Send "hello world" message to server
def helloWorld():
  ircsock.send(bytes("PRIVMSG "+ channel +" :Hello world!\n", 'utf-8'))
            
# Connect to the server                  
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, 6667))

# Send a greeting message
msg = bytes("USER " + botnick + " " + botnick + " " + botnick + 
  "Hello, this is an IRC bot!\n", 'utf-8')
ircsock.send(msg)
msg = bytes("NICK "+ botnick + "\n", 'utf-8')
ircsock.send(msg)

joinChannel(channel)

# Infinite loop reads bytes from server and responds to a specific message
while True:
  msg = ircsock.recv(recvBytes)
  msg = ircmsg.strip(bytes('\n\r', 'utf-8'))
  print(msg)

  # sendMessage(channel, "Hello!")

  if msg.find(bytes(":Hello " + botnick, 'utf-8')) != -1:
    helloWorld()

  if ircmsg.find(bytes("PING :", 'utf-8')) != -1:
    ping()
