import sys
import trace
from typing import List, Dict
import random

def tracefunc(frame, event, arg):
    if event == "call":
        print(f"Call to {frame.f_code.co_name} in {frame.f_code.co_filename} at line {frame.f_lineno}")
    elif event == "return":
        print(f"Return from {frame.f_code.co_name} in {frame.f_code.co_filename} at line {frame.f_lineno}")
    return tracefunc

def binary_search(l: List, target: int) -> bool:
    """
    
    Function to perform binary search in a list
    
    """
    l = sorted(l)
    start, end = 0, len(l) - 1
    while(start <= end):
        mid = start + (end - start)//2
        if l[mid] == target:
            return True
        elif l[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return False

def main():
    max_range = 100
    l = [random.randint(0, max_range)**2 for d in range(max_range)]
    targets = []
    searches = []
    for _ in range(10):
        target = random.randint(0, max_range)
        search_result = binary_search(l = l, target = target)
        targets.append(target)
        searches.append(search_result)
    
    return l, targets, searches

# Start tracing
sys.settrace(tracefunc)
# Run your code here
main()
# Stop tracing
sys.settrace(None)