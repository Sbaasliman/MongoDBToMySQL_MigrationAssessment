import pymongo
import mysql.connector

# MongoDB connection
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['database']  # Replace 'your_database' with the actual MongoDB database name
collection = db['shipment_data']  # Replace 'shipment_data' with the actual MongoDB collection name

# MySQL connection
mysql_conn = mysql.connector.connect(
    host="your_mysql_host",  # Replace with your MySQL host
    user="admin",            # Replace with your MySQL username
    password="your_password",# Replace with your MySQL password
    database="your_database" # Replace with your MySQL database name
)
cursor = mysql_conn.cursor()

# Migrate data
for document in collection.find():
    cursor.execute(
        """
        INSERT INTO shipment_data (shipment_id, origin, destination, weight) 
        VALUES (%s, %s, %s, %s)
        """,
        (
            document['shipment_id'], 
            document['origin'], 
            document['destination'], 
            document['weight']
        )
    )

mysql_conn.commit()
cursor.close()
mysql_conn.close()
