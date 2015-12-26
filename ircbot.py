import socket 

# No magic numbers!
recvBytes = 2048

# Hardcode values below
server  = ""
channel = ""
botnick = ""

def ping():
  """Ping the server."""

  ircsock.send(bytes("PONG :pingis\n", 'utf-8'))  

def sendMessage(chan, msg):
  """Send message to the server."""

  ircsock.send(bytes("PRIVMSG "+ chan +" :"+ msg +"\n", 'utf-8'))

def joinChannel(chan):
  """Join a channel."""

  ircsock.send(bytes("JOIN "+ chan +"\n", 'utf-8'))

def helloWorld():
  """Send "hello world" message to the server."""

  ircsock.send(bytes("PRIVMSG "+ channel +" :Hello world!\n", 'utf-8'))
            
def main():
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

if __name__ == "__main__":
  main()
