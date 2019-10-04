#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


# input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
# output: [ 3, 1 ] since these are the indices of weights 15 and 6 whose sum equals 21

def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for i in range(length):
        target = limit - weights[i] # 4 // 4
        check = hash_table_retrieve(ht, target) # None // 0
        if check is not None:
            return [i, check] # [1, 0]

        hash_table_insert(ht, weights[i], i) # {4: 0}

    return None


def print_answer(answer):
    if answer is not None:
        print(f'({answer[0]}, {answer[1]})')
    else:
        print("None")

if __name__ == "__main__":
    answer = get_indices_of_item_weights([ 4, 4 ], 2, 8)
    print_answer(answer)
