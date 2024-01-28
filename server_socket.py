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


def connect(Host, server_port):
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCP_sock:
        # socket.AF_INET tells python the address family we are using, which is ipv4. We can use socket.AF_INET6 for ipv6 addresses.
        # SOCK_STREAM is the socket type for TCP, and the timeout for packets is specified
		TCP_sock.bind((Host, server_port))
		# will bind to itself to the host and port we want to listen to
		TCP_sock.listen(5)
		# open to connections, with a maximum of 5 at once
		conn, addr = TCP_sock.accept()
		# accept incoming connections based on Host addresses
		print("hi")
		with conn:
			print(f"connected to {addr}")
			while True:
				data = TCP_sock.recv(1024)
				# receiving maximum of 1 byte od data
				if not data:
					break
				conn.sendall(data)

Host = ""
# empty string will accet any incoming ip connection
server_port = 80

connect(Host, server_port)
