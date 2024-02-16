from pymongo import MongoClient, GEOSPHERE
from bson.son import SON
import pprint
import random

#db_uri = 'mongodb://localhost:27017'
db_uri = 'mongodb+srv://viraja:capstonecloudjan23@capstonecloud-iitm-gl-a.rnianxz.mongodb.net/'


# Create a List of taxis
taxi_list = [
            {
                'name': "Toofan",
                'type': "Luxury",
                'location': {
                    'type': "Point",
                    'coordinates': [28.65195, 77.23149]
                }
            },
            {
                'name': "Vimaan",
                'type': "Basic",
                'location': {
                    'type': "Point",
                    'coordinates': [28.61123, 77.23163]
                }
            },
            {
                'name': "Pavan",
                'type': "Deluxe",
                'location': {
                    'type': "Point",
                    'coordinates': [28.66542, 77.23154]
                }
            }
        ]

# Create a list of Customers
customer_list = [
                {
                    'name': "Mohan",
                    'location': {
                        'type': "Point",
                        'coordinates': [28.64454, 77.23098]
                    }
                },
                {
                    'name': "Isaac",
                    'location': {
                        'type': "Point",
                        'coordinates': [28.67676, 77.23156]
                    }
                },
                {
                    'name': "Amir",
                    'location': {
                        'type': "Point",
                        'coordinates': [28.65213, 77.23121]
                    }
                },
                {
                    'name': "Ashok",
                    'location': {
                        'type': "Point",
                        'coordinates': [28.66132, 77.23176]
                    }
                },
                {
                    'name': "Leonard",
                    'location': {
                        'type': "Point",
                        'coordinates': [28.67423, 77.23172]
                    }
                }
            ]


#Access the MongoDB Service
aggregator_cli = MongoClient(db_uri)

# Create a Database
aggregator_db = aggregator_cli['taxis_and_customers']

# Create Collections
taxis = aggregator_db['taxis']
res = taxis.delete_many({})

customers = aggregator_db['customers']
res = customers.delete_many({})

# Populate the Collections
res = taxis.insert_many(taxi_list)
res = customers.insert_many(customer_list)

# Display the Database Collections
print('########################### Aggregator: TAXIS ###########################')

for doc in taxis.find():
    pprint.pprint(doc)

print('########################### Aggregator: CUSTOMERS ###########################')

for doc in customers.find():
    pprint.pprint(doc)
    
# Create Index(es)
taxis.create_index([('location', GEOSPHERE)])
customers.create_index([('location', GEOSPHERE)])

# Run Queries

# Select a random Customer
random.shuffle(customer_list)
customer_loc = customer_list[0]['location']

print('######################## CUSTOMER LOCATION ########################')
pprint.pprint(customer_loc)

# Getting all taxis within a certain distance range from a customer
print('######################## ALL TAXIS WITHIN 1 KILOMETER ########################')

range_query = {'location': SON([("$near", customer_loc), ("$maxDistance", 1000)])}
for doc in taxis.find(range_query):
    pprint.pprint(doc)

# Getting the nearest taxis to a customer
print('######################## THE 2 NEAREST TAXIS ########################')

nearest_query = {'location': {"$near": customer_loc}}
for doc in taxis.find(nearest_query).limit(2):
    pprint.pprint(doc)