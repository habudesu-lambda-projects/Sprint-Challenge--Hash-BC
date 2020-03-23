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
    def __str__(self):
        return f'({self.source}, {self.destination})'


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * (length - 1)

    current_ticket = None
    for ticket in tickets:
        if ticket.source == 'NONE':
            current_ticket = ticket
        hash_table_insert(hashtable, ticket.source, ticket)

    index = 0
    while current_ticket.destination != "NONE":
        print(current_ticket)
        route[index] = current_ticket.destination
        next_ticket = hash_table_retrieve(hashtable, current_ticket.destination)
        index += 1
        current_ticket = next_ticket

    return route
