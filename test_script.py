from watch_tower import capture_calls, capture_objects
def add(a, b):
    return a+b

# Example usage
@capture_calls
def add(a, b):
    return a + b

@capture_objects
class MyClass:
    def __init__(self, x):
        self.x = x

# Test function calls and object creation
add(3, 5)
obj1 = MyClass(10)
obj2 = MyClass(20)


