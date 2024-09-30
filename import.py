import sys
import json
from pymongo import MongoClient
from bson import json_util, ObjectId
from bson.json_util import loads, dumps

def convert_bson_types(obj):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == '$oid':
                return ObjectId(v)
            elif isinstance(v, dict):
                obj[k] = convert_bson_types(v)
            elif isinstance(v, list):
                obj[k] = [convert_bson_types(item) for item in v]
    return obj

def import_mongodb(url, input_file):
    try:
        # Connect to MongoDB
        client = MongoClient(url)
        
        # Get the database name from the URL
        db_name = url.split('/')[-1].split('?')[0]
        db = client[db_name]
        
        # Read data from file
        with open(input_file, 'r') as f:
            data = json.load(f)
        
        # Iterate through all collections in the data
        for collection_name, documents in data.items():
            collection = db[collection_name]
            
            # Clear existing data in the collection
            collection.delete_many({})
            
            # Parse and insert new data
            if documents:
                for doc in documents:
                    # Convert BSON types
                    converted_doc = convert_bson_types(doc)
                    # Insert the document
                    collection.insert_one(converted_doc)
            
            print(f"Imported {len(documents)} documents into {collection_name}")
        
        print(f"Database imported successfully from {input_file}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python import_script.py <mongodb_url> <input_file>")
        sys.exit(1)
    
    mongodb_url = sys.argv[1]
    input_file = sys.argv[2]
    
    import_mongodb(mongodb_url, input_file)