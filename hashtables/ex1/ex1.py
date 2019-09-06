#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    #Loop through

    for i in range(length):
        
        # weight is the weight at i
        weight = weights[i]


        # weight_limit is the limit minus the weight

        weight_limit = limit - weight

        # retrieve the weight_limit and set it as index_pair

        index_pair = hash_table_retrieve(ht, weight_limit)

        # if index_pair is not None and higher than i it'll be index_pair first, else it'll be i first

        if index_pair is not None:
             group = (index_pair, i) if i < index_pair else (i, index_pair)

            # return the group once we know what order it should go in 
             return group

         # finally insert everything into the hash table   
         #  
        hash_table_insert(ht, weight, i)
       

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
