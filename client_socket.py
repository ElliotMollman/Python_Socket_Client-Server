import socket

"""

bind() acts locally, which is to say it binds the end of the connection on the machine on which it is called, to the
requested address and assigns the requested port to you. It does that irrespective of whether that machine will be a 
client or a server. connect() initiates a connection to a server, which is to say it connects to the requested address 
and port on the server, from a client. That server will almost certainly have called bind() prior to listen(), in order 
for you to be able to know on which address and port to connect to it with using connect().

If you don't call bind(), a port and address will be implicitly assigned and bound on the local machine for you when you 
call either connect() (client) or listen() (server). However, that's a side effect of both, not their purpose. A port 
assigned in this manner is ephemeral.

An important point here is that the client does not need to be bound, because clients connect to servers

"""


def connect(dest_ip, dest_port, message):
    try:
        TCP_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # socket.AF_INET tells python the address family we are using, which is ipv4. We can use socket.AF_INET6 for ipv6 addresses.
        # SOCK_STREAM is the socket type for TCP, and the timeout for packets is specified
        TCP_sock.connect((dest_ip, dest_port))
        # .connect() will keep connection alive until .clos()'ed
        #TCP_sock.send(("GET /" + dest_ip + " HTTP/1.1\r\n").encode(encoding="ascii", errors="ignore"))
        TCP_sock.send(bytes(message, "utf-8"))
        data = TCP_sock.recv(1024)
        print(f"received data: {data}")

        # Python uses backslashes as escape characters. Prefacing the string definition with 'r' is a useful way to define a string
        # where you need the backslash to be an actual backslash and not part of an escape code that means something else in the string.
    except:
        print("failed to connect")


dest_ip = input("Enter destination IP address: \n")
dest_port = 80
message = "Hi"
connect(dest_ip, dest_port, message)