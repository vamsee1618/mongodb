import pymongo
import re
client = pymongo.MongoClient("mongodb://localhost:27017/")
db_pokemon = client["samples_pokemon"]
collection_pokemon = db_pokemon["samples_pokemon"]

def print_func(res_obj):
    for i in res_obj:
        print(i)

### Question-1
print("Question-1")
bday = 8 + 16
query_candy = {"candy_count": {"$gte": bday}}
projection = {"_id": 1, "name": 1}
result_candy = collection_pokemon.find(query_candy, projection)
print_func(result_candy)

### Question-2
print("Question-2")
query_num = {"num": {"$in": ['008', '016']}}
result_num = collection_pokemon.find(query_num, projection)
print_func(result_num)


db_crunch = client["crunchbase"]
collection_crunch = db_crunch["crunchbase_database"]

### Question-3
print("Question-3")
regex_crunch = re.compile(".text.")
query_crunch = {"tag_list": {"$regex": regex_crunch}}
result_crunch = collection_crunch.find(query_crunch, projection)
print_func(result_crunch)

### Question-4
print("Question-4")
regex_twit = re.compile(".*@gmail\.com$")
query = {
    "$or": [
        {"founded_year": {"$gte": 2000, "$lte": 2010}},
        {"email_address": {"$regex": regex_twit}}
    ]
}
projection_que = {"_id": 1, "name": 1, "twitter_username": 1}
result_twit = collection_crunch.find(query, projection_que)
print_func(result_twit)