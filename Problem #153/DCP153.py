#problem
'''
Find an efficient algorithm to find the smallest distance (measured in number of words) between any two given words in a string.

For example, given words "hello", and "world" and a text content of "dog cat hello cat dog dog hello cat world", return 1 because there's only one
word "cat" in between the two words.
'''
#samples
test1 = 'dog cat hello cat dog dog hello cat world'
test2 = 'You need to help Smith to develop a C code which finds the data in a linked list'
test3 = 'Well today was our English Common Revision test which went well'

#algo
def finddist(sen, key1, key2):
    sen = sen.split()
    sen = [x.lower() for x in sen]

    dist = 0

    if key1 not in sen:
        return None
    
    if key2 not in sen:
        return None

    for x in sen:
        if x == key1:
            dist = 0

        if x == key2:
            return dist-1 

        dist += 1

#testing
print(finddist(test1, 'hello', 'world'))
print(finddist(test2, 'develop', 'a'))
print(finddist(test3, 'revision', 'which'))

        


