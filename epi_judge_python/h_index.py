from typing import List

from test_framework import generic_test


def h_index(citations: List[int]) -> int:
    
    ## Brute Force Solution
    ## Time: O(n^2)
    ## Space: O(n)
    # citations.sort()
    
    # count = 1
    # while True:
    #     local_count = 0
    #     for cit in citations:
    #         if cit >= count:
    #             local_count += 1
                
    #     if local_count < count:
    #         return count - 1
                
    #     count += 1
    
    
    ## Optimized Solution
    ## Time: O(n log n)
    ## Space: O(n)
    ### Note: The time complexity is actually the time it takes to sort O(n log n) added onto the 
    ### amount of time it takes for the loop O(n). But since O(n log n) is slower than O(n), O(n) drops. 
    citations.sort()
    length = len(citations)
    
    for index, cit in enumerate(citations):
        # Stop at the first citation where it's >= than the number of remaining papers left
        if cit >= length - index:
            return length - index
    
    return 0
    
    


if __name__ == '__main__':
    exit(generic_test.generic_test_main('h_index.py', 'h_index.tsv', h_index))
