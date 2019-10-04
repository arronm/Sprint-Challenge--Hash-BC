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

    # construct hash table
    for i in range(length):
        # look for starting point while constructing hash
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)

    # set initial location
    location = "NONE"
    for i in range(length):
        dest = hash_table_retrieve(hashtable, location)
        route[i] = dest
        location = dest

    return route


if __name__ == "__main__":
    ticket_1 = Ticket("NONE", "PDX")
    ticket_2 = Ticket("PDX", "DCA")
    ticket_3 = Ticket("DCA", "NONE")

    tickets = [ticket_1, ticket_2, ticket_3]
    print(reconstruct_trip(tickets, 3))
