import sys
import json
from pymongo import MongoClient
from bson import json_util

def export_mongodb(url, output_file):
    try:
        # Connect to MongoDB
        client = MongoClient(url)
        
        # Get the database name from the URL
        db_name = url.split('/')[-1].split('?')[0]
        db = client[db_name]
        
        # Get all collections
        collections = db.list_collection_names()
        
        # Create a dictionary to store all data
        data = {}
        
        # Iterate through all collections
        for collection_name in collections:
            collection = db[collection_name]
            data[collection_name] = list(collection.find())
        
        # Write data to file
        with open(output_file, 'w') as f:
            json.dump(data, f, default=json_util.default, indent=2)
        
        print(f"Database exported successfully to {output_file}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <mongodb_url> <output_file>")
        sys.exit(1)
    
    mongodb_url = sys.argv[1]
    output_file = sys.argv[2]
    
    export_mongodb(mongodb_url, output_file)