#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)
                        


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    # Loop through tickets and check if it has a source of NONE, if so 
    # we know thats the start and where the ticket destination will be

    for t in tickets:
        if t.source == "NONE":
            route[0] = t.destination

    # if there is no NONE insert the source and destination to the hashtable
            
        else:
            hash_table_insert(hashtable, t.source, t.destination)

    # Loop through the route and next route will start with the destination from the last one(i-1)

    for i in range(1, len(tickets)):
        route[i] = hash_table_retrieve(hashtable, route[i-1])

    return route
