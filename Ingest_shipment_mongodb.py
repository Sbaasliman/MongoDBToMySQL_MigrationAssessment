import socket
import pymongo
import json

# MongoDB connection
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['database']
collection = db['shipment_data']

# TCP Server setup
TCP_IP = '0.0.0.0'
TCP_PORT = 8282
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

print(f"Listening on {TCP_IP}:{TCP_PORT}")

while True:
    conn, addr = s.accept()
    print('Connection address:', addr)
    
    while True:
        data = conn.recv(BUFFER_SIZE)
        if not data:
            break
        shipment_data = json.loads(data.decode('utf-8'))
        collection.insert_one(shipment_data)

    conn.close()
