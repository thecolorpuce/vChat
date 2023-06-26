import socket,sys,time, queue, threading

message_queue = queue.Queue()

def get_new_message():
    message = (socket_server.recv(1024)).decode()

    return message

def send_new_message():
    while True:
        message = input('Me : ')
        socket_server.send(message.encode())

def listen():
    while True:
        incoming_message = get_new_message()

        if incoming_message is not None:
            message_queue.put(incoming_message)


def process():
    while True:
        if not message_queue.empty():
            message = message_queue.get()

            print(message)


#Create the socket & Accept user input as hostname
socket_server = socket.socket()
server_host = socket.gethostname()
ip = socket.gethostbyname(server_host)
sport = 8899

# Connect to Server
print("This is your IP: ", ip)
server_host = input("Enter Server IP: ")
name = input("Enter Server name: ")

socket_server.connect((server_host, sport))

# Receiving Packets from server
socket_server.send(name.encode())
server_name = socket_server.recv(1024)
server_name = server_name.decode()

print(server_name, " has joinded...")

#Threading
listener_thread = threading.Thread(target=listen)
processor_thread = threading.Thread(target=process)
response_thread = threading.Thread(target = send_new_message)

listener_thread.start()
processor_thread.start()
response_thread.start()

listener_thread.join()
processor_thread.join()
response_thread.join()