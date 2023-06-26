import socket
import sys
import time
import queue
import threading

message_queue = queue.Queue()

def get_new_message(client):
    message = conn.recv(1024)
    message = message.decode()
    return client + ':' + message

def send_new_message():
    while True:
        message = input('Me : ')
        conn.send(message.encode())
    #send_new_message(message.encode())

def listen():
    while True:
        incoming_messaage = get_new_message(client)

        if incoming_messaage is not None:
            message_queue.put(incoming_messaage)

def process():
    while True:
        if not message_queue.empty():
            # Retrieve a message from the queue
            message = message_queue.get()

            print(message)

# Create Socket & Retreive hostname
new_socket = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)
port = 8899

# Binding host & Port
new_socket.bind((host_name, port))
print("Binding Successful!")
print("This is your IP: ", s_ip)

# Listen for Connections
name = input('Enter name: ')
new_socket.listen(1)

# Accepting Incoming Connections
conn, add = new_socket.accept()
print("Received connection from ", add[0])
print("Connection Established. Connection from: ", add[0])

# Storing Incoming Connection Data
client = (conn.recv(1024)).decode()
print(client + ' has connected.')
conn.send(name.encode())

# Setting up the threading
    
listener_thread = threading.Thread(target=listen)
processor_thread = threading.Thread(target=process)
response_thread = threading.Thread(target = send_new_message)

listener_thread.start()
processor_thread.start()
response_thread.start()

listener_thread.join()
processor_thread.join()
response_thread.join()
