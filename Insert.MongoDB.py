import pymongo

# MongoDB connection
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['your_database']  # Replace 'your_database' with the name of your MongoDB database
collection = db['shipment_data']  # Replace 'shipment_data' with the name of your collection

# Document to be inserted
document = {
    "shipment_id": "1234",
    "origin": "New York",
    "destination": "Los Angeles",
    "weight": 100.5
}

# Insert the document into the collection
result = collection.insert_one(document)

# Print the inserted document's ID
print("Document inserted with ID:", result.inserted_id)
