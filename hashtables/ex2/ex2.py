#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    for ticket in tickets:
        # insert a hash for each ticket
        hash_table_insert(hashtable, ticket.source, ticket.destination)

        find_location = hash_table_retrieve(hashtable, ticket.destination)
        
    for i in range(length):
        route[i] = find_location
        find_location = hash_table_retrieve(hashtable, find_location)
        
    return route