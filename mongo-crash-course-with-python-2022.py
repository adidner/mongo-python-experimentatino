from pymongo import MongoClient
import datetime

# SETUP:

cluster = "mongodb://localhost:27017"
client = MongoClient(cluster)

print(client.list_database_names())

test_db = client["test-db"]

print(test_db.list_collection_names())


# Insertion

todo_item = {
    "name": "Patrick",
    "text": "first todo",
    "tags": ["python", "coding"],
    "date": datetime.datetime.utcnow()
}

test_collection = test_db["test-collection"]

# Inserting 1 object into DB
# result = test_collection.insert_one(todo_item)

todo_many = [
    {
        "name": "Mary",
        "text": "many todo 1",
        "tags": ["C", "meh"],
        "date": datetime.datetime.utcnow()
    },
    {
        "name": "Jackie",
        "text": "many todo 2",
        "tags": ["R", "ble"],
        "date": datetime.datetime.utcnow()
    }
]

# Inserting list of objects into DB
# result = test_collection.insert_many(todo_many)


# Querying


# returns the first match that has at least the same attributes and values as the passed one
result = test_collection.find_one({"name": "Mary"})
# print(result)

# Querying list objects (you only give one match for the list to match and if anything has a submatch it grabs it), returns entire matching object
next = test_collection.find_one({"tags":"R"})
# print(next)

# Query by objectId
from bson.objectid import ObjectId
elsy = test_collection.find_one({"_id": ObjectId("641f9492d7e235d232a58ec7")})
# print(elsy)

# Query for all matching things, KEEP IN MIND our results object is used up when access so if you cast it or print it or whatever it becomes empty
results = test_collection.find({"name": "Patrick"})

# print(list(results))

# for result in results:
    # print(result)


# Counts all documents
# print(test_collection.count_documents({"tags": "R"}))
# print(test_collection.count_documents({"tags": "RRR"}))


# Querying for a less than something, $lg, $gt, https://www.mongodb.com/docs/manual/reference/operator/query/
# d = datetime.datetime(2021, 2, 1)
# results = test_collection.find({"date": {"$gt": d}}).sort("name") # also sorts by the name key 
# print(list(results))


# Deleteing items
# result = test_collection.delete_one({"name": "Mary"})

# test_collection.delete_many({"name": "Patrick"})



# Updating items, update operators https://www.mongodb.com/docs/manual/reference/operator/update/

# results = test_collection.update_one({"name": "Jackie"}, {"$set": {"status": "updated"}})
results = test_collection.update_one({"name": "Jackie"}, {"$set": {"status": "updated more"}}) # updates value, adds or overrides
results = test_collection.update_one({"name": "Jackie"}, {"$unset": {"status": None}}) # deletes attribute





