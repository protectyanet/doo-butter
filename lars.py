import socket
import json

#input target domain and target port to establish connection
#this is only a 1/4 of this project, other parts are being worked on


t = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = input('Enter a website: ')
port = int(input("Enter Desired Port Number: "))

ip_pull = socket.gethostbyname(server)

try:
    if server.startswith (''): 
        print("Ip Address: "+ip_pull)
        
    request = "GET / HTTP/1.1\nHost: "+server+"\n\n"
    t.connect((server, port))
    t.send(request.encode())
    result = t.recv(4096)
    print(result)

try:
    
    for port in range (0,65536, 1):

        print("Connecting on"+socket.getservbyport(port)+"port.")

except:
    print("Port/Proto not found")

