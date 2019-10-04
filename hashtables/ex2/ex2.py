#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)

# tickets = [
#   Ticket{ source: "PIT", destination: "ORD" },
#   Ticket{ source: "XNA", destination: "CID" },
#   Ticket{ source: "SFO", destination: "BHM" },
#   Ticket{ source: "FLG", destination: "XNA" },
#   Ticket{ source: "NONE", destination: "LAX" },
#   Ticket{ source: "LAX", destination: "SFO" },
#   Ticket{ source: "CID", destination: "SLC" },
#   Ticket{ source: "ORD", destination: "NONE" },
#   Ticket{ source: "SLC", destination: "PIT" },
#   Ticket{ source: "BHM", destination: "FLG" }
# ]

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
    
    location = "NONE"
    for i in range(length):
        dest = hash_table_retrieve(hashtable, location)
        # if dest == "NONE":
        #     continue
        # else:
        route[i] = dest
        location = dest

    return route

if __name__ == "__main__":
    # tickets = [
    #     Ticket("PIT", "ORD"),
    #     Ticket("XNA", "CID"),
    #     Ticket("SFO", "BHM"),
    #     Ticket("FLG", "XNA"),
    #     Ticket("NONE", "LAX"),
    #     Ticket("LAX", "SFO"),
    #     Ticket("CID", "SLC"),
    #     Ticket("ORD", "NONE"),
    #     Ticket("SLC", "PIT"),
    #     Ticket("BHM", "FLG")
    # ]
    ticket_1 = Ticket("NONE", "PDX")
    ticket_2 = Ticket("PDX", "DCA")
    ticket_3 = Ticket("DCA", "NONE")

    tickets = [ticket_1, ticket_2, ticket_3]
    print(reconstruct_trip(tickets, 3))