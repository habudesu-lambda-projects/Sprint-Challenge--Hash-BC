#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    index = 0
    answer = None
    for weight in weights:
        value = hash_table_retrieve(ht, weight)
        if value == None:
            hash_table_insert(ht, limit - weight, index)
            index += 1
        else:
            if index > value:
                answer = (index, value)
                print(answer)
                break
            else:
                answer = (value, index)
                print(answer)
                break
    return answer


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
